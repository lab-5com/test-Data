from pyspark.sql import SparkSession
import dbldatagen as dg
from pyspark.sql.types import StringType, TimestampType, ShortType, LongType, DoubleType
from pathlib import Path
import shutil

def move_single_csv(name: str, output_dir: Path):
    parts_dir = output_dir / Path(name + ".csv.parts")
    part_file = next(parts_dir.glob('part-*.csv'))

    desired_csv_file = output_dir / f"{name}.csv"

    shutil.move(str(part_file), str(desired_csv_file))
    shutil.rmtree(parts_dir)

def main():
    spark = SparkSession.builder \
        .appName("Dataset Generation") \
        .getOrCreate()

    # Define and generate the product dataset
    product_ds = (
        dg.DataGenerator(sparkSession=spark, name="products", rows=20, partitions=1)
        .withIdOutput()
        .withColumn("product_id", LongType(), expr="id")
        .withColumn("product_name", StringType(), template="Product \\w", random=True)
        .withColumn("price", DoubleType(), minValue=1.0, maxValue=1000.0, precision=2)
        .withColumn("category", StringType(), values=["Electronics", "Clothing", "Home & Kitchen"], random=True)
    )

    product_df = product_ds.build()
    product_df.coalesce(1).write.csv("products.csv.parts", header=True, mode="overwrite")
    print("Moving products.csv to " + str(Path.cwd()))
    move_single_csv("products", Path.cwd())

    # Generate the sales dataset
    product_ids = [row.product_id for row in product_df.select("product_id").distinct().collect()]

    sales_ds = (
        dg.DataGenerator(sparkSession=spark, rows=1000000, partitions=4, name="sales")
        .withColumn("product_id", StringType(), values=product_ids, random=True)
        .withColumn("quantity", ShortType(), minValue=1, maxValue=10)
        .withColumn("sale_date", TimestampType(),
                    data_range=dg.DateRange("2017-10-01 00:00:00", "2018-10-06 11:55:00", "microseconds=3"), random=True)
    )

    sales_df = sales_ds.build().orderBy("sale_date")
    print("Moving sales.csv to " + str(Path.cwd()))
    sales_df.coalesce(1).write.csv("sales.csv.parts", header=True, mode="overwrite")
    move_single_csv("sales", Path.cwd())

if __name__ == '__main__':
    main()
