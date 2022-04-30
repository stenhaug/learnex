# https://realpython.com/python-functional-programming/

mylist = ["emma", "ben", "kalin", "z"]

# default is alphabetical
sorted(mylist)

# can pass a function to sort using (reminds me of fct_reorder)
sorted(mylist, key = len)

# can define a custom function if i need to 
def reverse(x): 
    return -len(x)
    
sorted(mylist, key = reverse)

# but wait can't i do lambda function
lambda_reverse = lambda x: -len(x)

sorted(mylist, key = lambda_reverse)

# or just put the lambda right in there
sorted(mylist, key = lambda x: -len(x))
