result = []

for x in range(10):
    result.append(x**2)

result

[x**2 for x in range(10)]

[x**2 for x in range(10) if x**2 >= 5]
