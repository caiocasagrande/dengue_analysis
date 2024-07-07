# Importação de bibliotecas
import pandas       as pd
import requests

# URLs da API IBGE
url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/"

# Importação dos dados
request         = requests.get(url).json()
flattened_data  = pd.json_normalize(request, sep='_')
municipios      = pd.DataFrame(flattened_data)

# Excluindo colunas desnecessárias
drop_cols = ['regiao-imediata_regiao-intermediaria_id',
    'regiao-imediata_regiao-intermediaria_nome',
    'regiao-imediata_regiao-intermediaria_UF_id',
    'regiao-imediata_regiao-intermediaria_UF_sigla',
    'regiao-imediata_regiao-intermediaria_UF_nome',
    'regiao-imediata_regiao-intermediaria_UF_regiao_id',
    'regiao-imediata_regiao-intermediaria_UF_regiao_sigla',
    'regiao-imediata_regiao-intermediaria_UF_regiao_nome']

municipios.drop(drop_cols, axis=1, inplace=True)

# Renomeando as colunas
columns_dict = {
    'id': 'cod_ibge',
    'nome': 'nome_mun',
    'microrregiao_id': 'id_micro',
    'microrregiao_nome': 'nome_micro',
    'microrregiao_mesorregiao_id': 'id_meso',
    'microrregiao_mesorregiao_nome': 'nome_meso',
    'microrregiao_mesorregiao_UF_id': 'id_UF',
    'microrregiao_mesorregiao_UF_sigla': 'sigla_UF',
    'microrregiao_mesorregiao_UF_nome': 'nome_UF',
    'microrregiao_mesorregiao_UF_regiao_id': 'id_regiao',
    'microrregiao_mesorregiao_UF_regiao_sigla': 'sigla_regiao',
    'microrregiao_mesorregiao_UF_regiao_nome': 'nome_regiao',
    'regiao-imediata_id': 'id_regiao_imediata',
    'regiao-imediata_nome': 'nome_regiao_imediata'
}

# Adicionando coluna id_mun
municipios['id_mun'] = municipios['id'].apply(lambda x: int(str(x)[:-1]))

# Renomeando colunas
municipios.rename(columns=columns_dict, inplace=True)

# Ordenando colunas 
municipios = municipios[['cod_ibge', 'id_mun', 'nome_mun', 'id_micro', 'nome_micro', 
                         'id_meso', 'nome_meso', 'id_UF', 'sigla_UF', 'nome_UF',
                         'id_regiao', 'sigla_regiao', 'nome_regiao', 
                         'id_regiao_imediata', 'nome_regiao_imediata', ]]

# Exportando dados
municipios.to_csv('../../data/interim/municipios.csv', index=False)
