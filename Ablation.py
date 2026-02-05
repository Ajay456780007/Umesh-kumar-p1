import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager

import matplotlib.pyplot as plt

# Apply the fix from Step 1 first!

# Set global font to Times New Roman
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

# Force Bold for every specific element
plt.rcParams["font.weight"] = "bold"  # For ticks
plt.rcParams["axes.labelweight"] = "bold"  # For xlabel and ylabel
plt.rcParams["axes.titleweight"] = "bold"  # For titl

m = [98.405798, 97.754890, 99.4118]
n = ["SBOA", "CSA", "CHOA"]
colors = ["grey", "maroon", "green"]
plt.style.use("ggplot")
plt.bar(n, m, color=colors)
plt.ylabel("Accuracy (%)", fontweight="bold")
os.makedirs("Image_Results/DB2/Ablation/", exist_ok=True)
plt.savefig("Image_Results/DB2/Ablation/Ablation.png")
csv = pd.DataFrame([m], columns=n)
csv.to_csv("Image_Results/DB2/Ablation/Ablation.csv", index=False)
plt.show()
