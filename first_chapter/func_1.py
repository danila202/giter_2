
def func_test(string = 'test',number:int = 3):
    lst = [string.upper() if i == 1 else string for i in range(number)]
    return ''.join(lst)


b = func_test

