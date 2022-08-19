import pandas as pd
#csvファイルを読み込む
df =pd.read_csv("C:\\Users\\B20735\\Desktop\\相関係数.csv")
#print(df)
# print(df.head(3))

# df.tail(10)
#print(df.columns)
#print(df.dtypes)
#print(df.shape)
#print(df1 = df.sort_values('viewcount')) #昇順
# dfNo = df.sort_values('viewCount')
#df1 = df.sort_values('viewCount',ascending=False)
# print(df1.head(10))
# dfNo1 = dfNo.head(10)

#print(df.sort_values('viewcount', ascending=False)) #降順
# dfNo2 = df.sort_values('viewCount', ascending=False)
# dfNo3 =dfNo2.head(10)
# df.isnull()
# df.fillna(0).head()
#print(df.isnull().sum())
#print(df.groupby('').mean())
#print(df.mean()) #各カラムの平均値
# print(df.median())#中央値
# print(df.std()) #標準偏差
# df.max()#
# df.min()#
print(df.describe().round(1))  #総合的な数値データ

#図表化 折れ線グラフ
import matplotlib.pyplot as plt
#plt.show(df[:50].plot(x='publishedAt',y=['likecount','viewcount']))  #図表化 折れ線グラフ
#相関関係係数
print(df[['viewcount','likecount','commentcount','time','sence','s/m']].corr()) #相関関係係数

#データの出力
# df.sort_values().to_csv('出力NO3.csv',index = False)
# dfNo1.to_csv('NO10tail10.csv',index=False)
# dfNo3.to_csv('NO10head10.csv',index=False)



