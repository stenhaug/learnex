import os
os.getcwd()

# so im in some other script

# in R I'm used to running source to execute code

# this can be done here by doing basically this
exec(open("Py/ifnameequalsmain/file_two.py").read())
filetwof(0)

# but the pythonic way to do it is this
sys.path.append("Py/ifnameequalsmain")
import file_two
file_two.filetwof(1)
