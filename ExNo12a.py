# Normal Values
# Import pandas and matplotlib libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the data set from a CSV file
pima = pd.read_csv("pima-indians-diabetes.csv")

# Plot histograms of each feature
pima.hist(figsize=(12,10))
plt.show()

