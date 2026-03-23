from ETL.load import load_data

processed_data = "data/processed/relatorio_indicadores_agendamentos.parquet"
db_path = "database/validado.db"


if __name__ == "__main__":
    print("Carregado")
    load_data(processed_data, db_path)