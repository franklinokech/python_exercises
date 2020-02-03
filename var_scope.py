# define a global variable
x = 'Global_x'


def test_scope():
    y = 'Local_y'
    print(y)


test_scope()
