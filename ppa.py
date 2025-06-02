import streamlit as st
import requests
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np

st.title('Image Segmentation with kMeans')
c1, c2 = st.columns(2)
with c1:
    img_url = st.text_input('Image URL (Press Enter to apply)', value = None)
    if img_url != None:
        st.image(img_url, caption = 'Original Image')

with c2:
    k = st.slider('K', 2, 10)
    if img_url != None:
        img_pil = Image.open(requests.get(img_url, stream=True).raw)
        img = np.array(img_pil)
        X = img.copy().reshape(-1, 4)
        Kmeans = KMeans(n_clusters = k, n_init = 'auto')
        Kmeans.fit(X)
        img_new = np.array([Kmeans.cluster_centers_[i] for i in Kmeans.labels_]).reshape(img.shape)
        img_new = np.array(img_new, dtype=np.uint8)
        st.image(img_new, caption = 'Segmented Image')
