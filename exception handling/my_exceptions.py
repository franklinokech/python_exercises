

try:
    my_file = open('test.txt')
except FileNotFoundError as e:
    print(e)
else:
    print('Reading File')
    print(my_file.read())
    my_file.close()
finally:
    print('Little house keeping')
