# ---------- Imports

import pandas as pd

# ---------- Constants

# Directories and file paths
DATA_DIR    = '../../data/'
INTERIM_DIR = DATA_DIR + 'interim/'
RAW_DIR     = DATA_DIR + 'raw/'
OUTPUT_FILE = INTERIM_DIR + 'mun_dengue_obitos_amazonia_legal.csv'

# Load Data
ENCODING = 'latin1'
SKIPROWS = 6
SEP      = ';'

# Final Collumns
COLLUMNS = ['cod_ibge', 'id_mun', 'ano', 'obitos']

# ---------- Functions

def load_csv(filepath, skiprows=None, nrows=None, sep=',', encoding=None):
    return pd.read_csv(filepath, skiprows=skiprows, nrows=nrows, sep=sep, encoding=encoding)

def preprocess_dengue_data(df):
    # Renaming 
    df.rename(columns={'Município de residência': 'mun'}, inplace=True)
    # Extracting and cleaning 'id_mun' column
    df['id_mun'] = df['mun'].str.extract(r'(\d+)')
    # Selecting non-null rows
    df = df[~df['id_mun'].isna()]
    # Dropping unnecessary columns
    df.drop(columns=['Total', 'mun'], inplace=True)
    # Cleaning numerical values
    df.replace(["-", "..."], 0, inplace=True)
    # Changing values types
    df = df.astype('int64')
    # Melting data for easier manipulation
    df = pd.melt(df, id_vars='id_mun', var_name='year', value_name='obitos')
    # Changing values type
    df['year'] = df['year'].astype('int64')
    # Return 
    return df

def merge_dengue_data(*dfs):
    # First df
    df_merged = dfs[0]
    # Loop over
    for df in dfs[1:]:
        df_merged = pd.merge(df_merged, df, on=['id_mun', 'year'], how='outer')
    # Transformations
    df_merged.fillna(0, inplace=True)
    df_merged['total'] = df_merged.filter(like='obitos').sum(axis=1).astype('int64')
    df_merged.drop(columns=df_merged.filter(like='obitos').columns, inplace=True)
    df_merged.rename(columns={'year': 'ano', 'total': 'obitos'}, inplace=True)
    # Return merged and cleaned dataset
    return df_merged

def main():
    # Load datasets
    bla     = load_csv(INTERIM_DIR + 'mun_amazonia_legal.csv')[['cod_ibge', 'id_mun']]
    df_1324 = load_csv(RAW_DIR + 'obitos_dengue_MU_BR_2013_2024.csv', encoding=ENCODING, skiprows=SKIPROWS, nrows=185, sep=SEP)
    df_0713 = load_csv(RAW_DIR + 'obitos_dengue_MU_BR_2007_2013.csv', encoding=ENCODING, skiprows=SKIPROWS, nrows=167, sep=SEP)
    df_0106 = load_csv(RAW_DIR + 'obitos_dengue_MU_BR_2001_2006.csv', encoding=ENCODING, skiprows=SKIPROWS, nrows=42,  sep=SEP)

    # Process datasets
    df_1324 = preprocess_dengue_data(df_1324)
    df_0713 = preprocess_dengue_data(df_0713)
    df_0106 = preprocess_dengue_data(df_0106)

    # Merge datasets
    df_merged = merge_dengue_data(df_1324, df_0713, df_0106)
    df_final  = pd.merge(df_merged, bla, on='id_mun', how='left')

    # Rearrange the columns
    df_final = df_final[COLLUMNS]

    # Output final dataset
    df_final.to_csv(OUTPUT_FILE, index=False)

# ---------- Main

if __name__ == '__main__':
    main()