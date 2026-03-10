from sklearn.cluster import KMeans #type: ignore

def crear_clusters(data, n_clusters=3):
    modelo = KMeans(n_clusters=n_clusters)
    modelo.fit(data)
    return modelo.labels_