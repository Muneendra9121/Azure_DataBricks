# Databricks notebook source
# -- RDD
# -- Dataframes
# -- Datasets

# COMMAND ----------

data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
rdd

# COMMAND ----------

rdd.collect()

# COMMAND ----------

# map
def square(n):
    return n**2

rdd2 = rdd.map(square)
rdd2.collect()

# COMMAND ----------

# map
rdd2 = rdd.map(lambda x: x**2)
rdd2.collect()

# COMMAND ----------

# map in python
ls = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, ls))
squares

# COMMAND ----------

# filter 
rdd3 = rdd.filter(lambda x: x % 2 == 0)
rdd3.collect()

# COMMAND ----------

# flatMap
words_rdd = sc.parallelize(["Hello World", "Good Evening"])
# words_rdd.collect()
rdd4 = words_rdd.flatMap(lambda line: line.split(" "))
rdd4.collect()

# COMMAND ----------

rdd5 = words_rdd.map(lambda line: line.split(" "))
rdd5.collect()

# COMMAND ----------

# s = "Hello World"
# s.split()

# COMMAND ----------

# reduce
# rdd.collect() [1, 2, 3, 4, 5]
total = rdd.reduce(lambda x, y: x + y)
total

# COMMAND ----------

type(total)

# COMMAND ----------

# reduceByKey
data = [("a", 1), ("b", 2), ("c", 3), ("a", 4), ("c", 3)]
rdd = sc.parallelize(data)  # --> output [("a", 5), ("b", 2), ("c", 3)]
reduced = rdd.reduceByKey(lambda x, y: x + y)
reduced.collect()

# COMMAND ----------

# groupByKey
rdd7 = rdd.groupByKey()
# rdd.collect()
print([(k, list(v)) for k, v in rdd7.collect()])


# COMMAND ----------

print([(k, set(v)) for k, v in rdd7.collect()])

# COMMAND ----------

from pyspark.sql.functions import *
emp = [
    (1, "Alice", 101),
    (2, "Bob", 102),
    (3, "Charlie", 103),
    (4, "David", None)
]
columns = ["emp_id", "name", "dept"]
df= spark.createDataFrame(emp, columns)

# Departments DataFrame
dept = [
    (101, "HR"),
    (102, "Finance"),
    (104, "Engineering")
]
df2 = ["did", "dept_name"]
df1 = spark.createDataFrame(dept, df2)

#df5=df.join(df1,df.dept==df1.did,'left').show()
#df5=df.join(df1,df.dept==df1.did,'right').show()
#df5=df.join(df1,df.dept==df1.did,'inner').show()
#df5=df.join(df1,df.dept==df1.did,'full').show()
#df5=df.join(df1,df.dept==df1.did,'left_anti').show()
df5=df.join(df1,df.dept==df1.did,'leftsemi').show()



