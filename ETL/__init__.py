from ETL.transform import transform_data
import pandas as pd

pd.DataFrame.to_parquet(transform_data("data/raw/relatorio_indicadores_agendamentos.xlsx"), "data/processed/relatorio_indicadores_agendamentos.parquet", index=False)