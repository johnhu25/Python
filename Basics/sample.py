import random
import csv

housing_data = []
for _ in range(20):
    row = {
        "longitude": round(random.uniform(-124.35, -114.31), 5),
        "latitude": round(random.uniform(32.54, 41.95), 5),
        "housing_median_age": random.randint(1, 52),
        "total_rooms": random.randint(200, 10000),
        "total_bedrooms": random.randint(100, 3000),
        "population": random.randint(100, 5000),
        "households": random.randint(50, 2000),
        "median_income": round(random.uniform(1.5, 15.0), 2),
        "median_house_value": random.randint(15000, 500001)
    }
    housing_data.append(row)

# Save to CSV
with open("housing_data.csv", "w", newline="") as csvfile:
    fieldnames = housing_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(housing_data)

# Preview generated data
for row in housing_data:
    print(row)
