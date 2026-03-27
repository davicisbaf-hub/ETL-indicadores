![Logo Opera facil](https://cisbaf.org.br/uploads/siteDescricao/design-sem-nome-74_(150).png)


ESTRUTURA DAS COLUNAS

Filtros adicionados (ORDEM)

1. Agendamento:
    Indicador
2. Paciente:
    Nome, idade, sexo
3. Fornecedor
    Nome Fantasia
4. Profissional
    Nome
5. Procedimento
    Descrição, Valor SUS, Valor Regional
6. Agendamento
    Data/Hora


```
        
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

## Dataset Preparation
| Dataset  |   Download   |
|   ---    |     ---      |
| Raw File | [download](https://raw.githubusercontent.com/davicisbaf-hub/arquivos-download/main/relatorio_indicadores_agendamentos.xlsx) |

## 👨‍💻 Desenvolvedores

| Foto | Nome | Função |
|------|------|--------|
| <img src="https://github.com/Davi-html.png" width="60"/> | Seu Nome | Data Engineer |
| <img src="https://github.com/davicisbaf-hub.png" width="60"/> | Outro Nome | Data Analyst |