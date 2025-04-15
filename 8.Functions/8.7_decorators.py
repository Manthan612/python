'''
pizza - function
extra cheese - extra feture

main fun -> add fun
without change main function code
'''
def my_decorator(func):
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper

@my_decorator
def say_hello():
    print('hello')

say_hello()