import pandas as pd
import matplotlib.pyplot as plt

data = {
    "mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
    "ventas": [12000, 15000, 18000, 14000, 21000, 19000]
}

df = pd.DataFrame(data)

print(df)

print("\nVenta promedio mensual:", df["ventas"].mean())
print("Mejor mes:", df.loc[df["ventas"].idxmax(), "mes"])

plt.plot(df["mes"], df["ventas"])
plt.title("Ventas Mensuales")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()