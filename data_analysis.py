# Dayvion Peoples

import pandas as pd

# Read the csv file into a variable
df = pd.read_csv("popular_anime.csv")

# Dispaly first few rows in the dataset
print(df.head(10))


# Put the id cloumn into a variable
id_count = df["id"]

# Display largest id count
print(id_count.max())

largest_id_count = df[df['id'] == df['id'].max()]
print("Largest number of id")
print()
print(largest_id_count)

# Display smallest id count
#print(id_count.min())
