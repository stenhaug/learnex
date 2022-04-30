# append just adds it to the end
# extend does basically the same thing with one level of flattening

base_append = ["a", "b"]
base_extend = ["a", "b"]
addtoit = ["c", ["d", "e"]]

base_append.append(addtoit)
base_append

base_extend.extend(addtoit)
base_extend

# see flattening clearly
b = ["a", "b"]
a = ["c"]

b.append(a)
b

b = ["a", "b"]
a = ["c"]

b.extend(a)
b

# doesnt matter if you're not adding a list
b = ["a", "b"]
a = "c"

b.append(a)
b

b = ["a", "b"]
a = ["c"]

b.extend(a)
b

# for more info on how to flatten a list see flatten-list.py
