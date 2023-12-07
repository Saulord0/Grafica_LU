import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
#from matplotlib import ListedColormap
import matplotlib as mpl
import geopandas as gpd

'''
#retorna los indices del netcdf donde se delimita la ZMVM con sus estados(entidades)
'''
def limites_shape(ZMVM,entidades,XLONG_geo,XLAT_geo):
    #transformacion de coordenadas geopandas a lista
    xx=[]
    xy=[]
    for t in range(len(ZMVM.boundary.geometry.values)):
        ff=ZMVM.boundary.geometry.values[t]
        ff2=ff.xy
        xx.append(ff2[0])
        xy.append(ff2[1])
    xx2=[]
    xy2=[]
    for t in range(len(entidades.boundary.geometry.values)):
        ff=entidades.boundary.geometry.values[t]
        ff2=ff.xy
        xx2.append(ff2[0])
        xy2.append(ff2[1])
    # limites para la ZMVM
    coord_ZMVM=[min(min(xx))-0.5, max(max(xx))+0.5, min(min(xy))-0.5, max(max(xy))+0.5]
    dif_lat=list(abs(XLAT_geo[:,0]-coord_ZMVM[2]))
    lat=np.where(dif_lat==min(dif_lat))
    indlat_ini=list(lat[0])[0]          #indice de latitud donde se hace el corte
    dif_lat=list(abs(XLAT_geo[:,0]-coord_ZMVM[3]))
    lat=np.where(dif_lat==min(dif_lat))
    indlat_fin=list(lat[0])[0]          #indice de latitud donde se hace el corte
    dif_long=list(abs(XLONG_geo[0,:]-coord_ZMVM[0]))
    long=np.where(dif_long==min(dif_long))
    indlong_ini=list(long[0])[0]          #indice de latitud donde se hace el corte
    dif_long=list(abs(XLONG_geo[0,:]-coord_ZMVM[1]))
    long=np.where(dif_long==min(dif_long))
    indlong_fin=list(long[0])[0]          #indice de latitud donde se hace el corte

    return indlong_ini,indlong_fin,indlat_ini,indlat_fin,coord_ZMVM,xx,xy,xx2,xy2

