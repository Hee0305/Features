import pandas as pd
import numpy as np
E = pd.read_csv("./train_input/train_input_스핀들전력.csv")
V = pd.read_csv("./train_input/train_input_스핀들진동.csv")
A = pd.read_csv("./train_input/train_input_전체전력.csv")


Id,time,data=[],[],[]

for i in range(0,410):
    for j in range(0,60):
        Id.append(i)
        time.append(j)
        data.append(V.iloc[i,j])

df1 = pd.DataFrame({'id':Id,'time':time,'data':data})
print(df1)
            
df1.to_csv("V_features.csv",index=None)




