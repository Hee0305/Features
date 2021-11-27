from tsfresh import extract_features
import pandas as pd
df = pd.read_csv("./AE.csv")

X = extract_features(df, column_id='id', column_sort='time')
print(X)

E = X.dropna(axis=1)
print(E)

E.to_csv("AE_ts.csv",index=None)


