def my_func(n):
    return lambda x: x * n


my_doubler = my_func(2)
print(my_doubler(11))
