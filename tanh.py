import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Activation", layout="centered")
st.title("3. Hyperbolic Tangent (Tanh)")
st.write("Formula: $f(x) = \\tanh(x)$")

# Generate data based on foundation_nn.py xgrid parameters
xgrid = np.linspace(-6, 6, 400)
y = np.tanh(xgrid)

# Plotting
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(xgrid, y, label="tanh", color="red")
ax.grid(True)
ax.legend()
ax.set_title("Tanh Curve")

st.pyplot(fig)