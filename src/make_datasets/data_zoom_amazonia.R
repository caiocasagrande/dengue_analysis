# Data Zoom Amazonia

# ----- Libraries

# Main library
library(datazoom.amazonia)

# Data manipulation
library(writexl)

# ----- AMAZONIA LEGAL
df_alb_mun = datazoom.amazonia::municipalities

# Filtering to Brazilian Legal Amazon (BLA) municipalities
df_alb_mun = df_alb_mun[df_alb_mun$legal_amazon == 1, ]

# List of municipalities IBGE codes
list_alb_codes = as.list(df_alb_mun$code_muni)

# ----- DEFORESTATION

# Raw deforestation data
df_raw_deforestation_alb = subset(
  load_prodes(
    dataset  = 'deforestation', 
    language = 'pt',
    raw_data = TRUE 
  ), 
  CodIbge %in% list_alb_codes
)

# Clean deforestation clean
df_clean_deforestation_alb = subset(
  load_prodes(
    dataset  = 'deforestation', 
    language = 'pt',
    raw_data = FALSE 
  ), 
  cod_municipio %in% list_alb_codes
)

# Saving deforestation data as CSV
write.csv(df_raw_deforestation_alb, 'data/data_zoom_R/raw_deforestation_alb.csv', row.names = FALSE)
write.csv(df_clean_deforestation_alb, 'data/data_zoom_R/clean_deforestation_alb.csv', row.names = FALSE)

# ----- IPS 

# IPS 2014
df_ips_2014 = subset(
    load_ips(
        dataset = 'all', 
        raw_data = FALSE, 
        time_period = 2014, 
        language = 'pt'
), 
  codigo_ibge %in% list_alb_codes
)

# IPS 2018
df_ips_2018 = subset(
    load_ips(
        dataset = 'all', 
        raw_data = FALSE, 
        time_period = 2018, 
        language = 'pt'
), 
  codigo_ibge %in% list_alb_codes
)

# IPS 2021
df_ips_2021 = subset(
    load_ips(
        dataset = 'all', 
        raw_data = FALSE, 
        time_period = 2021, 
        language = 'pt'
), 
  codigo_ibge %in% list_alb_codes
)

# IPS 2023
df_ips_2023 = subset(
    load_ips(
        dataset = 'all', 
        raw_data = FALSE, 
        time_period = 2023, 
        language = 'pt'
), 
  codigo_ibge %in% list_alb_codes
)

# Saving IPS data as CSV
write.csv(df_ips_2014, 'data/data_zoom_R/ips_2014_alb.csv', row.names = FALSE)
write.csv(df_ips_2018, 'data/data_zoom_R/ips_2018_alb.csv', row.names = FALSE)
write.csv(df_ips_2021, 'data/data_zoom_R/ips_2021_alb.csv', row.names = FALSE)
write.csv(df_ips_2023, 'data/data_zoom_R/ips_2023_alb.csv', row.names = FALSE)