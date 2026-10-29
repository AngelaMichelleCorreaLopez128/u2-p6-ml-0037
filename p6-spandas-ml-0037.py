import pandas as pd
import numpy as np
# Angela Correa NC = 0037

serie_amigos=["Angela","Jade","Catherine","Pedro","Morgan","Adrian","Maria"]
print(" --- Serie listado de amigos --- NC = 0037")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print(" --- Serie listado valor de billetes MX --- NC = 0037")
amigos=pd.Series(serie_billetes)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
serie_bletras=["veinte","cincuenta","cien","doscientos","quinientos","mil"]
print(" --- Serie listado nombre y valor de billetes MX --- NC = 0037")
tablabilletes=pd.Series(serie_billetes,serie_bletras)
print(tablabilletes)
# Diccionario dataframe
# Diccionario de valor monedas y nombre
print("--- datos de diccionario a DataFrame en pandas --- NC = 0037")
dic_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras":["veinte","cincuenta","cien","doscientos","quinientos","mil"],
}

tablabilletes= pd.DataFrame(dic_monedas,index= ["A","B","C","D","E","F"])
print(tablabilletes)

print("Casa de cambio de Angela Correa NC = 0037 ")