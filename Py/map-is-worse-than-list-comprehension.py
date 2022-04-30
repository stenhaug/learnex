mylist = ["emma", "ben", "kalin", "z"]
rev = lambda x: -len(x)

# use map to create the map object (this is more generally an iterator)
map_object_which_is_an_iterator = map(rev, mylist)
list(map_object_which_is_an_iterator)

# can also get in there using a list comprehension
# (have to recreate the iterator because its used up)
map_object_which_is_an_iterator = map(rev, mylist)
[x for x in map_object_which_is_an_iterator]

# but list comprehension is just way more general and way more awesome
# could have done this the whole time
# gosh that's sweet
[rev(x) for x in mylist]
