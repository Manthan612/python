a = [1,2,3]
b=[5,6,7]
# add in end
a.append(4)
print(a)
# use for add list
a.extend(b)
print(a)
# insert it will add that value on index and didn't remove that index value
a.insert(0 , 0)
print(a)
#remove (list.remove(value))
a.remove(0)
print(a)
#remove value using index
a.pop(6)
print(a)