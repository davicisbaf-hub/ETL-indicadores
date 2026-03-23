```
ESTRUTURA DAS COLUNAS

![Logo Opera facil](blob:https://app.powerbi.com/07609afe-4ecc-4a94-b15e-5455de2b5ea0)

Filtros adicionados
"codigo_agenda" | "nome" | "idade" | "sexo" | "prestador" | "profissional" | "procedimento" | "valor_sus" | "valor_regional" | "valor_total" | "data"
        
📁relatorio_indicadores
    └── 📁data
        └── 📁processed
            ├── relatorio_indicadores_agendamentos.parquet
        └── 📁raw
            ├── relatorio_indicadores_agendamentos.xlsx
    └── 📁database
        ├── validado.db
    └── 📁ETL
        ├── __init__.py
        ├── extract.py
        ├── load.py
        ├── transform.py
    ├── .gitignore
    ├── main.py
    └── requirements.txt
```