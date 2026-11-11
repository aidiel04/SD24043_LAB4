import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sigmoid Activation", layout="centered")
st.title("2. Sigmoid (Logistic)")
st.write("Formula: $f(x) = \\frac{1}{1 + e^{-x}}$")

# Generate data based on foundation_nn.py xgrid parameters
xgrid = np.linspace(-6, 6, 400)
y = 1 / (1 + np.exp(-xgrid))

# Plotting
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(xgrid, y, label="logistic (sigmoid)", color="green")
ax.grid(True)
ax.legend()
ax.set_title("Sigmoid Curve")

st.pyplot(fig)