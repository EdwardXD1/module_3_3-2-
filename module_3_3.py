def print_params(a = 2, b = 'string', c = False):
    print(a, b, c)
print_params(3, 'yo', True)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [1, 'LOL', True]
values_dict = {'a':7, 'b':'omg', 'c':False}
print_params(*values_list)
print_params(**values_dict)


value_list2 = [1.11, "wow"]
print_params(*value_list2, 42)