#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = (lambda x:x**2)(3)
print(a)


# In[1]:


mutlu = lambda x,y : (x+y) /2
print(mutlu(3,5))


# In[8]:


kare = lambda x :x**2
kare(4)


# In[7]:


ortalama = lambda x, y: (x + y)/ 2
ortalama(3,7)


# In[4]:


tersten = lambda x : x[ ::-1]
tersten("mutluyum")


# In[6]:


avarage = lambda x,y: (x+y)/2
avarage(3,5)


# In[19]:


list = []
list_not = []

for j in range(2,100) :    
    for i in range(2,j):  
        if (j %i ) == 0:
            list_not.append(j)
            break
    else: 
        list.append(j)
        

print(list_not)


# In[33]:




for i in range(1,100):
    if ( i%3 ) == 0:
        print("Fizz")
    elif (i%5 ) == 0:
        print("Buzz")
    elif (i % 5)==0 and (i%3)==0:
        print("FizzBuzz")
    else :
        print(i)
    
    


# In[ ]:





# In[ ]:




