# https://stackoverflow.com/questions/22646463/and-boolean-vs-bitwise-why-difference-in-behavior-with-lists-vs-nump

# • If you have vectors of truth values that you wish to combine, use numpy with &.
# • If you are not dealing with arrays and are not performing math manipulations of integers, you probably want and.

# https://www.geeksforgeeks.org/difference-between-and-and-in-python/#:~:text=and%20is%20a%20Logical%20AND,otherwise%20True%20when%20using%20logically.

# and is a Logical AND that returns True if both the operands are true 
# ‘&’ is a bitwise operator in Python that acts on bits and performs bit by bit operation.

True and True
True or False

# https://realpython.com/python-and-operator/
# weirddness i don't totally get
True and []
False and []

2 < 3 and 4 < 5
3 < 2 and 4 < 5

5 or 3
5 and 3
