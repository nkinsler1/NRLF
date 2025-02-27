from pyspark.sql.functions import (
    coalesce,
    col,
    concat,
    explode_outer,
    from_unixtime,
    lit,
    regexp_replace,
    to_date,
    to_timestamp,
    when,
)
from pyspark.sql.types import ArrayType, StructType


def resolve_dupes(df):
    drop = []
    for i in range(len(df.columns)):
        for j in range(i + 1, len(df.columns)):
            if df.columns[i].lower() == df.columns[j].lower():
                df = df.withColumn(
                    df.columns[i].lower() + "_",
                    when(
                        col(df.columns[i]).isNull() | col(df.columns[j]).isNull(),
                        coalesce(col(df.columns[i]), col(df.columns[j])),
                    ).otherwise(
                        concat(col(df.columns[i]), lit(","), col(df.columns[j]))
                    ),
                )
                drop.extend([df.columns[i], df.columns[j]])
    df = df.drop(*drop)

    return df


def flatten_df(df):
    complex_fields = dict(
        [
            (field.name, field.dataType)
            for field in df.schema.fields
            if type(field.dataType) == ArrayType or type(field.dataType) == StructType
        ]
    )
    while len(complex_fields) != 0:
        col_name = list(complex_fields.keys())[0]

        if type(complex_fields[col_name]) == StructType:
            expanded = [
                col(col_name + "." + k).alias(col_name + "_" + k)
                for k in [n.name for n in complex_fields[col_name]]
            ]
            df = df.select("*", *expanded).drop(col_name)

        elif type(complex_fields[col_name]) == ArrayType:
            df = df.withColumn(col_name, explode_outer(col_name))

        complex_fields = dict(
            [
                (field.name, field.dataType)
                for field in df.schema.fields
                if type(field.dataType) == ArrayType
                or type(field.dataType) == StructType
            ]
        )
    return df


def dtype_conversion(df):
    df = (
        df.withColumn(
            "event_timestamp_cleaned", regexp_replace(col("event_timestamp"), ",", ".")
        )
        .withColumn(
            "event_timestamp",
            to_timestamp(col("event_timestamp_cleaned"), "yyyy-MM-dd HH:mm:ss.SSSZ"),
        )
        .withColumn("time", from_unixtime(col("time")).cast("timestamp"))
        .withColumn("date", to_date(col("time")))
    )
    return df.drop("event_timestamp_cleaned")
