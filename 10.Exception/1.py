try:
    num1 = int(input('Enter the numebr1:'))
    num2 = int(input('Enter the numebr2:'))
    try:
        div = num1/num2
        print(f'Div:{div}')
    except ZeroDivisionError as e:
        print(f'Error: {e}')
        # print('You entered zero, which cannot be divided.')
except ValueError as e:
    print(f'Error: {e}')
    # print('The input you entered is a string, which is not supported.')