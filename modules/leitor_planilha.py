import pandas as pd

def carregar_dados(caminho_planilha):
    df = pd.read_excel(caminho_planilha)
    # validar dados básicos
    if 'Cliente' not in df.columns or 'Servico' not in df.columns:
        raise ValueError('Colunas obrigatórias ausentes')
    return df.to_dict(orient='records')
