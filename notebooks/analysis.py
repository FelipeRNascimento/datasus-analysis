import pandas as pd
import matplotlib.pyplot as plt

# Criando um dataset simples (simulação de dados de saúde)
data = {
    "estado": ["SP", "RJ", "MG", "BA", "RS"],
    "atendimentos": [12000, 8500, 9500, 7000, 6000]
}

df = pd.DataFrame(data)

# Visualizar dados
print(df)

# Ordenar para análise
df = df.sort_values(by="atendimentos", ascending=False)

# Criar gráfico
plt.figure()
plt.bar(df["estado"], df["atendimentos"])
plt.title("Atendimentos por Estado")
plt.xlabel("Estado")
plt.ylabel("Total de Atendimentos")
plt.tight_layout()
plt.show()

# Insight simples
print("\nINSIGHT:")
print("SP concentra o maior volume de atendimentos, indicando maior demanda ou capacidade instalada.")
