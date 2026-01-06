import streamlit as st
import numpy as np
import joblib

# Carregar modelo
model = joblib.load("model/imc_model.pkl")

def classificar_imc(imc):
    if imc < 18.5:
        return "Magreza"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 40:
        return "Obesidade"
    else:
        return "Obesidade Grave"

st.title("🧮 Preditor de IMC com Machine Learning")

altura = st.number_input(
    "Altura (em metros)",
    min_value=1.40,
    max_value=2.10,
    step=0.01
)

peso = st.number_input(
    "Peso (em kg)",
    min_value=30.0,
    max_value=200.0,
    step=0.5
)

if st.button("Calcular IMC"):
    X = np.array([[altura, peso]])
    imc = model.predict(X)[0]

    st.success(f"IMC previsto: {imc:.2f}")
    st.info(f"Classificação: {classificar_imc(imc)}")
