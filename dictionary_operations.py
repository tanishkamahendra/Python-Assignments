dict1 = {"name": "Tanishka", "age": 18, "city": "Pune"}
print("Dictionary:", dict1)
print("Name:", dict1["name"])

dict1["age"] = 19
dict1["course"] = "CS"
print("After update:", dict1)

dict1.pop("city")
print("After removing element:", dict1)

dict2 = {"grade": "A", "year": 1}
dict1.update(dict2)

print("Merged Dictionary:", dict1)