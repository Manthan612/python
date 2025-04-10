"""
in 
not in
"""
list = [1,2,3,4,5]
check = int(input('enter the number you wanna check: '))
if check in list:
    print(f'{check} is present in list')
else:
    print(f"{check} isn't present in list")