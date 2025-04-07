import math
print(math.floor(4.23333))

# 'from' keyword is used when we have to import a particular function, or set of functions

from math import sqrt, pi
print(pi)
print(sqrt(4))

# similarly if we write the * we can get the all the functions

from math import *

# likewise we can change the names of the packages we import as :
import math as m 

# similarly we can do for the methods as :
from math import sqrt as s, pi as p
print(p)