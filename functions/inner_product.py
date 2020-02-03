# given two tuples, x_vals and y_vals of equal lenght, compute inner prod
x_vals = tuple([10, 20, 30])
y_vals = tuple([40, 50, 60])

dot_prod = sum([x ** y for x, y in zip(x_vals, y_vals)])
print(dot_prod)
