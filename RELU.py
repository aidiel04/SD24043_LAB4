import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="ReLU Activation", layout="centered")
st.title("1. Rectified Linear Unit (ReLU)")
st.write("Formula: $f(x) = \max(0, x)$")

# Generate data based on foundation_nn.py xgrid parameters
xgrid = np.linspace(-6, 6, 400)
y = np.maximum(0, xgrid)

# Plotting
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(xgrid, y, label="relu", color="blue")
ax.grid(True)
ax.legend()
ax.set_title("ReLU Curve")

st.pyplot(fig)