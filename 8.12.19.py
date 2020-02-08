import numpy as np
import pandas as pd
s=np.array([[1,2],[3,4],[0,-1]])
s.sort(axis=0)
print(s)

s=pd.read_csv('F:\\50_Startups.csv')
print(s.shape)
print(type(s))
print(s.columns)
print(s.index)
print(s[0:50:2])
print("*****************************************************")
s[['Administration','Profit']]
print(s[5:11])
print(s.iloc[5:11,1:5:2])
