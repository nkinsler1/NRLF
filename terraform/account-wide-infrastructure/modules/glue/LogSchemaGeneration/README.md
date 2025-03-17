# Log Schema Generation

The Glue script uses pyspark to process log data. Due to the structure of each json document inside of a log group differing, we need to account for this variance.

The notebook provides a way to automatically generate a pyspark schema for a log group without manual intervention. Point it at the desired group, and hit run all, then copy and paste the output into either producer_schema.py or consumer_schema.py.
