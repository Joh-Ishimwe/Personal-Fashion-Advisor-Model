import pandas as pd
import numpy as np
import random

# Define possible values for dataset features
body_types = ["Hourglass", "Rectangle", "Pear", "Inverted Triangle", "Oval"]
event_types = ["Casual", "Formal", "Wedding", "Party", "Business"]
colors = ["Red", "Blue", "Black", "White", "Gold", "Silver", "Green", "Neutral"]
seasons = ["Summer", "Winter", "Spring", "Fall"]
fabrics = ["Cotton", "Silk", "Polyester", "Wool", "Denim"]
genders = ["Male", "Female", "Unisex"]
price_ranges = ["Budget", "Mid-range", "Luxury"]
style_categories = ["Streetwear", "Bohemian", "Business Casual", "Formal", "Glam"]

# Define weights for balancing categories
style_weights = [0.2, 0.2, 0.2, 0.2, 0.2]  # Equal weights for balancing
event_weights = [0.3, 0.2, 0.1, 0.2, 0.2]  # Higher weight for "Casual" and "Formal"

# Function to generate realistic combinations
def generate_realistic_row():
    # Randomly select features with constraints
    body_type = random.choice(body_types)
    event_type = random.choices(event_types, weights=event_weights, k=1)[0]
    preferred_colors = random.sample(colors, k=random.randint(1, 3))
    season = random.choice(seasons)
    
    # Fabric type based on season
    if season == "Winter":
        fabric_type = random.choices(["Wool", "Denim", "Polyester"], weights=[0.5, 0.3, 0.2], k=1)[0]
    else:
        fabric_type = random.choices(["Cotton", "Silk", "Polyester"], weights=[0.5, 0.3, 0.2], k=1)[0]
    
    gender = random.choice(genders)
    price_range = random.choice(price_ranges)
    occasion_score = round(random.uniform(1, 10), 1)
    
    # Style category based on event type and body type
    if event_type == "Formal":
        style_category = random.choices(["Formal", "Glam", "Business Casual"], weights=[0.5, 0.3, 0.2], k=1)[0]
    else:
        style_category = random.choices(style_categories, weights=style_weights, k=1)[0]
    
    return {
        "Body Type": body_type,
        "Event Type": event_type,
        "Preferred Colors": preferred_colors,
        "Season": season,
        "Fabric Type": fabric_type,
        "Gender": gender,
        "Price Range": price_range,
        "Occasion Suitability Score": occasion_score,
        "Style Category": style_category  # Target Label
    }

# Function to generate dataset
def generate_fashion_dataset(num_samples=10000):
    data = [generate_realistic_row() for _ in range(num_samples)]
    return pd.DataFrame(data)

# Generate dataset with 10000 samples
fashion_df = generate_fashion_dataset(10000)

# Save to CSV
fashion_df.to_csv("fashion_dataset.csv", index=False)
print("Dataset saved successfully as 'fashion_dataset.csv'")