import pandas as pd
import numpy as np

# Simulamos 100 ventas
np.random.seed(42)

df = pd.DataFrame({
    "producto": np.random.choice(["Notebook", "Mouse", "Monitor"], 100),
    "cantidad": np.random.randint(1, 5, 100),
    "precio_unitario": np.random.choice([25, 300, 1200], 100)
})

df["facturacion"] = df["cantidad"] * df["precio_unitario"]

print(df.head())

print("\nFacturación total:", df["facturacion"].sum())

print("\nFacturación por producto:")
print(df.groupby("producto")["facturacion"].sum())

print("\nCantidad total vendida por producto:")
print(df.groupby("producto")["cantidad"].sum())

print("\nPrecio promedio por producto:")
print(df.groupby("producto")["precio_unitario"].mean())

print("\nResumen completo:")
print(df.groupby("producto").agg({
    "cantidad": "sum",
    "precio_unitario": "mean",
    "facturacion": "sum"
}))

resumen = df.groupby("producto").agg({
    "cantidad": "sum",
    "facturacion": "sum"
})

resumen["precio_promedio_real"] = resumen["facturacion"] / resumen["cantidad"]

print("\nResumen mejorado:")
print(resumen)