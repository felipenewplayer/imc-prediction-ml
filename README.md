#  IMC Prediction with Machine Learning

##  Visão Geral do Projeto

Este projeto consiste no desenvolvimento de um **modelo de Machine Learning para predição do IMC (Índice de Massa Corporal)** a partir de dados de **peso** e **altura**, com disponibilização do modelo em uma **interface web interativa utilizando Streamlit**.

O objetivo é demonstrar, de forma prática, o **pipeline completo de um projeto de Machine Learning**, desde a modelagem até o deploy em nuvem, seguindo boas práticas utilizadas no mercado.

---

##  Objetivo do Sistema

Permitir que o usuário informe:

*  **Altura (cm)**
*  **Peso (kg)**

E o sistema retorna:

 **IMC previsto**
 **Classificação automática** (Abaixo do peso, Normal, Sobrepeso, Obesidade)

---

## Abordagem de Machine Learning

### Tipo de Problema

* **Regressão supervisionada**

### Variáveis

* **Features (X):** Altura, Peso
* **Target (y):** IMC

### Modelo Utilizado

* `LinearRegression` (Scikit-learn)

Motivo da escolha:

* Relação matemática direta entre peso, altura e IMC
* Modelo interpretável
* Excelente baseline para problemas numéricos contínuos

---

## Pipeline do Projeto

1. Geração / preparação dos dados
2. Separação em treino e teste
3. Treinamento do modelo
4. Avaliação do modelo
5. Salvamento com `joblib`
6. Criação da interface com Streamlit
7. Deploy no Streamlit Cloud

---

## Interface com Streamlit

A aplicação web permite:

* Inserção de dados via **sliders**
* Validação automática de valores
* Exibição clara do resultado
* Experiência amigável ao usuário final

> Interface pensada para usuários não técnicos

---

##  Deploy

A aplicação está hospedada no **Streamlit Cloud**, garantindo:

* Acesso público
* Ambiente isolado
* Reprodutibilidade

🔗 **Demo online:** https://imc-prediction-ml-68e39a7v555an8nyk85pb3.streamlit.app/

---

## Tecnologias Utilizadas

* Python 3
* Scikit-learn
* Pandas
* NumPy
* Joblib
* Streamlit

---

## Estrutura do Projeto

```
imc-prediction-ml/
│── app.py              # Aplicação Streamlit
│── model.pkl           # Modelo treinado
│── requirements.txt    # Dependências
│── README.md           # Documentação
```

---

## 🧪 Como Executar Localmente

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/imc-prediction-ml.git

# Acessar o projeto
cd imc-prediction-ml

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
streamlit run app.py
```

---

