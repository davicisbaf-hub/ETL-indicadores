import sqlite3
import pandas as pd

def load_data(processed_data, db_path):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()    

    df_validado = pd.read_parquet(processed_data)
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS validado (
            baixar_guia TEXT PRIMARY KEY,
            nome TEXT,
            idade TEXT,
            sexo TEXT,
            prestador TEXT,
            profissional TEXT,
            procedimento TEXT,
            quantidade INTEGER, 
            valor_sus DECIMAL(10, 2),
            valor_regional DECIMAL(10, 2),
            valor_total DECIMAL(10, 2),
            data DATE
        )
    ''')
    
    df_validado = df_validado.drop_duplicates(subset=["baixar_guia"])

    existentes = pd.read_sql(
        "SELECT baixar_guia FROM validado", con
    )

    df_validado = df_validado[~df_validado["baixar_guia"].isin(existentes["baixar_guia"])]

    df_validado.to_sql("validado", con, if_exists="append", index=False)

    con.close()