import pandas as pd

df1 = pd.read_csv("V_ts.csv")
df2 = pd.read_csv("A_ts.csv")
df3 = pd.read_csv("E_ts_1.csv")
df4 = pd.read_csv("Tlqkf.csv")

#dd = pd.concat([df1,df2,df3],axis=1)
#print(dd)
#dd.to_csv("asdf.csv",index=None)


# =====================================================================================================
# E
# from sklearn.feature_selection import SelectKBest, f_classif

# X = df3
# y2 = pd.read_csv('train_output.csv')
# y = y2.iloc[:,1] # 0 = tool / 1 = condition


# selectK = SelectKBest(score_func=f_classif, k=50)

# X1 = selectK.fit_transform(X, y)
# condition_feature_E = pd.DataFrame(X1)
# print(condition_feature_E)

# condition_feature_E.to_csv("E_20.csv",index=None)

# =====================================================================================================
#  A
# from sklearn.feature_selection import SelectKBest, f_classif

# X = df2
# y2 = pd.read_csv('train_output.csv')
# y = y2.iloc[:,1] # 0 = tool / 1 = condition


# selectK = SelectKBest(score_func=f_classif, k=50)

# X1 = selectK.fit_transform(X, y)
# condition_feature_A = pd.DataFrame(X1)
# print(condition_feature_A)

# condition_feature_A.to_csv("A_20.csv",index=None)


# =====================================================================================================
# V  
from sklearn.feature_selection import SelectKBest, f_classif

X = df1
print(X)
y2 = pd.read_csv('train_output.csv')
y = y2.iloc[:,1] # 0 = tool / 1 = condition


selectK = SelectKBest(score_func=f_classif, k=50) # best : 50 

X1 = selectK.fit_transform(X, y)
condition_feature_V = pd.DataFrame(X1)
print(condition_feature_V)

condition_feature_V.to_csv("V_50.csv",index=None)
# =====================================================================================================
# from sklearn.feature_selection import SelectKBest, f_classif

# X = df4
# y2 = pd.read_csv('train_output.csv')
# y = y2.iloc[:,1] # 0 = tool / 1 = condition


# selectK = SelectKBest(score_func=f_classif, k=20) # best : 50 

# X1 = selectK.fit_transform(X, y)
# condition_feature_all = pd.DataFrame(X1)
# print(condition_feature_all)

# condition_feature_all.to_csv("Tlqkfplz.csv",index=None)
