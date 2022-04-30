######################## essence ###############################
# just like in R, we can use global variables in a function
x = 1
def f():
    print(x)
f()

# unlike R, some object types can be sneakly globally changed in a function
# https://miro.medium.com/max/1316/1*uFlTNY4W3czywyU18zxl8w.png
a_int = 1; a_list = [1]
def g():
    a_int = 2
    a_list[0] = 2
g(); a_int; a_list

# if i want to change something immutable, use the global function
a_int = 1
def h():
    global a_int
    a_int = 2
h(); a_int

# if i want to avoid changing something mutable, use a deepcopy
import copy
a_list = [1]
def g(a_list):
    a_list = copy.deepcopy(a_list)
    a_list[0] = 2
    return a_list
g(a_list); a_list

######################## thinking ###############################
# int is immutable
a = 1

def func(x):
    x = 2

func(a)
a

# list is mutable
a = [1]
def func2(x):
    x[0] = 2

func2(a)
a

# tuple doesn't even get assignment
a = (1, 2)

def func3(x):
    x[0] = 2

func3(a)
a

# global gets around it and makes it clear we want the whole thing
a = 1

def func(x):
    global a
    a = 2
    x = 2

func(a)
a

# list is mutable but can get around this by making a copy of x 
# so when setting something it does it to the copy
import copy

a = [1]
def func2(x):
    x = copy.deepcopy(x)
    x[0] = 2

func2(a)
a

# just like in R, you can use global variables
a = 1
def func2(x):
    print(a)
    x = x + a
    return(x)

func2(5)
a
