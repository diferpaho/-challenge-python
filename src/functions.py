import requests
import pandas as pd
import hashlib
import time
import sqlite3

# Obtener la información de los países
def get_paises(url):
    r = requests.get(url)
    data = r.json()
    return data

def get_df(data):
    # Creación del data frame
    df=pd.DataFrame(columns = ['Region' , 'City Name', 'Languaje','Time(ms)'])
    for i in data:
        language_SHA1 = hashlib.sha1(i["languages"][0]["nativeName"].encode('utf-8'))
        start_time = time.time()
        df=df.append({'Region': i["region"], 'City Name':i["name"], 'Languaje':str(language_SHA1.hexdigest()),'Time(ms)':(time.time() - start_time)*1000},ignore_index=True)
    return df