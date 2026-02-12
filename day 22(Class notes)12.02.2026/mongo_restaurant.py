from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Step 2: Connect to your database
db = client["restaurant_db"]

# Step 3: Connect to your collection
collection = db["restaurants"]

# Step 4: Create restaurant document (Teacher's data)
new_restaurant = {
    "name": "Spice Villa",
    "location": "Bhubaneswar",
    "category": "Indian",
    "rating": 4.5
}

# Step 5: Insert into MongoDB
insert_result = collection.insert_one(new_restaurant)

# Step 6: Print inserted data
print("Inserted Restaurant ID:", insert_result.inserted_id)

print("Inserted Document:")
print(collection.find_one({"_id": insert_result.inserted_id}))
