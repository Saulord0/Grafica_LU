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

