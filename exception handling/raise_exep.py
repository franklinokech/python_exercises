try:
    my_file = open('test.txt')
    my_file.writable()
    my_file.write('The Best A')
except Exception as e:
    print(e)
else:
    pass
finally:
    pass
