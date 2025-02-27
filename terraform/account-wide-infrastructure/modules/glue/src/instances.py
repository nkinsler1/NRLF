import logging

from awsglue.context import GlueContext
from pyspark.sql import SparkSession


class GlueContextSingleton:
    """Singleton for GlueContext and SparkSession"""

    _instance = None

    def __new__(cls, spark_context):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.spark = SparkSession.builder.config(
                "spark.sql.caseSensitive", "true"
            ).getOrCreate()
            cls._instance.context = GlueContext(spark_context)
        return cls._instance


class LoggerSingleton:
    """Singleton for logger"""

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.logger = logging.getLogger("ETLLogger")
            cls._instance.logger.setLevel(logging.INFO)
        return cls._instance
