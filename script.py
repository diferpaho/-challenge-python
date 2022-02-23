import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import requests
import hashlib
import pandas as pd
import time


url="https://restcountries.com/v2/all"
r = requests.get(url)
data = r.json()

df=pd.DataFrame(columns = ['Region' , 'City Name', 'Languaje','Time(ms)'])
for i in data:
    language_SHA1 = hashlib.sha1(i["languages"][0]["nativeName"].encode('utf-8'))
    start_time = time.time()
    df=df.append({'Region': i["region"], 'City Name':i["name"], 'Languaje':str(language_SHA1.hexdigest()),'Time(ms)':(time.time() - start_time)*1000},ignore_index=True)

print(df.to_string(index=False))
print("Tiempo total= "+str("{0:.6f}".format(df['Time(ms)'].sum()))+" ms")
print("Tiempo promedio= "+str("{0:.6f}".format(df['Time(ms)'].mean()))+" ms")
print("Tiempo minimo= "+str("{0:.6f}".format(df['Time(ms)'].min()))+" ms")
print("Tiempo maximo= "+str("{0:.6f}".format(df['Time(ms)'].max()))+" ms")