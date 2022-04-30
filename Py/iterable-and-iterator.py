# iterable is something that can be turned into an iterator
# range creates an iterable

# iterator is something that you can iterate over
# iter creates an iterator

# whats happening here is python turns range3 into an iterator and then does the next thing
for x in range(3):
    x

# we can do this manually
iterator = iter(range(3))
next(iterator)

for x in iterator:
    x
