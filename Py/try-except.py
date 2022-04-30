# if no error, except doesn't happen
try:
    1 / 1
    print("TRY")
except:
    print("EXCEPT")

# if error, except does happen
try:
    1 / 0
    print("TRY")
except:
    print("EXCEPT")

# part of try can execute still until the error
try:
    print("TRY")
    1 / 0
except:
    print("EXCEPT")

# this is how it will usually go down
# FAIL
try:
    1 / 0
    print("TRY")
except:
    print("EXCEPT")
else:
    print("ELSE")
finally:
    print("FINALLY")

# SUCCEED
try:
    1 / 1
    print("TRY")
except:
    print("EXCEPT")
else:
    print("ELSE")
finally:
    print("FINALLY")
