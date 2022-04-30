# i have some function that takes three arguments

# feed list or dict to a regular function
def f(x, y, z):
    return x + y - z

f(1, 2, 3)

f(*[1, 2, 3])

f(**{"x": 3, "z": 2, "y": 1})

# can simply show it with print
print(*[1, 2, 3])

# position-based function
def g(*args):
    return args

g(1, 2, 3)

# keyword-based function (ie named)
def h(**kwargs):
    return kwargs

h(z = 1, y = 2, x = 3)

# combine it all

**[1, 2, 3]
