# Let's first load the uploaded CSV file to understand its structure and identify the categorical data.
import pandas as pd


# Load the data
data_path = 'Data\main_data.csv'
data = pd.read_csv(data_path)

# Display the first few rows to understand the structure
data.head()


import matplotlib.pyplot as plt

# Function to plot frequency tables for each categorical column
def plot_frequency_tables(data):
    categorical_columns = ['gender', 'group', 'parent degrees', 'lunch', 'test prep', 'result', 'grade']
    fig, axes = plt.subplots(nrows=len(categorical_columns), ncols=1, figsize=(10, 20))

    for i, column in enumerate(categorical_columns):
        frequency = data[column].value_counts()
        axes[i].bar(frequency.index, frequency.values, color='skyblue')
        axes[i].set_title(f'Frequency of {column}')
        axes[i].set_ylabel('Frequency')
        axes[i].set_xticklabels(frequency.index, rotation=45, ha="right")

    plt.tight_layout()
    plt.show()

plot_frequency_tables(data)
