import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from functions import *

# Obtener la información de los países
data=get_paises("https://restcountries.com/v2/all")

# Agregamos los países al dataframe 
df=get_df(data)

# Mostrar el dataframe por consola
print(df.to_string(index=False))

# Mostrar los tiempos por consola
print("Tiempo total= "+str("{0:.6f}".format(df['Time(ms)'].sum()))+" ms")
print("Tiempo promedio= "+str("{0:.6f}".format(df['Time(ms)'].mean()))+" ms")
print("Tiempo minimo= "+str("{0:.6f}".format(df['Time(ms)'].min()))+" ms")
print("Tiempo maximo= "+str("{0:.6f}".format(df['Time(ms)'].max()))+" ms")

# Crear la base de datos y la respectiva tabla basandose en el dataframe
export_to_sqlite(df)

# Crear un archivo tipo json basandose en el dataframe
export_to_json(df)

# Mostrar por consola el archivo json creado con la informacion del dataframe
print(pd.read_json('data.json'))