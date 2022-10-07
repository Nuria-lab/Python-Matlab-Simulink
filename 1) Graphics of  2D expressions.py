# graphics on python

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10,0.1)  #create the table for certain independent variable
y= np.sqrt(x)  

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphics')
plt.show()