def count_even(n):
    return sum([x % 2 == 0 for x in range(n)])


print(count_even(4))
