#https://www.youtube.com/watch?v=PXMJ6FS7llk&t=2507s
import pandas as pd 

##retornar tablas de ua pagima web 
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')

len(simpsons)
23 # numero de tablas del destino 

print (simpsons [3]) #numero de tabla que quiero retornar 
