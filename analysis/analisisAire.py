import pandas as pd
from data.generators.generadorAire import generarDatosCalidadAire
from helpers.crearTablaHTML import crearTabla

def construirAireDataFrame():
    datosAire=generarDatosCalidadAire()

    #generamos el dataframe
    aireDataFrame=pd.DataFrame(datosAire,columns=['nombre','comuna','ica','fecha','correo'])

    #crearTabla(aireDataFrame,"datosaire")
    #Limpiando el dataframe
    #reemplazando valores 
    aireDataFrame.replace('sin',pd.NA,inplace=True)
    #elimino los registros que no cumplen el criterio
    aireDataFrame.dropna(inplace=True)
    
    #filtrar DATOS
    #Filtrar es aplicar condiciones logicas
    #que permitan analizar la informacion del DF
    filtroCalidadAireBueno=aireDataFrame.query("(ica>=10)and(ica<40)").value_counts()
    filtroCalidadAireAceptable=aireDataFrame.query("(ica>=40)and(ica<50)").value_counts()
    filtroCalidadAireMalo=aireDataFrame.query("(ica>=50)and(ica<100)").value_counts()

    print(filtroCalidadAireBueno)
    print("\n")
    print(filtroCalidadAireAceptable)
    print("\n")
    print(filtroCalidadAireMalo)

construirAireDataFrame()