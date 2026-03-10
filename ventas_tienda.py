import pandas as pd
import matplotlib.pyplot as plt

data = {
    "venta_id": [1,1,2,2,3,3,4,4,5,5,6,6,7,7],
    "producto": [
        "Notebook","Mouse",
        "Notebook","Teclado",
        "Monitor","Mouse",
        "Notebook","Monitor",
        "Teclado","Mouse",
        "Notebook","Monitor",
        "Monitor","Mouse"
    ],
    "cantidad": [1,2,1,1,2,3,1,1,2,1,1,2,1,4],
    "precio_unitario": [1200,20,1200,50,300,20,1200,300,50,20,1200,300,300,20],
    "costo_unitario": [1000,10,1000,30,200,10,1000,200,30,10,1000,200,200,10]
}

df = pd.DataFrame(data)
df["ingreso"] = df["cantidad"] * df["precio_unitario"]
df["costo_total"] = df["cantidad"] * df["costo_unitario"]
df["utilidad"] = df["ingreso"] - df["costo_total"]
print(df)

print("\nFacturación por producto:")
print(df.groupby("producto")["ingreso"].sum())

print("\nUtilidad total por producto:")
print(df.groupby("producto")["utilidad"].sum())

print("\nMargen por producto:")
resumen = df.groupby("producto").agg({
    "ingreso": "sum",
    "costo_total": "sum",
    "utilidad": "sum"
})
resumen["margen"] = resumen["utilidad"] / resumen["ingreso"]
print(resumen)

print("\nIngreso total por porcentaje")
ingreso_producto = df.groupby("producto")["ingreso"].sum()
ingreso_total = df["ingreso"].sum()
porcentaje = (ingreso_producto / ingreso_total) * 100
print(porcentaje)

ingreso_producto = df.groupby("producto")["ingreso"].sum()

plt.bar(ingreso_producto.index, ingreso_producto.to_numpy())

plt.title("Ingresos por producto")
plt.xlabel("Producto")
plt.ylabel("Ingresos")

plt.show()

utilidad_producto = df.groupby("producto")["utilidad"].sum()

plt.bar(utilidad_producto.index, utilidad_producto.to_numpy())

plt.title("Utilidad por producto")
plt.xlabel("Producto")
plt.ylabel("Utilidad")

plt.show()

margen_producto = resumen["utilidad"] / resumen["ingreso"]
plt.bar(margen_producto.index, margen_producto.to_numpy())
plt.title("Margen por producto")
plt.xlabel("Producto")
plt.ylabel("Margen")

plt.show()