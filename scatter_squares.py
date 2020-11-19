#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


plt.scatter(2,4)
plt.show()


# In[5]:


#plt.scatter(2, 4, s = 200)
#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#plt.scatter(x_values, y_values, c='red', edgecolor=None, s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor=None, s=40)

#Set chart title and label axes
plt.title("Square numbers", fontsize = 24)
plt.xlabel("Value", fontsize =14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=10)

#Set the range for each axis
plt.axis([0, 1100, 0, 1100000])

plt.show()

#Saving the plots automatically
plt.savefig('squares_plot.png', bbox_inches='tight')


# In[ ]:




