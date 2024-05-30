import pandas as pd
from data.generators.generadorAire import generarDatosCalidadAire
from helpers.crearTablaHTML import crearTabla

def construirAireDataFrame():
    datosAire=generarDatosCalidadAire()

    #generamos el dataframe
    aireDataFrame=pd.DataFrame(datosAire,columns=['nombre','comuna','ica','fecha','correo'])

    crearTabla(aireDataFrame,"datosaire")
    print(aireDataFrame)

construirAireDataFrame()