def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
print_params()
print_params(7, 8, 9)

values_list = [5, 6, 7]
values_dict = {"a": True, "b": 10, "c": 12}
print_params(*values_list)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print_params(**values_dict)
