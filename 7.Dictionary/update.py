my_dict = {
    'language':'python','version':'3.11'
}
print(f'Before Update: {my_dict}')

my_dict['version'] = 3.12
print(f'After Update: {my_dict}')

del my_dict['version']
print(my_dict)