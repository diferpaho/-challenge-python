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
    # Creación del dataframe
    df=pd.DataFrame(columns = ['Region' , 'City Name', 'Languaje','Time(ms)'])
    # Llenar dataframe con los datos obtenidos anteriormente
    for i in data:
        language_SHA1 = hashlib.sha1(i["languages"][0]["nativeName"].encode('utf-8'))
        start_time = time.time()
        df=df.append({'Region': i["region"], 'City Name':i["name"], 'Languaje':str(language_SHA1.hexdigest()),'Time(ms)':(time.time() - start_time)*1000},ignore_index=True)
    return df

def export_to_sqlite(df):
    try:
        # Crear una conexión a la base de datos SQLite
        con = sqlite3.connect("sqlite.db")
        # Crear la tabla donde se guardara la informacion
        create_sql="CREATE TABLE IF NOT EXISTS countries (id INTEGER,region TEXT,city TEXT,languaje TEXT,time FLOAT)"
        cursor=con.cursor()
        cursor.execute(create_sql)
        # Agregar informacion a la tabla en la base de datos
        for row in df.itertuples():
            insert_sql=f"INSERT INTO countries (id,region,city,languaje,time) VALUES (?, ?, ? ,?,?)" 
            cursor.execute(insert_sql, row)
        con.commit()
        return True
    except:
        return False

    

def export_to_json(df):
    try:
        # crear archivo json con la informacion del dataframe
        df.to_json(r'data.json')
        return True
    except:
        return False