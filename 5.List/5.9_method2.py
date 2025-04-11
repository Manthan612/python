a = [1,2,2,3,3,4,4,4,5,5,5,6]

# index
b = a.index(4)
print(f'index: {b}')
# count
c = a.count(5)
print(f'count: {c}')

del a[4:9]
print(a)
# deleted variable can't access

d = a.clear()
print(d)