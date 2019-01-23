#!/usr/bin/env python
# coding: utf-8

# In[15]:


#original data
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]


# In[16]:


#profit = revenue - expenses


# In[17]:


import numpy as np
# converting original data lists into arrays
aRevenue = np.array(revenue)
aExpenses = np.array(expenses)

# creating named month reference for final reporting
aMonths = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#print(aRevenue)
#print(aExpenses)
#print(aMonths)


# In[18]:


#using the subtract method from NumPy to calculate << profits >>
np.subtract(aRevenue,aExpenses)


# In[19]:


#using the multiply method from NumPy to calculate *<< profit after tax >>
profitAfterTax = np.subtract(np.subtract(aRevenue,aExpenses),np.subtract(aRevenue,aExpenses) * 0.3)
profitAfterTax


# In[20]:


#using the divide method from NumPy to calculate << profit margin >>
profitMargin = (np.divide(profitAfterTax,aRevenue) * 100).round(2)
profitMargin


# In[21]:


np.max(profitMargin)
np.min(profitMargin)


# In[22]:


#finding best month

nBestMonth, = np.where(profitMargin == np.max(profitMargin))
aBestMonth = aMonths[nBestMonth[0]]
print(aBestMonth, '(',nBestMonth[0],')')


# In[23]:


#finding worst month

nWorstMonth, = np.where(profitMargin == np.min(profitMargin))
aWorstMonth = aMonths[nWorstMonth[0]]
print(aWorstMonth, '(',nWorstMonth[0],')')


# ---

# In[ ]:


#from now on nothing works...


# In[56]:


#finding good months
xGoodMonths = profitAfterTax[ profitAfterTax > profitAfterTax.mean() ] #xGoodMonths selects the values from aProfitTax which are higher than average
print(xGoodMonths)

nGoodMonths = np.dtype(np.isin(profitAfterTax, xGoodMonths), bool)
np.indices
print(nGoodMonths)
aGoodMonths = aMonths[nGoodMonths]

print(aGoodMonths)
#for i in range(0, len(xGoodMonths)):
 #   nGoodMonths.append()


# In[53]:


#nGoodMonths selects the index of the values from xGoodMonths
nGoodMonths, = np.where(np.isin(profitAfterTax, xGoodMonths))
print('NGood Months: ', nGoodMonths)
type(nGoodMonths)


# ---

# In[25]:


#reference code from https://stackoverflow.com/questions/3179106/python-select-subset-from-list-based-on-index-set


# In[31]:


#Using numpy:
property_a = np.array([545., 656., 5.4, 33.])
property_b = np.array([ 1.2,  1.3, 2.3, 0.3])
good_objects = [False, True, False, True]
good_indices = [0, 3]
property_asel = property_a[good_objects]
property_bsel = property_b[good_indices]


# In[34]:


#my own tests
print(property_asel)
print(property_bsel)
property_bsela = property_b[good_objects]
print('using A to select from B', property_bsela)


# In[ ]:


#Using a list comprehension and zip it:
property_a = [545., 656., 5.4, 33.]
property_b = [ 1.2,  1.3, 2.3, 0.3]
good_objects = [True, False, False, True]
good_indices = [0, 3]
property_asel = [x for x, y in zip(property_a, good_objects) if y]
property_bsel = [property_b[i] for i in good_indices]


# ---

# In[ ]:


#old code


# In[35]:


#finding good months
xGoodMonths = aProfitTax[ aProfitTax > aProfitMean ] #xGoodMonths selects the values from aProfitTax which are higher than average
#print(nGoodMonths)
#nGoodMonths = np.array[]
nGoodMonths, = np.where(np.isin(aProfitTax, xGoodMonths)) #nGoodMonths selects the index of the values from xGoodMonths
print('NGood Months: ', nGoodMonths)
type(nGoodMonths)


# In[ ]:





# In[54]:


aGoodMonths = aMonths[nGoodMonths]
#print(np.where(aGoodMonths))
print('aGoodMonths', aGoodMonths) #ainda acha só o primeiro...


# In[82]:


#finding bad months
nBadMonths = aProfitTax[ aProfitTax < aProfitMean ]
print(nBadMonths)


# In[42]:


#finding best month

nBestMonth, = np.where(aProfitMargin == aProfitMargin.max())
print(nBestMonth[0])
aBestMonth = aMonths[nBestMonth[0]]
print(aBestMonth)


# In[43]:


#finding worst month
nWorstMonth, = np.where(aProfitMargin == aProfitMargin.min())
print(nWorstMonth[0])
aWorstMonth = aMonths[nWorstMonth[0]]
print(aWorstMonth)


# In[ ]:




