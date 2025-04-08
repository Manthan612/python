x = int(input('enter the first value:'))
y = int(input('enter the second value:'))

z = input('Choose an operator (+, -, *, /): ')

if z == '+':
    print(x+y)

elif z == '-':
    print(x-y)

elif z == '*':
    print(x*y)

elif z == '/':
    print(x/y)

else:
    print("Invalid Choice")