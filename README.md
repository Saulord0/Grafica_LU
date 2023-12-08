# Funciones_LU
funciones creadas para la manipulacion de datos shapefile y netCDF4 con el fin de facilitar el graficado de la variable
de uso de suelo (LU_INDEX)
##########################################################
#limites_shape(ZMVM,entidades,XLONG_geo,XLAT_geo)
##########################################################
- Toma los archivos shapefile y los convierte en listas para que puedan ser graficadas
- Toma las coordenadas XLONG y XLAT de grogrid y con los límites del shapefile de la Zona Metropolitana
  del Valle de México (dominio interno) calcula los indices del netcdf donde se encuentran de las coordenadas más cercanas

===========   Entradas   ===========
ZMVM         |    shapefile del dominio interno
entidades    |    shapefile de las entidades que componen el dominio interno
XLONG_geo    |    arreglo de dos dimensiones con las coordenadas XLONG
XLAT_geo     |    arreglo de dos dimensiones con las coordenadas XLAT
===========   Salidas   ===========
indlong_ini  |    indice de la longitud mínima
indlong_fin  |    indice de la longitud maxima
indlat_ini   |    indice de la latitud mínima
indlat_fin   |    indice de la longitud maxima
coord_ZMVM   |    lista con las coordenadas límite del shapefile de ZMVM
xx           |    lista de coordenadas X del shapefile de ZMVM
xy           |    lista de coordenadas Y del shapefile de ZMVM
xx2          |    lista de coordenadas X del shapefile de entidades
xy2          |    lista de coordenadas y del shapefile de entidades

##########################################################
#Clases(numclases)
##########################################################
- Define las clases de USGS a utilizar
-   si el número de clases es menor o igual a 24, se toman las clases 'normales' de USGS
-   si el numero de clases es mayor a 24 y menor o igual a 61, se toman las clases de USGS más la de LCZ v1
-   en otro caso (si el numero de clases es mayor a 61, se toman las clases de USGS más la de LCZ v2


===========   Entradas   ===========
numclases    |    número entero con el número de clases de uso de suelo

===========    Salidas   ===========
datos_usgs   |    diccionario con el valor numérico de la clase de suelo como llave y como valores una lista con el nombre de la clase y una tupla con el color en RGB

##########################################################
#leyenda(datos_usgs,LU_geo)
##########################################################
- Define la nueva paleta de colores y la leyenda de acuerdo con las las clases de USGS del dominio


===========   Entradas   ===========
datos_usgs   |  diccionario con el valor numérico de la clase de suelo como llave y como valores una lista con el nombre de la clase y una tupla con el color en RGB
LU_geo       |  arreglo de dos dimensiones con datos de uso de suelo

===========    Salidas   ===========
leyenda      |    lista con las tuplas de los colores de las clases que aparecen en LU_geo
barra        |    lista con los valores RGB normalizados (/255)
newcmp       |    colormap con los colores de barra lista para usar en colorbar()


##########################################################
#corrige_valores(LU_geo)
##########################################################
- Modifica los valores del arrelgo LU_geo para que coincidan con la nueva barra de colores
    Esto es: Si las clases de suelo en el dominio son: [1,2,3,4,8,9,15,16,18,22]
    la barra de colores tendrá saltos en la leyenda y los colores no corresponderán a las etiquetas. 
    Entonces el programa cambia las clases de la forma: 
          [1,2,3,4,8,9,15,16,18,22]
    a la forma
          [1,2,3,4,5,6,7,8,9,10]
    para que tanto las etiquetas y los colores de la barra concuerden a lo establecido en la paleta de colores

===========   Entradas   ===========
LU_geo       |  arreglo de dos dimensiones con datos de uso de suelo

===========    Salidas   ===========
LU_geo       |  arreglo de dos dimensiones modificado para que las clases de suelo sean consecutivas y coincidentes con la barra de colores


##########################################################
#coordenadas_USyV(LU_geo,coordenadas,USyV,XLAT_geo=0,XLONG_geo=0)
##########################################################



