a = [9, 6, 29, 4, -1]

s=a.sort()
print(a)
# s = sorted(a)
# print(s)
a.reverse()
print(a)

b = [3, 5, 7, -100, 6, 1000, 4, 0]
print(min(b))
print(max(b))

# set
set1 = set(a)
set2 = set(b)
s3 = set1.intersection(set2)
print(list(s3))