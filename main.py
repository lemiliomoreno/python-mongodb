from pymongo import MongoClient


MONGODB_URL = "mongodb://academia:academia@localhost:27017"


def get_db():
    mongodb_client = MongoClient(MONGODB_URL)

    return mongodb_client["academia"]


def insert(items: list):
    database = get_db()

    for item in items:
        database.inventory.insert_one(item)


def get(filter: dict):
    database = get_db()

    for item in database.inventory.find(filter):
        print(item)


get(filter={"category": "Blancos"})

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
