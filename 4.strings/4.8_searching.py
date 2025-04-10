# find = (sub) it only fint one charactor from string first charactor and first index it return
text = 'python programming'
print(text.find('p'))

# replace
print(text.replace('python','java'))

#split 'it will exclude that word which you mension and print that sentance after splite with that charactor
s= text.split("o")
print(f'After split: {s}')

# Join use for join the string
j = ('o').join(s)
print(j)

#start with
print(text.startswith('p'))

# ends with
print(text.endswith('g'))