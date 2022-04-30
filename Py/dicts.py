d = {"a": 1, "b": [1, 2]}

d["a"]
d.get("a")

d["c"]
d.get("c", "return if cant find key")

d["a"] = 12
d["a"]

d.update({"a": 13})
d["a"]

d.__setitem__("c", 3)

d["d"] = 4

d

d["a"]

"a" in d
d.keys()
d.values()

d.get("b")
d.__getitem__("b")

list(d.keys())
list(d.keys())[2]

list(d.values())

for i in enumerate(d):
    print(i)
