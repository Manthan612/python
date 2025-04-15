'''
ondemand create value
yield keyword
'''

# def count_down(num):
#     while num > 0:
#         yield num
#         num-=1

# for number in count_down(5):
#     print(number)
def gen():
    for i in range(3):
        yield i

g = gen()
print(next(g))  # 0
print(next(g))  # 1
