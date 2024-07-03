def print_params(a, b, c):
    print(a, b, c)
a = 1
b = 'string'
c = True

my_lst = [1, 2, 3]
print_params(1, 25, my_lst)

def print_params(a, b, c):
    print(a, b, c)
values_list = [2, True, 'Python']
values_dict = {'a': 7, 'b': False, 'c': 'string'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [100, 'note']
print_params(*values_list_2, 42)