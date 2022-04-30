# https://stackoverflow.com/questions/12377473/write-versus-writelines-and-concatenated-strings/12377575#12377575
# http://satishpython.blogspot.com/2015/01/difference-between-write-and-writelines.html

import sys
import os 
os.getcwd()

with open("data/cars.txt", "r") as file:
    file.read()

with open("data/cars.txt", "r") as file:
    file.readlines()

with open("data/cars1.txt", "w") as file:
    file.writelines(["a", "b", "c"])

with open("data/cars2.txt", "w") as file:
    file.write("\n".join(["a", "b", "c"]))

with open("data/cars3.txt", "w") as file:
    file.write("dhfklasdhflkashdnf")
