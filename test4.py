from pyspark.sql import SparkSession

sc = SparkSession.Builder().appName("Hello").getOrCreate()
print("In spark")
df = sc.read.csv("sample.csv", header = True)
df.show()