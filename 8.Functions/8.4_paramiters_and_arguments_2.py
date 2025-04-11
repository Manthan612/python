'''
1- positional args
keywprd args
default args
'''
# default set if user forgot to mension value it will reflect preamiter value
# def greet(city='mumbai',name='manthan'): 
def greet(name,city):
    print(f'{name} from {city} '.title())

greet(city='mumbai',name='manthan')
# greet('manthan','mumbai') #right way
# greet('mumbai','manthan') #wrong way