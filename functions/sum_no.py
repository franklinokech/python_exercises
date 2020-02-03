n = input('Enter Some Number\n')
n = int(n)

sum = 0
for num in range(0, n + 1, 1):
    sum = sum + num
print('Sum of the first ' + str(n) + ' is ' + str(sum))
