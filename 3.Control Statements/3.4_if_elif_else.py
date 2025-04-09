x = int(input('enter the value of x:'))
y = int(input('enter the value of y:'))

z = input('Choose an operator (+, -, *, /): ')

if z == '+':
    print(f'addition of x & y ={x+y}')


elif z == '-':
    print(f'subtraction of x & y ={x-y}')

elif z == '*':
    print(f'multiplication of x & y ={x*y}')


elif z == '/':
    print(f'division of x & y ={x/y}')

else:
    print("Invalid Choice")