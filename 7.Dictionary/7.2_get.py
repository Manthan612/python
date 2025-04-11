profile = {
    'name':'raj','age':23,'salary':25000.00
}

age = profile.get('age','not found')
print(age)
# age = profile.get('if key is wrong','use default value')
age = profile.get('age1','not found')
print(age)

keys = profile.keys()
print(list(keys))

Value = profile.values()
print(list(Value))

all_item = profile.items()
print(list(all_item))

# pop is use for remove 1 pair of key & Value
# pop = profile.pop('age','not found')
# print(pop)
# print(profile)

# popitme by default remove last pair of key and value
# pop = profile.popitem()
# print(pop)
# print(profile)

# use for clear tuple
# clr = profile.clear()
# print(profile)