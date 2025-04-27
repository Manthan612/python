'''
one name, many forms

->i can run fast
->car run on petrol
->this program can't run
'''

# print(len('pytohn'))
# print(len((1,2,3)))
# print(len({'a':1,'b':2,'c':3}))

class Bike():
    def speed(self):
        print('normal top speed of bikes 109km/h')


class Aprilia457(Bike):
    def speed(self):
        print('Aprilia457 Top speed 190km/h')

class Duke390(Bike):
    def speed(self):
        print('Duke390 Top speed 167km/h')

b1 = Aprilia457()
b2 = Duke390()
b1.speed()
b2.speed()