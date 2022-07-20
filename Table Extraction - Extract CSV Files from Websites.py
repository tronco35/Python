#https://www.youtube.com/watch?v=PXMJ6FS7llk&t=2507s

import pandas as pd 
df_premier21 = pd.read_csv ('https://www.football-data.co.uk/mmz4281/2122/E0.csv')

#renombrar columnas
df_premier21.rename(columns={'FTHG': 'home_goals'}, inplace= True)
 #show dataframe 
print (df_premier21 )