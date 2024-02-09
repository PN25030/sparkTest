from pyspark.sql import SparkSession
import pandas as pd
import uuid
import random

if __name__ == "__main__":
    sc = SparkSession.builder.appName("Hello").getOrCreate()
    names = (str(uuid.uuid4()) for _ in range(10))
    age = (random.randint(10, 26) for _ in range(10))
    data = {
        "names":names,
        "age":age
    }
    
    # data1 = sc.createDataFrame(data)
    pd1 = pd.DataFrame(data)
    print(pd1)
    

    df3 = sc.read.csv("sample.csv", header = True)
    df3.show()

    

