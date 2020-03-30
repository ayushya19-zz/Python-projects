import pandas as pd

ufo=pd.read_csv('http://bit.ly/uforeports')
print(type(ufo))
print(ufo.head())
print(ufo.City)