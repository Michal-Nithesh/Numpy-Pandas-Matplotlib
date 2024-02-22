# Three-dimensional plotting
# Import pandas, matplotlib, and mpl_toolkits libraries
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data set from a CSV file
pima = pd.read_csv("pima-indians-diabetes.csv")

# Plot 3D scatter plots of three features
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pima['Glucose'], pima['BMI'], pima['Age'], c=pima['Outcome'], cmap='coolwarm')
ax.set_xlabel('Glucose')
ax.set_ylabel('BMI')
ax.set_zlabel('Age')
plt.show()
