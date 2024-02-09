from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Hello World").getOrCreate()

df = spark.read.csv("sample.csv",header= True, inferSchema=True)

df.show()
print("Hello")
