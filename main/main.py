import json


with open("operations.json", 'r', encoding="utf-8") as file:
    raw_json = file.read()
    all_operations = json.loads(raw_json)
def operations_data():
    pass

print(all_operations)
