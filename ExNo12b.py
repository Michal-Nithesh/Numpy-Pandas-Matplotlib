# Density and contour plots
# Import pandas, seaborn, and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data set from a CSV file
pima = pd.read_csv("pima-indians-diabetes.csv")

# Plot KDE plots of each feature
sns.displot(pima, kind="kde", height=8, aspect=1.5)
plt.show()