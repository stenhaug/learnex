import sys
sys.path.append("Py")

# import the pkg
import pkgtoshowinit as p

# can access to from init
p.alist

# can access mod1 because its in init
p.mod1
p.mod1.fmod1(0)

# but can NOT access mod2
p.mod2
p.mod2.fmod2(0)

# can if i do this
from pkgtoshowinit import mod2
p.mod2
p.mod2.fmod2(0)

mod2
mod2.fmod2(0)

# alternatively can do the import * thing
from pkgtoshowinit import *
alist
mod1
mod1.fmod1(0)
mod2
mod1.fmod1(0)
