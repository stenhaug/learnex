# https://realpython.com/introduction-to-python-generators/

def inf():
    num = 0
    while True:
        yield num
        num = num +1

gen_inf = inf()

next(gen_inf)
    
# generator comprehension is cool too
gen_comprehension = (num**2 for num in range(10000000000000000000000000000000000000))
next(gen_comprehension)
