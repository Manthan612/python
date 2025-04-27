try:
    file = open('C:/Users/Admin/OneDrive/Desktop/python/10.Exception/Exception handling.txt','r')
    content = file.read()
    print(content)

except FileNotFoundError as e:
    print(f'Error: {e}')

finally:
    file.close()
    print('file closed')