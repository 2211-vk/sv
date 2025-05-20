import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

col1, col2 = st.columns(2)
with col1:
    u = st.slider('${\mu}$',-10.00, 10.00)
with col2:
    o = st.slider('${\sigma}$',0.10, 10.00)
np.random.seed(10)
a = np.random.normal(loc = u, scale = o, size = 1000)
x = np.linspace(np.min(a), np.max(a), 1000)
fig, ax = plt.subplots()
ax.plot(x, (1/(o*(2*np.pi)**.5))*np.exp(-(((x-u)**2)/2*o**2)), 'b')
ax.set_title('Gauss Mass Function')
ax.set_xlabel('x')
ax.set_ylabel('p(x)')
plt.axhline(0, color='yellow')
plt.axvline(0, color='yellow')

st.pyplot(fig)