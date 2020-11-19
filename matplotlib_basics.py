#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()


# In[7]:


plt.plot(squares, linewidth=5)

#Set chart title and label axes
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', labelsize=14)
plt.show()


# In[ ]:


#### input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth=5)
#Set chart title and label axes
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', labelsize=14)
plt.show()


# In[ ]:




