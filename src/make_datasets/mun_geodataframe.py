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
gdf.rename(columns={'codarea': 'cod_ibge'}, inplace=True)

# Tratamento de dados
cols = ['cod_ibge', 'id_mun']

for col in cols:
    gdf[col] = gdf[col].astype('int64')

# ----- Merge - Amazonia Legal

# Municipios Amazônia Legal
df_amazonia_legal = pd.read_csv('../../data/interim/mun_amazonia_legal.csv')[['cod_ibge', 'nome_mun', 'id_uf']]

# Merge
amazonia_legal = df_amazonia_legal.merge(gdf, on='cod_ibge', how='left')

# Reordenando colunas
amazonia_legal = amazonia_legal[['cod_ibge', 'id_mun', 'nome_mun', 'id_uf', 'geometry']]

# DataFrame to GeoDataFrame
amazonia_legal = gpd.GeoDataFrame(amazonia_legal, geometry=amazonia_legal.geometry)

# Exportação dos dados
amazonia_legal.to_file('../../data/interim/amazonia_legal.geojson', driver='GeoJSON')