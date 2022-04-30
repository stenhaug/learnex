x = {'a': 4, 'b': -3, 'c': 100, 'd': 1}

# gives us lists
x.keys()
x.items()

# sort
y = sorted(x.items(), key = lambda x: x[1])

# but what do we have
type(x)
type(y)
type(y[0])
