# my method 0
# my_even = []
# for i in range(100):
#     if i % 2 == 0:
#         my_even.append(i)
# print(len(my_even))

# my method 1
my_even = sum(x % 2 != 0 for x in range(100))
print(my_even)

# my method 2
my_sum_even = sum([x % 2 != 0 for x in range(100)])
print(my_sum_even)

print(len([x for x in range(100) if x % 2 == 0]))
