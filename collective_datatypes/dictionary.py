name_dict = {'John': 44, 'Wick': 33, 'Paul': 55}
# print(name_dict)

del name_dict['Paul']
# print(name_dict)

# print(len(name_dict))
# print(name_dict.get('John'))
# print(name_dict.get('Paul', "Not defined"))

# print(name_dict)
# print(name_dict.popitem())
# print(name_dict)
# name_dict.clear()

# for loop in dic
for key, value in name_dict.items():
    print(key, value)

for key in name_dict.keys():
    print(key, name_dict[key])

while key in name_dict.keys():
    print(key, name_dict[key])
