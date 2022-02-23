# Challenge-python

## Challenge

|  Region | City Name |  Languaje | Time  |
|---|---|---|---|
|  Africa | Angola  |  AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724 | 0.23 ms  |
|   |   |   |   |
|   |   |   |   |

Desarrolle una aplicacion en python que genere la tabla anterior teniendo las siguientes consideraciones:

- De https://restcountries.com/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
- En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
- La tabla debe ser creada en un DataFrame con la libreria PANDAS
- Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
- Guarde el resultado en sqlite.
- Genere un Json de la tabla creada y guardelo como data.json
- La prueba debe ser entregada en un repositorio git.

Es un plus si:

- No usa famework
- Entrega Test Unitarios
- Presenta un diseño de su solucion.

## Proyecto fue creado usando las siguientes tecnologias:

- Python 3.8.10
- SO: Ubuntu 20.04 LTS

## Ejecutar proyecto

Para ejecutar el codigo puede usar el siguiente comando
```
python3 src/main.py
```

## Base de datos en sqlite

La base de datos queda guardada con el nombre:
```
sqlite.db
```
## Archivo json
El archivo json con la informacion queda guardado con el nombre:
```
sqlite.db
```
## Ejecutar pruebas

Para ejecutar las pruebas puede usar el siguiente comando:
```
python test.py
```

## Diseño de la solucion

El diseño de la solucion es un diagrama de secuencia que podra encontrar en la ruta
```
diseño/diagrama.png
```

