import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,10)#[0,0.55,1.11,1.66,2.22,2.77,3.33,3.88,4.44,5]
y = np.exp(x)#[1,1.74,3.03,5.29,9.22,16.08,29.03,48.85,85.15,145.41]
plt.plot(x,y)
plt.show()