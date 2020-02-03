n = input('Enter a number range\n')
n = int(n)
sum = 0
avg = 0

for num in range(0, n + 1, 1):
    sum = sum + num
    avg = sum / n
print('The avg of first ' + str(n) + ' is ' + str(avg))
