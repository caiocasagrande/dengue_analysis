# Bibliotecas
import pandas   as pd
import requests

# URLs API IBGE
url_est_pop = 'https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/{}/variaveis/9324?localidades=N3[all]'
url_censo   = 'https://servicodados.ibge.gov.br/api/v3/agregados/9605/periodos/2010|2022/variaveis/93?localidades=N3[all]'

# Listas de apoio
data_dict_pop   = []
data_dict_censo = []

# ---------- Estimativa da População

# Loop para obter os dados dos anos, exceto 2007 e 2010
for year in range(2001, 2022):
    if year not in [2007, 2010]:
        url = url_est_pop.format(year)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            series_list = data[0]['resultados'][0]['series']
            for item in series_list:
                nome_uf = item['localidade']['nome']
                serie = item['serie']
                for ano, valor in serie.items():
                    data_dict_pop.append({'nome_uf': nome_uf, 'ano': int(ano), 'populacao': int(valor)})
        else:
            print(f"Erro ao buscar dados de Estimativa da População: {response.status_code}")

# DataFrame
df_pop = pd.DataFrame(data_dict_pop)

# Calculando a população de 2007 como a média entre 2006 e 2008
pop_07 = []
df_pop_0608 = df_pop[df_pop['ano'].isin([2006, 2008])]
ufs = df_pop_0608['nome_uf'].unique()

for uf in ufs:
    pop_2006 = df_pop_0608[(df_pop_0608['nome_uf'] == uf) & (df_pop_0608['ano'] == 2006)]['populacao'].values[0]
    pop_2008 = df_pop_0608[(df_pop_0608['nome_uf'] == uf) & (df_pop_0608['ano'] == 2008)]['populacao'].values[0]
    pop_2007 = (pop_2006 + pop_2008) // 2
    pop_07.append({'nome_uf': uf, 'ano': 2007, 'populacao': pop_2007})

# DataFrame para 2007
df_pop_07 = pd.DataFrame(pop_07)

# ---------- Censo Demográfico

# Obtendo os dados 
response = requests.get(url_censo)

# Organizando dados
if response.status_code == 200:
    data = response.json()
    series_list = data[0]['resultados'][0]['series']
    for item in series_list:
        nome_uf = item['localidade']['nome']
        serie = item['serie']
        for ano, valor in serie.items():
            data_dict_censo.append({'nome_uf': nome_uf, 'ano': int(ano), 'populacao': int(valor)})
else:
    print(f"Erro ao buscar dados do Censo: {response.status_code}")

# DataFrame para o Censo
df_pop_censo = pd.DataFrame(data_dict_censo)

# ---------- Resultados finais

# Concatenando dados
df_populacao = pd.concat([df_pop, df_pop_07, df_pop_censo], ignore_index=True)

# Ordena o DataFrame por localidade e ano
df_populacao = df_populacao.sort_values(by=['nome_uf', 'ano']).reset_index(drop=True)

# Dicionário de id_ufs
dict_id_ufs = {
    'Acre': 12, 'Alagoas': 27, 'Amapá': 16, 'Amazonas': 13, 'Bahia': 29, 'Ceará': 23, 'Distrito Federal': 53, 
    'Espírito Santo': 32, 'Goiás': 52, 'Maranhão': 21, 'Mato Grosso': 51, 'Mato Grosso do Sul': 50, 'Minas Gerais': 31, 
    'Paraná': 41, 'Paraíba': 25, 'Pará': 15, 'Pernambuco': 26, 'Piauí': 22, 'Rio Grande do Norte': 24, 'Rio Grande do Sul': 43, 
    'Rio de Janeiro': 33, 'Rondônia': 11, 'Roraima': 14, 'Santa Catarina': 42, 'Sergipe': 28, 'São Paulo': 35, 'Tocantins': 17
}

# Cria coluna id_uf
df_populacao['id_uf'] = df_populacao['nome_uf'].map(dict_id_ufs)
df_populacao['id_uf'] = df_populacao['id_uf'].astype('int64')

# Reordenamdo colnunas
df_populacao = df_populacao[['nome_uf', 'id_uf', 'ano', 'populacao']]

# Exportando resultados
df_populacao.to_csv('../../data/interim/uf_populacao.csv', index=False)