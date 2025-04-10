'''
[expresion for itme in itrable if condition]
e- x*2
itme - range(1,10+1)
condition - if

'''
# sq = []
# for i in range(1,10+1):
#     sq.append(i**2)
# print(sq)

sq = [i ** 2 for i in range(1,10+1) if i % 2 == 0]
print(sq)