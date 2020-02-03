# # defination of function
# def hello_func():
#     print('Hello word...')


# hello_func()
# hello_func()
# hello_func()
# hello_func()

# passing params
def hello_func(greeting='Anonymous', name='You'):
    return '{}, {}'.format(greeting, name)


print(hello_func().upper())
