import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import requests
import hashlib
import pandas as pd
import time

# Obtener la información de los países
url="https://restcountries.com/v2/all"
r = requests.get(url)
data = r.json()

# Creación del data frame
df=pd.DataFrame(columns = ['Region' , 'City Name', 'Languaje','Time(ms)'])

# Agregamos los países al data frame 
for i in data:
    language_SHA1 = hashlib.sha1(i["languages"][0]["nativeName"].encode('utf-8'))
    start_time = time.time()
    df=df.append({'Region': i["region"], 'City Name':i["name"], 'Languaje':str(language_SHA1.hexdigest()),'Time(ms)':(time.time() - start_time)*1000},ignore_index=True)

# Mostrar el data frame por consola
print(df.to_string(index=False))

# Mostrar los tiempos por consola
print("Tiempo total= "+str("{0:.6f}".format(df['Time(ms)'].sum()))+" ms")
print("Tiempo promedio= "+str("{0:.6f}".format(df['Time(ms)'].mean()))+" ms")
print("Tiempo minimo= "+str("{0:.6f}".format(df['Time(ms)'].min()))+" ms")
print("Tiempo maximo= "+str("{0:.6f}".format(df['Time(ms)'].max()))+" ms")