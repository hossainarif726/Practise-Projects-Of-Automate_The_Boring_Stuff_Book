#!/usr/bin/env python
# coding: utf-8

# In[6]:


lis = [20,12,23]
lis1 = []
for i in range(len(lis)-1):
    lis1.append(str(lis[i]))
print(', '.join(lis1)+', and '+str(lis[-1]))


# In[7]:


lis = 
lis1 = []
for i in range(len(lis)-1):
    lis1.append(str(lis[i]))
print(', '.join(lis1)+', and '+str(lis[-1]))


# In[9]:


def list_thing(words):
    if len(words) == 1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])
list_thing(['apples','banans','tofu','cats'])


# In[ ]:




