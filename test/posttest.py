import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/content/drive/My Drive/Colab Notebooks/adult.csv')

# Calculate the average income and standard deviation
average_income = df['Income'].mean()
std_dev_income = df['Income'].std()

#print("Dataframe:", df)
print("Average Income:", average_income)
print("Standard Deviation of Income:", std_dev_income)

# Create a histogram of the income distribution
df['Income'].hist()
plt.title('Income Distribution')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.show()