'''
#paleta de colores con todas las clases de USGS o USGS+LCZ
'''
def Clases(numclases):
    if numclases<=24:
        datos_usgs={1:["Urbano",(220,20,20)],
                    2:["Cultivo de temporal",(70,40,5)],
                    3:["Cultivo de riego",(180,140,50)],
                    4:["Mosaico de cultivo y pastizal",(180,107,45)],
                    5:["Cultivos y pasturas de riego",(196,130,74)],
                    6:["Mosaico de cultivo con bosque poco denso",(122,80,69)],
                    7:["Pastizal",(255,180,50)],
                    8:["Matorral",(245,22,180)],
                    9:["Matorral y pastizal",(210,180,150)],
                    10:["Sabana",(230,200,150)],
                    11:["Bosque caducifolio de hoja ancha",(160,250,160)],
                    12:["Bosque caducifolio de hoja de aguja",(154,205,48)],
                    13:["Bosque perenne de hoja ancha",(60,200,40)],
                    14:["Bosque perenne de hoja de aguja",(33,140,33)],
                    15:["Bosque mixto",(0,60,0)],
                    16:["Cuerpos de agua",(0,70,200)],
                    17:["Pantano herbaceo",(120,181,181)],
                    18:["Pantano boscoso",(120,220,240)],
                    19:["Sin vegetacion aparente",(165,165,165)],
                    20:["Tundra herbacea",(140,148,125)],
                    21:["Tundra boscosa",(78,115,75)],
                    22:["Tundra mixta",(140,190,125)],
                    23:["Tundra con suelo desnudo",(140,206,67)],
                    24:["Nieve",(255,255,255)]}
    elif numclases>24 and numclases<=61:
        datos_usgs={1:["Urbano",(220,20,20)],
                    2:["Cultivo de temporal",(70,40,5)],
                    3:["Cultivo de riego",(180,140,50)],
                    4:["Mosaico de cultivo y pastizal",(180,107,45)],
                    5:["Cultivos y pasturas de riego",(196,130,74)],
                    6:["Mosaico de cultivo con bosque poco denso",(122,80,69)],
                    7:["Pastizal",(255,180,50)],
                    8:["Matorral",(245,22,180)],
                    9:["Matorral y pastizal",(210,180,150)],
                    10:["Sabana",(230,200,150)],
                    11:["Bosque caducifolio de hoja ancha",(160,250,160)],
                    12:["Bosque caducifolio de hoja de aguja",(154,205,48)],
                    13:["Bosque perenne de hoja ancha",(60,200,40)],
                    14:["Bosque perenne de hoja de aguja",(33,140,33)],
                    15:["Bosque mixto",(0,60,0)],
                    16:["Cuerpos de agua",(0,70,200)],
                    17:["Pantano herbaceo",(120,181,181)],
                    18:["Pantano boscoso",(120,220,240)],
                    19:["Sin vegetacion aparente",(165,165,165)],
                    20:["Tundra herbacea",(140,148,125)],
                    21:["Tundra boscosa",(78,115,75)],
                    22:["Tundra mixta",(140,190,125)],
                    23:["Tundra con suelo desnudo",(140,206,67)],
                    24:["Nieve",(255,255,255)],
                    51:["Compact High-Rise",(140,0,0)],
                    52:["Compact Mid-Rise",(209,0,0)],
                    53:["Compact Low-Rise",(255,0,0)],
                    54:["Open High-Rise",(191,77,0)],
                    55:["Open Mid-Rise",(255,102,0)],
                    56:["Open Low-Rise",(255,153,85)],
                    57:["Lightweight low-rise",(250,238,5)],
                    58:["Large low-rise",(188,188,188)],
                    59:["Sparsely built",(255,204,170)],
                    60:["Heavy industry",(85,85,85)]}
    else:
        datos_usgs={1:["Urbano",(220,20,20)],
                    2:["Cultivo de temporal",(70,40,5)],
                    3:["Cultivo de riego",(180,140,50)],
                    4:["Mosaico de cultivo y pastizal",(180,107,45)],
                    5:["Cultivos y pasturas de riego",(196,130,74)],
                    6:["Mosaico de cultivo con bosque poco denso",(122,80,69)],
                    7:["Pastizal",(255,180,50)],
                    8:["Matorral",(245,22,180)],
                    9:["Matorral y pastizal",(210,180,150)],
                    10:["Sabana",(230,200,150)],
                    11:["Bosque caducifolio de hoja ancha",(160,250,160)],
                    12:["Bosque caducifolio de hoja de aguja",(154,205,48)],
                    13:["Bosque perenne de hoja ancha",(60,200,40)],
                    14:["Bosque perenne de hoja de aguja",(33,140,33)],
                    15:["Bosque mixto",(0,60,0)],
                    16:["Cuerpos de agua",(0,70,200)],
                    17:["Pantano herbaceo",(120,181,181)],
                    18:["Pantano boscoso",(120,220,240)],
                    19:["Sin vegetacion aparente",(165,165,165)],
                    20:["Tundra herbacea",(140,148,125)],
                    21:["Tundra boscosa",(78,115,75)],
                    22:["Tundra mixta",(140,190,125)],
                    23:["Tundra con suelo desnudo",(140,206,67)],
                    24:["Nieve",(255,255,255)],
                    61:["Compact High-Rise",(140,0,0)],
                    62:["Compact Mid-Rise",(209,0,0)],
                    63:["Compact Low-Rise",(255,0,0)],
                    64:["Open High-Rise",(191,77,0)],
                    65:["Open Mid-Rise",(255,102,0)],
                    66:["Open Low-Rise",(255,153,85)],
                    67:["Lightweight low-rise",(250,238,5)],
                    68:["Large low-rise",(188,188,188)],
                    69:["Sparsely built",(255,204,170)],
                    70:["Heavy industry",(85,85,85)]}
    return datos_usgs

'''
Devuelve la nueva paleta de colores con su leyenda
'''
def leyenda(datos_usgs,LU_geo):
    leyenda=[]
    barra_lulc=[]
    x=np.unique(LU_geo)
    for clase in x:
        leyenda.append(datos_usgs[int(clase)][0])
        barra_lulc.append(datos_usgs[int(clase)][1])

    barra=np.zeros((len(barra_lulc),4))
    cont=0
    for r in barra_lulc:
        for valor in range(len(r)):
            if valor<len(r):
                barra[cont,valor]=r[valor]/255
        cont+=1
    barra[:,-1]=1

    #crea nueva paleta de colores
    #se toma un colormap establecido
    viridis=mpl.colormaps.get_cmap('viridis')
    #se define un arreglo con los colores del color map establecido
    inter=len(leyenda)*10
    newcolors=viridis(np.linspace(0,1,inter))
    #se define el color que se quiere modificar
    cont=0
    contB=0
    for r in newcolors:
        for valor in range(len(r)):
            if cont<=240 and contB<len(barra):
                newcolors[cont:cont+10,valor]=barra[contB,valor]
        cont+=10
        contB+=1
    newcmp=ListedColormap(newcolors)

    return leyenda,barra,newcmp
