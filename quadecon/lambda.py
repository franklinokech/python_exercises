f = lambda x: x * x
my_list = [f(x) for x in range(10) if x % 2 == 0]
print(my_list)
