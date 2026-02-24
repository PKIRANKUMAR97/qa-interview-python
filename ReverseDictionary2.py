original = {"a": 1, "b": 1, "c": 2,"d": 3, "e": 4, "f": 3, "g": 6, "h": 6}

reversed_dict = {}

for key, value in original.items():
    if value not in reversed_dict:
        reversed_dict[value] = [key]
    else :
        reversed_dict[value].append(key)

print(reversed_dict)