# big question of when to use assert vs. raise
# https://stackoverflow.com/questions/40182944/whats-the-difference-between-raise-try-and-assert
# assert when want to STOP
# raise when want to have the opportunity to handle it ("raise it to the next level up" which can hopefully handle it)

# https://realpython.com/python-assert-statement/

# nothing happens
assert 1 > 0

# throws an error
assert 1 < 0, f"first number should be greater than second number"

# more generally think of assert as a function
# which takes two arguments — the statement, the error message
num1 = 100
num2 = 50

# BUT this does not work
assert(
    num1 < num2,
    f"{num1} is greater than {num2}"
)

# If you want multiple lines, need to do this
assert num1 < num2, \
    f"{num1} is greater than {num2}"

# This also works
assert \
    num1 < num2, \
        f"{num1} is greater than {num2}"

# (in general \ lets you go to the next line without there being meaning to the line break)

# all and any can be helpful
assert all([True, False])
assert any([True, False])

# can do the same thing with raising an exception
# (this also reads more naturally to me)
if num1 > num2:
    raise Exception(f"{num1} is greater than {num2}")

# see try-except.py for how to get around this
