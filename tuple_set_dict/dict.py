# key-value pair

user_data = {
    "user_123": {"name": "Alice", "email":"alice@example.com"},
    "user_456": {"name": "Mike", "email":"mike@example.com"}
}

# print(user_data.values())

# for k, v in user_data.items():
#     print(k, v)


for k, v in user_data.items():
    for k, v in v.items():
        print(k, v)
