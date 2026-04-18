from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def get_dominant_colors(image_file, k=7):
    # 1. Load image
    image = Image.open(image_file).convert("RGB")

    # 2. Resize (important for speed)
    image = image.resize((200, 200))

    # 3. Convert to numpy array
    image = np.array(image)

    # 4. Flatten image → list of pixels
    pixels = image.reshape((-1, 3))

    # 5. Apply KMeans clustering
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)

    # 6. Get cluster centers (dominant colors)
    colors = kmeans.cluster_centers_

    return colors.astype(int)
