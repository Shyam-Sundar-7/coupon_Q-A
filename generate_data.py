import pandas as pd
import random

# Function to generate random data for the dataframe
def generate_data():
    categories = ["electronics", "jewelry", "apparel", "accessories"]
    brands_per_category = {
        "electronics": ["Sony", "Samsung", "LG", "Apple", "Dell"],
        "jewelry": ["Tiffany", "Cartier", "Pandora", "Swatch", "Bvlgari"],
        "apparel": ["Nike", "Adidas", "Zara", "H&M", "Gucci"],
        "accessories": ["Ray-Ban", "Fossil", "Kate Spade", "Michael Kors", "Coach"]
    }
    offers = ["5 percent", "10 percent", "15 percent", "20 percent"]
    expiration_days = list(range(1, 31))

    data = []

    for _ in range(2000):
        category = random.choice(categories)
        brand = random.choice(brands_per_category[category])
        offer = random.choice(offers)
        expiring_days = random.choice(expiration_days)
        sentence = f"🌟 Grab {offer} off on {brand} {category}! Limited offer, only {expiring_days} days left!"
        data.append([category, brand, offer, expiring_days,sentence])

    return data

# Create a DataFrame
columns = ["category", "brand", "offers", "expiring_in_days","Sentence"]
df = pd.DataFrame(generate_data(), columns=columns)
df.drop_duplicates(inplace=True)

# Display the DataFrame
print(df.head())
df.to_csv("data_2.csv", index=False)
