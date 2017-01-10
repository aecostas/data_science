import numpy
import math
from pandas import *

a = pandas.Series([1, 2, float('nan') , 4])
b = pandas.Series([1, 2, float('nan') , 4])

# artesanal mechanism
nan_pos = numpy.argwhere(numpy.isnan(a))
for i in nan_pos:
    a[i] = 100
    
# pandas mechanism
b = b.fillna(200)

print a
print b
