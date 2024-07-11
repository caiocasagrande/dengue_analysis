# ---------- Bibliotecas

import pandas as pd
import numpy  as np

# ---------- CasosDengueUF20142023
class CasosDengueUF20142023:
    def __init__(self):
        self.filepath = '../data/raw/casos_dengue_UF_BR_2014_2023.csv'
        self.df = None
        self.df_dengue = None

    def read_data(self):
        """
        Read the CSV file
        """
        self.df = pd.read_csv(
            self.filepath, 
            encoding='latin-1', 
            skiprows=4, 
            nrows=27, 
            sep=';')

        self.df.drop(columns=['Total'], inplace=True)
        self.df.rename(columns={'UF de residência': 'uf'}, inplace=True)
        self.df[['id_uf', 'nome_uf']] = self.df['uf'].str.extract(r'(\d+)\s(.+)')
        self.df.drop(columns=['uf'], inplace=True)
        self.df = self.df[['nome_uf', 'id_uf', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']]
        self.df['id_uf'] = self.df['id_uf'].astype('int64')

    def melt_data(self):
        """
        Reshape the dataframe using pd.melt()
        """
        self.df_dengue = pd.melt(
            self.df, 
            id_vars=['nome_uf', 'id_uf'], 
            var_name='ano', 
            value_name='casos', 
            value_vars=['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'])
        
        # Changing types
        self.df_dengue['ano'] = self.df_dengue['ano'].astype('int64')
        self.df_dengue.casos.replace("-", 0, inplace=True)
        self.df_dengue.casos = self.df_dengue.casos.astype('int64')

    def process_data(self):
        
        if self.df is None:
            self.read_data()

        if self.df_dengue is None:
            self.melt_data()

        return self.df_dengue

# ---------- CasosDengueUF20072013
class CasosDengueUF20072013:
    def __init__(self):
        self.filepath = '../data/raw/casos_dengue_UF_BR_2007_2013.csv'
        self.df = None
        self.df_dengue = None

    def read_data(self):
        """
        Read the CSV file
        """
        self.df = pd.read_csv(
            self.filepath, 
            encoding='latin-1', 
            skiprows=4, 
            nrows=27, 
            sep=';')

        self.df.drop(columns=['Em Branco/ign', 'Total'], inplace=True)
        self.df.rename(columns={'UF de residência': 'uf'}, inplace=True)
        self.df[['id_uf', 'nome_uf']] = self.df['uf'].str.extract(r'(\d+)\s(.+)')
        self.df.drop(columns=['uf'], inplace=True)
        self.df = self.df[['nome_uf', 'id_uf', '2007', '2008', '2009', '2010', '2011', '2012', '2013']]
        self.df['id_uf'] = self.df['id_uf'].astype('int64')

    def melt_data(self):
        """
        Reshape the dataframe using pd.melt()
        """
        self.df_dengue = pd.melt(
            self.df, 
            id_vars=['nome_uf', 'id_uf'], 
            var_name='ano', 
            value_name='casos', 
            value_vars=['2007', '2008', '2009', '2010', '2011', '2012', '2013'])
        
        # Changing types
        self.df_dengue['ano'] = self.df_dengue['ano'].astype('int64')
        self.df_dengue.casos.replace("-", 0, inplace=True)
        self.df_dengue.casos = self.df_dengue.casos.astype('int64')

    def process_data(self):
        
        if self.df is None:
            self.read_data()

        if self.df_dengue is None:
            self.melt_data()

        return self.df_dengue

# ---------- CasosDengueUF20012006
class CasosDengueUF20012006:
    def __init__(self):
        self.filepath = '../data/raw/casos_dengue_UF_BR_2001_2006.csv'
        self.df = None
        self.df_dengue = None

    def read_data(self):
        """
        Read the CSV file
        """
        self.df = pd.read_csv(
            self.filepath, 
            encoding='latin-1', 
            skiprows=4, 
            nrows=27, 
            sep=';')

        self.df.drop(columns=['2001', '2002', 'Total'], inplace=True)
        self.df.rename(columns={'UF de residência': 'uf'}, inplace=True)
        self.df[['id_uf', 'nome_uf']] = self.df['uf'].str.extract(r'(\d+)\s(.+)')
        self.df.drop(columns=['uf'], inplace=True)
        self.df = self.df[['nome_uf', 'id_uf', '2003', '2004', '2005', '2006']]
        self.df['id_uf'] = self.df['id_uf'].astype('int64')

    def melt_data(self):
        """
        Reshape the dataframe using pd.melt()
        """
        self.df_dengue = pd.melt(
            self.df, 
            id_vars=['nome_uf', 'id_uf'], 
            var_name='ano', 
            value_name='casos', 
            value_vars=['2003', '2004', '2005', '2006'])
        
        # Changing types
        self.df_dengue['ano'] = self.df_dengue['ano'].astype('int64')
        self.df_dengue.casos.replace("-", 0, inplace=True)
        self.df_dengue.casos = self.df_dengue.casos.astype('int64')

    def process_data(self):
        
        if self.df is None:
            self.read_data()

        if self.df_dengue is None:
            self.melt_data()

        return self.df_dengue

# ---------- ObitosDengueUF20142023
class ObitosDengueUF20142023:
    def __init__(self):
        self.filepath = '../data/raw/obitos_dengue_UF_BR_2014_2023.csv'
        self.df = None
        self.df_dengue = None

    def read_data(self):
        """
        Read the CSV file
        """
        self.df = pd.read_csv(
            self.filepath, 
            encoding='latin-1', 
            skiprows=5, 
            nrows=27, 
            sep=';')

        self.df.drop(columns=['Total'], inplace=True)
        self.df.rename(columns={'UF de residência': 'uf'}, inplace=True)
        self.df[['id_uf', 'nome_uf']] = self.df['uf'].str.extract(r'(\d+)\s(.+)')
        self.df.drop(columns=['uf'], inplace=True)
        self.df = self.df[['nome_uf', 'id_uf', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']]
        self.df['id_uf'] = self.df['id_uf'].astype('int64')

    def melt_data(self):
        """
        Reshape the dataframe using pd.melt()
        """
        self.df_dengue = pd.melt(
            self.df, 
            id_vars=['nome_uf', 'id_uf'], 
            var_name='ano', 
            value_name='obitos', 
            value_vars=['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'])
        
        # Changing types
        self.df_dengue['ano'] = self.df_dengue['ano'].astype('int64')
        self.df_dengue.obitos.replace("-", 0, inplace=True)
        self.df_dengue.obitos = self.df_dengue.obitos.astype('int64')

    def process_data(self):
        
        if self.df is None:
            self.read_data()

        if self.df_dengue is None:
            self.melt_data()

        return self.df_dengue

# ---------- ObitosDengueUF20072013
class ObitosDengueUF20072013:
    def __init__(self):
        self.filepath = '../data/raw/obitos_dengue_UF_BR_2007_2013.csv'
        self.df = None
        self.df_dengue = None

    def read_data(self):
        """
        Read the CSV file
        """
        self.df = pd.read_csv(
            self.filepath, 
            encoding='latin-1', 
            skiprows=5, 
            nrows=27, 
            sep=';')

        self.df.drop(columns=['Total'], inplace=True)
        self.df.rename(columns={'UF de residência': 'uf'}, inplace=True)
        self.df[['id_uf', 'nome_uf']] = self.df['uf'].str.extract(r'(\d+)\s(.+)')
        self.df.drop(columns=['uf'], inplace=True)
        self.df = self.df[['nome_uf', 'id_uf', '2007', '2008', '2009', '2010', '2011', '2012', '2013']]
        self.df['id_uf'] = self.df['id_uf'].astype('int64')

    def melt_data(self):
        """
        Reshape the dataframe using pd.melt()
        """
        self.df_dengue = pd.melt(
            self.df, 
            id_vars=['nome_uf', 'id_uf'], 
            var_name='ano', 
            value_name='obitos', 
            value_vars=['2007', '2008', '2009', '2010', '2011', '2012', '2013'])
        
        # Changing types
        self.df_dengue['ano'] = self.df_dengue['ano'].astype('int64')
        self.df_dengue.obitos.replace("-", 0, inplace=True)
        self.df_dengue.obitos = self.df_dengue.obitos.astype('int64')

    def process_data(self):
        
        if self.df is None:
            self.read_data()

        if self.df_dengue is None:
            self.melt_data()

        return self.df_dengue

# ---------- ObitosDengueUF20012006
class ObitosDengueUF20012006:
    def __init__(self):
        self.filepath = '../data/raw/obitos_dengue_UF_BR_2001_2006.csv'
        self.df = None
        self.df_dengue = None

    def read_data(self):
        """
        Read the CSV file
        """
        self.df = pd.read_csv(
            self.filepath, 
            encoding='latin-1', 
            skiprows=5, 
            nrows=23, 
            sep=';')

        self.df.drop(columns=['2002', 'Total'], inplace=True)
        self.df.rename(columns={'UF de residência': 'uf'}, inplace=True)
        self.df[['id_uf', 'nome_uf']] = self.df['uf'].str.extract(r'(\d+)\s(.+)')
        self.df.drop(columns=['uf'], inplace=True)
        self.df = self.df[['nome_uf', 'id_uf', '2003', '2004', '2005', '2006']]
        self.df['id_uf'] = self.df['id_uf'].astype('int64')

    def melt_data(self):
        """
        Reshape the dataframe using pd.melt()
        """
        self.df_dengue = pd.melt(
            self.df, 
            id_vars=['nome_uf', 'id_uf'], 
            var_name='ano', 
            value_name='obitos', 
            value_vars=['2003', '2004', '2005', '2006'])
        
        # Changing types
        self.df_dengue['ano'] = self.df_dengue['ano'].astype('int64')
        self.df_dengue.obitos.replace("-", 0, inplace=True)
        self.df_dengue.obitos = self.df_dengue.obitos.astype('int64')

    def process_data(self):
        
        if self.df is None:
            self.read_data()

        if self.df_dengue is None:
            self.melt_data()

        return self.df_dengue

# ----------