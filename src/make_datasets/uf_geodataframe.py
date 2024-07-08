# Importação de bibliotecas

# Bibliotecas
import pandas       as pd   
import geopandas    as gpd  
import requests     as req  

# URLs da API IBGE
url = 'https://servicodados.ibge.gov.br/api/v3/malhas/paises/BR?formato=application/vnd.geo+json&qualidade=maxima&intrarregiao=UF'

# Importação dos dados
request = req.get(url).json()

# Criando GeoDataFrame
gdf = gpd.GeoDataFrame.from_features(request)

# Renomeando colunas
gdf.rename(columns={'codarea': 'id_uf'}, inplace=True)

# Reordenando colunas
gdf = gdf[['id_uf', 'geometry']]

# GeoDataFrame
uf_brasil = gpd.GeoDataFrame(gdf, geometry=gdf.geometry)

# Exportação dos dados
uf_brasil.to_file('../../data/interim/uf_brasil.geojson', driver='GeoJSON')