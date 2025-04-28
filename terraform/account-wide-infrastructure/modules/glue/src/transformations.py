from pyspark.sql.functions import (
    coalesce,
    col,
    concat,
    from_unixtime,
    lit,
    regexp_replace,
    to_date,
    to_timestamp,
    when,
)


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


def rename_cols(df):
    for col_name in df.columns:
        df = df.withColumnRenamed(col_name, col_name.replace(".", "_"))
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
