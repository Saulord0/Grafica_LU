#limites_shape(ZMVM,entidades,XLONG_geo,XLAT_geo)
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


# Grafica_LU
Grafica datos de Uso de suelo guardados en un netcdf. En caso que en el dominio no se encuentren las clases consecutivas
modifica los valores para que la gráfica de colores corresponda a lo mostrado.

Esto es: Si las clases de suelo en el dominio son: [1,2,3,4,8,9,15,16,18,22]
la barra de colores tendrá saltos en la leyenda y los colores no corresponderán a las etiquetas. 
Entonces el programa cambia las clases de la forma: 
    [1,2,3,4,8,9,15,16,18,22]
a la forma
    [1,2,3,4,5,6,7,8,9,10]
para que tanto las etiquetas y los colores de la barra concuerden a lo establecido en la paleta de colores

