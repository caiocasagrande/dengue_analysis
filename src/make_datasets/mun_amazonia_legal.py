# Importação de bibliotecas

# Bibliotecas
import pandas as pd

# Importação dos dados
data = pd.read_excel('../../data/raw/Municipios_da_Amazonia_Legal_2022.xlsx')

# Tratamento de dados

# Excluindo colunas desnecessárias
data.drop(columns=['SEDES_FORA_AMAZÔNIA', 'NM_UF'], inplace=True)

# Renomeando colunas
columns_dict = {
    'CD_MUN': 'cod_ibge',
    'NM_REGIAO': 'sigla_regiao',
    'CD_UF': 'id_uf',
    'SIGLA_UF': 'sigla_uf',
    'NM_MUN': 'nome_mun',
    'AREA_TOTAL': 'area_total',
    'AREA_INTEGRADA NA AMAZÔNIA': 'area_amazonia',
    'PORCENTAGEM_AMAZÔNIA': 'pctg_amazonia'}

data.rename(columns=columns_dict, inplace=True)

# Criando coluna de identificação dos municiípios
data['id_mun'] = data['cod_ibge'].apply(lambda x: int(str(x)[:-1]))

# Renomeando as regioes
regiao_dict = {
    'Norte': 'N',
    'Nordeste': 'NE',
    'Centro-oeste': 'CO'}

data['sigla_regiao'] = data['sigla_regiao'].map(regiao_dict)

# Reordenando colunas
data = data[['cod_ibge', 'id_mun', 'nome_mun', 'sigla_uf', 'id_uf', 'sigla_regiao', 
             'area_total', 'area_amazonia', 'pctg_amazonia']]

# Exportação dos dados
data.to_csv('../../data/interim/mun_amazonia_legal.csv', index=False)