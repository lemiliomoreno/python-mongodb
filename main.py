from pymongo import MongoClient
from bson import ObjectId


MONGODB_URL = "mongodb://academia:academia@localhost:27017"


def get_db():
    mongodb_client = MongoClient(MONGODB_URL)

    return mongodb_client["academia"]


def insert(items: list):
    database = get_db()

    for item in items:
        item["_id"] = str(ObjectId())
        database.inventory.insert_one(item)


def get(filter: dict):
    database = get_db()

    for item in database.inventory.find(filter):
        print(item)


def update(filter: dict, new_value: dict):
    database = get_db()

    database.inventory.update_one(
        filter,
        {
            "$set": new_value,
        }
    )


def delete(id):
    database = get_db()

    database.inventory.delete_one({"_id": id})


# delete("6490fd615aaeebe21135fe45")

# update(
#     filter={"_id": "6490fde7d3975ed3c7279dae"},
#     new_value={
#         "name": "Papel de baño UPDATE",
#         "category": "Blancos",
#         "quantity": 50,
#         "price": 15,
#     }
# )

# get(filter={"_id": "6490fd615aaeebe21135fe46"})

# insert([
#     {
#         "name": "Tenedor",
#         "category": "Cocina",
#         "quantity": 20,
#         "price": 5,
#     },
#     {
#         "name": "Cuchara",
#         "category": "Cocina",
#         "quantity": 10,
#         "price": 3,
#     },
#     {
#         "name": "Papel de baño",
#         "category": "Blancos",
#         "quantity": 50,
#         "price": 15,
#     },
# ])
