import json
import pandas as pd
import numpy as np

def preProcesado (DF):
    # Funcion que prepara los generos en un DF para ser codificadas en la matriz
    # Devuelve tambien los generos en una lista
    generosDF = DF['genres']. apply (pd.Series)
    generosDF ['title'] = DF['title']
    generosDF = generosDF . drop_duplicates ([ 'title'])
    generosDF . set_index ('title', inplace = True )
    genres = [ generosDF [ genre ]. unique () for genre in generosDF . columns ]
    genres = [ genre for lista in genres for genre in lista if all ([ pd. isnull (
    genre ) == False , genre != ' ', genre != '', len (str ( genre )) > 1]) ]
    genres = list ( set( genres ))
    return generosDF , genres

def codificaMatriz (DF , genres : list , producto : list ):
    
    matriz = pd.DataFrame(
        np.zeros((len(genres), len(producto))),
        index=genres,
        columns=list(producto)
    )
    
    for pelicula in DF.index:
        for index in DF:
            genero = DF[index][pelicula]
            if genero in genres:
                matriz[pelicula][genero] = 1

    return matriz# Debe retornar un DF como el de la Tabla 1.

def recomiendaPeliculas (url_puntuacion:str,url_perfil:str , url_recomendacion : str)->json:
    
    puntuacionPelicula = pd.read_csv(url_puntuacion, sep=';', names=['pelicula', 'puntuacion'], index_col=['pelicula'])

    dataPerfil = pd.read_json(url_perfil)
    dataPerfil, generosPuntuacion = preProcesado(dataPerfil)

    peliculasPuntuacion = dataPerfil.index

    mGeneros = codificaMatriz(dataPerfil, generosPuntuacion, peliculasPuntuacion)

    for pelicula in mGeneros.columns:
        if pelicula in puntuacionPelicula.index:
            mGeneros[pelicula] = mGeneros[pelicula].apply(lambda punto: float(punto * puntuacionPelicula['puntuacion'][pelicula]))
    
    mGeneros['perfilUsuario'] = [mGeneros.loc[genero,:].sum() for genero in mGeneros.index]
    mGeneros['perfilUsuario'] = mGeneros['perfilUsuario'].apply(lambda punto: punto / mGeneros['perfilUsuario'].sum())
    
    # Codigo para la matriz candidata

    return json.dumps(solucionDict, indent=4)

    

recomiendaPeliculas('https://git.io/JZKcF','https://git.io/JZKZV','https://git.io/JZKWX')