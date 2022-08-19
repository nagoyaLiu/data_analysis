import pandas as pd
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],
                   columns=['col01','col02','col03'],
                   index=['idx01','idx02','idx03'])
print(df)
print(df.columns)