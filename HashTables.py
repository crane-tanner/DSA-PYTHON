# Known as Dictionaries in Python
# Dictionaries are key-value pair data structure

user = {"first_name": "Jerome",
        "middle_name": "Michael",
        "last_name": "Sullivan",
        "age": 23}

print(user["middle_name"])

user["date_of_birth"] = "2/6/1990"
# adding and deleting new key-value pair is O(1) generally

del user["date_of_birth"]
user.pop("last_name")
# two ways to delete

for k in user.keys():
    print(k)
for _ in user.items():
    print(_)

    # One downside is dictionaries require more memory 
