import difflib as diff
import pandas as pd
import os

path = os.getcwd()

print('読み込みたいcsvファイルを書いてください')
print('↓'*10)
a = input()

df1 = pd.read_csv(a)

print('読み込みたいcsvファイルを書いてください')
print('↓'*10)
b = input()

df2 = pd.read_csv(b)

df_diff = df1[~df1['word'].isin(df2['word'])]



print('新しいcsvのファイル名を書いてください')
c = input()

df_diff.to_csv(c)



