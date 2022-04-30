# set the goal to find "ben" from this dict
A = [
    {"name": "alex", "score": 12},
    {"name": "ben", "score": 24},
    {"name": "carry", "score": 99}
]

# print to see whats up
for a in A:
    a

# loopy way
for a in A:
    if a["name"] == "ben":
        a["score"]

# list comprehension way
[a["score"] for a in A if a["name"] == "ben"][0]

# filter way
# function, list to apply it to
filter(lambda x: x["name"] == "ben", A)
list(filter(lambda x: x["name"] == "ben", A))
next(filter(lambda x: x["name"] == "ben", A))
