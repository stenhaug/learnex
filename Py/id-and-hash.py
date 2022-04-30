# beyond the basic stuff with python page 111

# make ben it has an id
ben = []
id(ben)

# add food the id doesn't change 
ben.append("food")
id(ben)

# set emma to ben she has the same id
emma = ben
id(emma)

# add to emma ben changes because they have the same id
emma.append("bagel")
emma
ben

# setting ben to a new thing changes its id
id(ben)
ben = []
id(ben)

# this is the way to think about mutable vs. immutable data types
# mutable: list, dict, set, array
# immutable: integer, float, boolean, string, tuple

# immutable you can only change by changing the id
x = 1
id(x)
x = 2
id(x)

coord = (0, 0)
id(coord)
coord = (0, 1)
id(coord)


a = ["a"]
id(a)
a.extend(["b", "c"])
id(a)

b = ["a"]
id(b)
b.append(["b", "c"])
id(b)

# hash is about the value
# id is about the variable "bucket"
x = 12.5
y = 12.5

hash(x)
hash(y)

id(x)
id(y)

# this is why hash can be used to see if something is equal without knowing the thing
# example was someone you said hey i wrote this blogpost
# ill prove it in the future by giving you
# x such that
# hash(x) = 1152921504606846988
# the whole point is that hash^-1 isn't really a thing



