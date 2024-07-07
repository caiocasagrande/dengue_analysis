# Importação de bibliotecas
import pandas as pd
import requests

# URLs da API IBGE
url_estimativa_populacao = "https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/{}/variaveis/9324?localidades=N6[all]"
url_censo = "https://servicodados.ibge.gov.br/api/v3/agregados/9605/periodos/{}/variaveis/93?localidades=N6[all]"

# Listas de apoio
dfs_1   = []
dfs_2   = []
censos  = [2010, 2022]

##### Dados de Estimativa de População IBGE

# Iteração entre os anos, exceto 2007 e 2010
for year in range(2001, 2022):
    if year != 2007 and year != 2010:
        url_1 = url_estimativa_populacao.format(year)
        data = requests.get(url_1).json()

        # População
        rows = []
        for item in data:
            for result in item['resultados']:
                for series in result['series']:
                    row = {
                        'id': series['localidade']['id'],
                        'nome_municipio': series['localidade']['nome'],
                        str(year): series['serie'][str(year)]
                    }
                    rows.append(row)

        # DataFrame
        df_year = pd.DataFrame(rows)
        dfs_1.append(df_year)

# Mesclando os DataFrames de cada ano em um único DataFrame
df_estimativa_populacao = dfs_1[0]
for df_year in dfs_1[1:]:
    df_estimativa_populacao = pd.merge(df_estimativa_populacao, df_year, on=['id', 'nome_municipio'], how='outer')

# Lista com os anos
cols = ['2001', '2002', '2003', '2004', '2005', '2006', '2008', '2009', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']

# Tratamento dos dados
df_estimativa_populacao[cols] = df_estimativa_populacao[cols].replace("...", 0)
df_estimativa_populacao[cols] = df_estimativa_populacao[cols].astype(int)

# Imputando dados para 2007
df_estimativa_populacao['2007'] = (df_estimativa_populacao['2006'] + df_estimativa_populacao['2008']) / 2

##### Dados de Censo IBGE

# Itera sobre os censos de 2010 e 2022
for year in censos:
    url_2 = url_censo.format(year)
    data = requests.get(url_2).json()
    
    # Extrai os dados de cada ano e cria um DataFrame
    rows = []
    for item in data:
        for result in item['resultados']:
            for series in result['series']:
                row = {
                    'id': series['localidade']['id'],
                    'nome_municipio': series['localidade']['nome'],
                    str(year): series['serie'][str(year)]
                }
                rows.append(row)
    
    df_year = pd.DataFrame(rows)
    dfs_2.append(df_year)

# Mesclando os DataFrames de cada ano em um único DataFrame
df_censo = dfs_2[0]
for df_year in dfs_2[1:]:
    df_censo = pd.merge(df_censo, df_year, on=['id', 'nome_municipio'], how='outer')

# Tratamento dos dados
cols = ['2010', '2022']
df_censo[cols] = df_censo[cols].replace("...", 0)
df_censo[cols] = df_censo[cols].astype(int)

df_censo.drop(columns=['nome_municipio'], inplace=True)

##### Transformando dois DataFrames em um único
df_populacao = df_estimativa_populacao.merge(df_censo, on='id', how='outer')

# Criando novas colunas
df_populacao[['nome_municipio', 'sigla_UF']] = df_populacao['nome_municipio'].str.extract(r'(.+)\s-\s(.+)')
df_populacao['id_mun'] = df_populacao['id'].apply(lambda x: int(str(x)[:-1]))
df_populacao.rename(columns={'id': 'cod_ibge'}, inplace=True)

# Lista de colunas
cols = ['cod_ibge', 'id_mun', 'nome_municipio', 'sigla_UF',
        '2001', '2002', '2003', '2004', '2005', '2006', '2007', 
        '2008', '2009', '2010', '2011', '2012', '2013', '2009', 
        '2010', '2011', '2012', '2013', '2014', '2015', '2016', 
        '2017', '2018', '2019', '2020', '2021', '2022']

# Reordena as colunas do DataFrame final
df_populacao = df_populacao[cols]

# Exportando DataFrames para arquivos .csv
df_populacao.to_csv('../../data/interim/populacao.csv', index=False)
