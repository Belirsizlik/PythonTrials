
# coding: utf-8

## Harmonik Osilator Psi(0)

# In[14]:

from numpy import*
import matplotlib.pyplot as plt

x=arange(-5,5,.1)
y=sqrt(sqrt(10./math.pi))*e**(-x**2/2)
grph1=plt.plot(x,y)
plt.grid(True)
plt.title("Psi0")
plt.show()


# In[ ]:



