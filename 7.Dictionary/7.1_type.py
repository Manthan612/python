dict = {"name":"Manthan",
         '1': {'1':('manthan',20,98)},
         '2': {'2':('raj',19,33)},
         '3': {'3':('yash',19,64)},
         '4': {'4':('harsh',21,88)}
         }
print(dict)

dict2 = input('enter the key: ')
dict3 = input('enter the value: ')
dict[f'{dict2}'] = dict3
print(dict)