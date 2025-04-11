'''
def name(f_name,l_name):
    fullname = f'{f_name} {l_name}'    
    print(fullname)
    # it print value but in some case when we grab value from user
    # which we wanna use in backend we use return
'''
def name(f_name,l_name):
    fullname = f'{f_name} {l_name}'
    return fullname
get_name = name('jethalal','gada')
print(get_name.title())