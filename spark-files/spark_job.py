from pyspark.sql import SparkSession
from pyspark import SparkConf

if __name__ == '__main__':

    spark = SparkSession \
            .builder \
            .appName("migration_snapshot") \
            .config("spark.sql.session.timeZone", "UTC") \
            .config("spark.sql.legacy.parquet.int96RebaseModeInWrite", "CORRECTED") \
            .config("spark.sql.legacy.parquet.datetimeRebaseModeInWrite", "CORRECTED") \
            .getOrCreate()

    print(SparkConf().getAll())

    spark.sparkContext.setLogLevel('INFO')

    load_df = spark.read \
        .format("jdbc") \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("url", "jdbc:mysql://XX.XX.XX.XX:3306/taxi?serverTimezone=UTC") \
        .option("user", "XXX") \
        .option("password", "XXX") \
        .option("dbtable", "drivers") \
        .option("pushDownPredicate", "false") \
        .option("fetchsize", f"1000") \
        .load()

    output_path = f"gs://datalake/snapshot/taxi/drivers"

    load_df.repartition(2).write.format("parquet").mode("overwrite").save(output_path)

    spark.stop()