# should always return a positive number

# assert
def f_assert(num1, num2):
    assert num1 < num2, f"{num1} is greater than {num2}"
    return num2 - num1
    
f_assert(1, 2)
f_assert(1, 0)

try:
    f_assert(1, 0)
except AssertionError as error: # notice AssertionError
    f"the error is {error}"

# except
def f_except(num1, num2):
    if num1 > num2:
        raise Exception(f"{num1} is greater than {num2}")
    
    return num2 - num1
    
f_except(1, 2)
f_except(1, 0)

try:
    f_except(1, 0)
except Exception as error: # notice Exception
    f"the error is {error}"
