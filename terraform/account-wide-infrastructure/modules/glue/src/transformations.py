from pyspark.sql.functions import (
    col,
    from_unixtime,
    regexp_replace,
    to_date,
    to_timestamp,
)
from pyspark.sql.types import StructType


def flatten_df(df):
    def flatten(schema, prefix=""):
        """
        Recursively traverse the schema to extract all nested fields.
        """
        fields = []
        for field in schema.fields:
            name = f"{prefix}.{field.name}" if prefix else field.name
            if isinstance(field.dataType, StructType):
                fields += flatten(field.dataType, name)
            else:
                alias_name = name.replace(".", "_")
                fields.append((name, alias_name))
        return fields

    flat_columns = flatten(df.schema)

    return df.select([col(c).alias(n) for c, n in flat_columns])


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
