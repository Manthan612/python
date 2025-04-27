try:
    num = int(input('Enter the numebr:'))
    result = 10/num
    print(f'result: {result}')
except ZeroDivisionError as e:
    print(f'Error: {e}')
    # print('You entered zero, which cannot be divided.')
except ValueError as e:
    print(f'Error: {e}')
    # print('The input you entered is a string, which is not supported.')