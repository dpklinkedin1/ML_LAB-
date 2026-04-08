import numpy as np
from sklearn.cluster import KMeans

# Data (2D points)
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [8, 7],
    [9, 8],
    [10, 9]
])

# Create model (K = 2 clusters)
model = KMeans(n_clusters=2)

# Train model
model.fit(X)

# Get cluster labels
labels = model.labels_

# Get centroids
centroids = model.cluster_centers_

print("Cluster Labels =", labels)
print("Centroids =", centroids)
