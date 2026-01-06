import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

np.random.seed(42)

# Geração de dados
alturas = np.random.randint(150, 200, size=200)
pesos = np.random.randint(45, 100, size=len(alturas))

df = pd.DataFrame({
    "altura": alturas,
    "peso": pesos
})

df["altura_m"] = df["altura"] / 100
df["IMC"] = df["peso"] / df["altura_m"] ** 2

X = df[["altura_m", "peso"]]
y = df["IMC"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

pipeline.fit(X_train, y_train)

# Avaliação
y_pred = pipeline.predict(X_test)
r2 = r2_score(y_test, y_pred)

print(f"R² do modelo: {r2:.4f}")

# Salvar modelo
joblib.dump(pipeline, "model/imc_model.pkl")
print("Modelo salvo em model/imc_model.pkl")
