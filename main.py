from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.my_database
print("Подключение успешно выполнено!")

collection = db.my_collection

new_document = {
    "name": "Dastan",
    "age": 21,
    "city": "Almaty"
}
collection.insert_one(new_document)
print("Документ вставлен.")

documents = [
    {"name": "Aigerim", "age": 28, "city": "Nur-Sultan"},
    {"name": "Dina", "age": 22, "city": "Shymkent"}
]
collection.insert_many(documents)
print("Несколько документов вставлены.")

print("Все документы в коллекции:")
for document in collection.find():
    print(document)

# Чтение по критерию
person = collection.find_one({"name": "Ali"})
print("Документ с именем 'Ali':", person)

# 5. Обновление данных
# Обновление одного документа
query = {"name": "Ali"}
new_values = {"$set": {"age": 26}}
collection.update_one(query, new_values)
print("Документ обновлен.")

# Обновление нескольких документов
query = {"city": "Almaty"}
new_values = {"$set": {"city": "Aktau"}}
collection.update_many(query, new_values)
