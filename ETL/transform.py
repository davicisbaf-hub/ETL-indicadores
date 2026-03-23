from ETL.extract import extract_data
import pandas as pd

def transform_data(raw_file_path):
    data = extract_data(raw_file_path)

    data = pd.read_excel(raw_file_path)

    data = data.iloc[19:]

    data.columns = [
        "codigo_agenda",
        "nome",
        "idade",
        "sexo",
        "prestador",
        "profissional",
        "procedimento",
        "valor_sus",
        "valor_regional",
        "valor_total",
        "data"
    ]

    data["data"] = data["data"].astype(str).str.split(' ').str[0]

    return data