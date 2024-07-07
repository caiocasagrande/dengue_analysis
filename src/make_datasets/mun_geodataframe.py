# Importação de bibliotecas

# Bibliotecas
import pandas       as pd   
import geopandas    as gpd  
import requests     as req  

# URLs da API IBGE
url = 'https://servicodados.ibge.gov.br/api/v3/malhas/paises/BR?formato=application/vnd.geo+json&qualidade=maxima&intrarregiao=municipio'

# Importação dos dados
request = req.get(url).json()

# Criando GeoDataFrame
gdf = gpd.GeoDataFrame.from_features(request)

# Renomeando colunas
gdf['id_mun'] = gdf['codarea'].apply(lambda x: int(str(x)[:-1]))
gdf = gdf[['codarea', 'id_mun', 'geometry']]

# Tratamento de dados
gdf['id_mun'] = gdf['id_mun'].astype(int)

# ----- Merge - Amazonia Legal

# Municipios Amazônia Legal
df_amazonia_legal = pd.read_csv('../../data/interim/mun_amazonia_legal.csv')

# Merge
amazonia_legal = df_amazonia_legal[['id_mun', 'nome_mun', 'sigla_uf']].merge(gdf[['id_mun', 'geometry']], on='id_mun', how='left')

# DataFrame to GeoDataFrame
amazonia_legal = gpd.GeoDataFrame(amazonia_legal, geometry=amazonia_legal.geometry)

# Exportação dos dados
amazonia_legal.to_file('../../data/interim/amazonia_legal.geojson', driver='GeoJSON')