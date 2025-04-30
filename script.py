from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("DataProcessing").getOrCreate()

# Sample data
data = [("Alice", 34), ("Bob", 45), ("Charlie", 29)]
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Filter data
df_filtered = df.filter(df.Age > 30)

# Show results
df_filtered.show()

# Stop Spark session
spark.stop()
