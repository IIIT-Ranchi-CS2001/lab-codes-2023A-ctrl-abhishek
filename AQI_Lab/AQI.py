import pandas as pd
import numpy as np
path="AQI_Data.csv"
df = pd.read_csv(path)

#Display the first five rows
print("First five rows of the datasheet:-")
print(df.head(5))
print("\n")

#Display the last five rows
print("Last five rows of the datasheet:-")
print(df.tail(5))
print("\n")

#Display the statistics for all numeric columns
print("Summary statistics for all numeric columns are:-")
print(df.describe())
print("\n")

#Display the mean of AQI, PM2.5 and PM10
AQI_mean = np.mean(df['AQI'])
PM_mean = np.mean(df['PM2.5'])
PM10_mean = np.mean(df['PM10'])
print(f"Mean of AQI is {AQI_mean}.")
print("")
print(f"Mean of PM2.5 is {PM_mean}.")
print("")
print(f"Mean of PM10 is {PM10_mean}.")
print("\n")

#Display all rows where the PM2.5 level exceeds 100
pm = df[df["PM2.5"] > 100]
print(pm)
print("\n")

# Initialize an empty dictionary to store counts
row_counts = {}
# Loop through unique values in the 'City' column
for l in pm['City'].unique():
    row_counts[l] = len(pm[pm['City'] == l])
# Print the result
print(row_counts)