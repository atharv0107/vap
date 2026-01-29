"""import pandas as pd

s=pd.Series([10, 20, 30, 40, 50])
print(s)
"""
from pandas import DataFrame

student=DataFrame (
    {
        "id":[1,2,3,4,5,6],
        "name":["atharv","sumit","rahul","tanmay","aditya"],
        "age": [12,13,12,14,12]
        
    }
)
print(student)

print(student['name'])

print(student.columns)
print[["name","age"]]  #