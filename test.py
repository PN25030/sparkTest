from pyspark.sql import SparkSession

#create a sample pyspark code
spark = SparkSession.builder \
    .appName("Simple PySpark Example") \
    .getOrCreate()

data = [("John", 25), ("Alice", 30), ("Bob", 35), ("Piyush", 38)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Show the DataFrame
df.show()

df_filter = df.filter(df["Age"]>25)
df_filter.show()

df_name_filter = df.filter(df["Name"]=="Piyush")
df_name_filter.show()

print("Hello world")