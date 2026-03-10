import pandas as pd
import matplotlib.pyplot as plt

# Datos simulados
data = {
    "producto": ["Notebook", "Mouse", "Teclado", "Monitor", "Auriculares"],
    "ventas": [15, 40, 25, 10, 30],
    "precio_unitario": [1200, 25, 45, 300, 80]
}

df = pd.DataFrame(data)

# Crear columna de facturación
df["facturacion"] = df["ventas"] * df["precio_unitario"]

print("=== DATAFRAME ===")
print(df)

print("\n=== MÉTRICAS ===")
print("Facturación total:", df["facturacion"].sum())
print("Producto más vendido:", df.loc[df["ventas"].idxmax(), "producto"])
print("Producto más rentable:", df.loc[df["facturacion"].idxmax(), "producto"])

print("\n=== ANÁLISIS EXTRA ===")

# Ordenar por facturación
df_ordenado = df.sort_values("facturacion", ascending=False)
print("\nProductos ordenados por facturación:")
print(df_ordenado[["producto", "facturacion"]])

# Top 3 productos
top_3 = df_ordenado.head(3)
print("\nTop 3 productos más rentables:")
print(top_3[["producto", "facturacion"]])

# Gráfico
plt.bar(df["producto"], df["facturacion"])
plt.title("Facturación por producto")
plt.xlabel("Producto")
plt.ylabel("Facturación")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()