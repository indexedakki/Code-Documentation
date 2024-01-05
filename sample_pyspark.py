from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Sample PySpark App") \
    .getOrCreate()

# Read data from CSV file
df = spark.read.csv("/path/to/your/file.csv", header=True, inferSchema=True)

# Show the first few rows of the DataFrame
df.show()

# Write DataFrame to Parquet file
df.write.parquet("/path/to/your/output.parquet", mode="overwrite")

# Select specific columns
selected_df = df.select("column1", "column2")

# Filter data based on a condition
filtered_df = df.filter(df["column1"] > 100)

# GroupBy and calculate aggregate functions
agg_df = df.groupBy("group_column").agg({"numeric_column": "mean", "another_column": "max"})

# Create a second DataFrame
df2 = spark.read.csv("/path/to/another/file.csv", header=True, inferSchema=True)

# Inner join based on a common column
joined_df = df.join(df2, on="common_column", how="inner")

# Define a simple UDF
@udf(StringType())
def uppercase_column(column_value):
    return column_value.upper()

# Apply the UDF to a DataFrame column
df_with_udf = df.withColumn("upper_column", uppercase_column(df["column"]))

# Prepare features and target column for Linear Regression
assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
assembled_df = assembler.transform(df).select("features", "target_column")

# Train a Linear Regression model
lr = LinearRegression(featuresCol="features", labelCol="target_column")
model = lr.fit(assembled_df)
