import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def predict(df: pd.DataFrame):
    
    # Carregar o modelo do arquivo pickle
    dict_model = pickle.load(open("./documents/model/model2.pkl", "rb"))

    # Extrair o modelo e as colunas usadas no treinamento
    model: RandomForestClassifier = dict_model["model"]

    # Verificar as colunas que estão faltando
    expected_cols = dict_model["cols"]
    missing_cols = [col for col in expected_cols if col not in df.columns]
    
    if missing_cols:
        raise KeyError(f"Estas colunas estão faltando no DataFrame: {missing_cols}")

    # Selecionar as colunas que o modelo espera
    X = df[expected_cols]

    # Fazer a previsão de probabilidades
    y_proba = model.predict_proba(X)

    return y_proba[0]
