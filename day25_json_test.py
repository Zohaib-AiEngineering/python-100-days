##json loads()
import json
json_text = '{ "name": "Ahmad", "age": 22, "city": "multan"}'
data = json.loads(json_text)


print (data)
print(data["name"])
print(data["age"])
print(data["city"])



# json dumps()
data = {
    "name": "Ahmad",
    "age": 22,
    "city": "Multan"
}
json_text = json.dumps(data)
print(json_text)
print(type(data))
print(type(json_text))