dict3 = {
    "key1":"value1",
    "key2":"value2",
}

dict4={}

for key,value in dict3.items():
    dict4[value] = key

print(dict4)

original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)