import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from functions import *
import sqlite3
# Obtener la información de los países
data=get_paises("https://restcountries.com/v2/all")

# Agregamos los países al data frame 
df=get_df(data)

# Mostrar el data frame por consola
print(df.to_string(index=False))

# Mostrar los tiempos por consola
print("Tiempo total= "+str("{0:.6f}".format(df['Time(ms)'].sum()))+" ms")
print("Tiempo promedio= "+str("{0:.6f}".format(df['Time(ms)'].mean()))+" ms")
print("Tiempo minimo= "+str("{0:.6f}".format(df['Time(ms)'].min()))+" ms")
print("Tiempo maximo= "+str("{0:.6f}".format(df['Time(ms)'].max()))+" ms")

# Crea una conexión a la base de datos SQLite
con = sqlite3.connect("sqlite.db")
create_sql="CREATE TABLE IF NOT EXISTS countries (id INTEGER,region TEXT,city TEXT,languaje TEXT,time FLOAT)"
cursor=con.cursor()
cursor.execute(create_sql)

for row in df.itertuples():
    insert_sql=f"INSERT INTO countries (id,region,city,languaje,time) VALUES (?, ?, ? ,?,?)" 
    cursor.execute(insert_sql, row)

con.commit()