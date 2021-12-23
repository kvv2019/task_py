import csv
import json

DATA_USERS = "data/users.json"
DATA_BOOKS = "data/books.csv"
DATA_RESULTS = "result.json"

result = []

with open(DATA_USERS, "r") as read_json:
    users = json.load(read_json)
    for user in users:
        result.append({"name": user['name'],
                       "gender": user['gender'],
                       "address": user['address'],
                       "age": int(user['age']),
                       "books": []})

count = 0
count_users = len(result)

with open(DATA_BOOKS, encoding='utf-8') as read_file:
    books = csv.reader(read_file, delimiter=",")
    for book in books:
        if count != 0:  # убираем заголовок
            result[(count - 1) % count_users]['books'].append({"title": book[0],
                                                               "author": book[1],
                                                               "pages": int(book[3]),
                                                               "genre": book[2]})
        count += 1

with open(DATA_RESULTS, "w") as write_file:
    json.dump(result, write_file)