'''
Modifica los valores de LU para que coincidan con la nueva barra de colores
'''
def corrige_valores(LU_geo):
    x=np.unique(LU_geo)
    #ajuste de los valores unicos de LU
    cont=1
    dddg=[] #lista con los valores corregidos
    dff=[] #lista con lo que se tiene que restar para corregir
    for t in x:
        print('valor t:{},valor cont:{}'.format(t,cont))
        if(t!=cont):
            dif=t-cont
            dff.append(dif)
            print('valor t corregido:{},valor cont:{}'.format(t-dif,cont))
            dddg.append(t-dif)
        else:
            dddg.append(t)
            dif=0
            dff.append(dif)
        cont+=1
        indif=np.where(np.array(dff)>0)
    indigu=np.where(np.array(dff)==0)

    #ajuste de los valores de LU para que coincidan con los valores en la barra de colores
    cont=0
    for i in dff:
        if(i>0):
            indif=np.where(LU_geo[:]==x[cont])
            LU_geo[indif]=LU_geo[indif]-i
            cont+=1
        else:
            cont+=1
    return LU_geo

'''
devuelve los indices donde se cumple que hay determinado tipo de suelo
'''
def coordenadas_USyV(LU_geo,coordenadas,USyV,XLAT_geo=0,XLONG_geo=0):
    if coordenadas:
        #indlon=[]
        #indlat=[]
        clases={}
        #encuentra indices a cada uno de los puntos
        for clase in USyV.keys():
            lon=USyV[clase][0]
            lat=USyV[clase][1]
            dif=abs(XLAT_geo[:,0]-lat)
            #indlat.append(np.where(dif==min(dif)))
            indlat=list(np.where(dif==min(dif)))
            dif=abs(XLONG_geo[0,:]-lon)
            #indlon.append(np.where(dif==min(dif)))
            indlon=list(np.where(dif==min(dif)))
            clases[clase]=[indlon[0][0],indlat[0][0]]
        return clases
    else:
        USyV7={}
        x=np.unique(LU_geo)
        for clase in x:
            USyV7[int(clase)]=list(np.where(LU_geo==clase))
        return USyV7
'''
input:
long_d2: arreglo de longitudes del dominio2
lat_d2: arreglo de latitudes del dominio2
var_d2: arreglo de la variable del dominio2 que se quiere recortar
long_d3: arreglo de longitudes del dominio3
lat_d3: arreglo de latitudes del dominio3

devuelde la variable del dominio 2 recortada al dominio 3

'''
def limites_netcdf(long_d2,lat_d2,var_d2,long_d3,lat_d3):
    #coord_d2=[min(min(long_d2)),min(min(lat_d2)),max(max(long_d2)),max(max(lat_d2))]
    coord_d3=[long_d3.min(),lat_d3.min(),long_d3.max(),lat_d3.max()]
    
    dif_lat=list(abs(lat_d2[:,0]-coord_d3[1]))
    lat=np.where(dif_lat==min(dif_lat))
    indlat_ini=list(lat[0])[0]        #indice de latitud donde se hace el corte
    dif_lat=list(abs(lat_d2[:,0]-coord_d3[3]))
    lat=np.where(dif_lat==min(dif_lat))
    indlat_fin=list(lat[0])[0]          #indice de latitud donde se hace el corte
    dif_long=list(abs(long_d2[0,:]-coord_d3[0]))
    long=np.where(dif_long==min(dif_long))
    indlong_ini=list(long[0])[0]          #indice de latitud donde se hace el corte
    dif_long=list(abs(long_d2[0,:]-coord_d3[2]))
    long=np.where(dif_long==min(dif_long))
    indlong_fin=list(long[0])[0]
    if len(var_d2.shape)==3:
        var_d2=var_d2[:,indlat_ini:indlat_fin,indlong_ini:indlong_fin]
    else:
        var_d2=var_d2[indlat_ini:indlat_fin,indlong_ini:indlong_fin]
    
    return var_d2
