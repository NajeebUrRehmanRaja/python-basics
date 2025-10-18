print('importing mymodule')

myvar = 'value'

def find_index(to_search, target):
    for i, item in enumerate(to_search):
        if item == target:
            return i
    return -1