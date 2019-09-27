#!/usr/bin/env python
# coding: utf-8

# In[3]:


tabledata = [['apples','oranges','cherries','bananas'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]
fruits = tabledata[0]
names = tabledata[1]
animals = tabledata[2]

def bigword(lis):
    c = 0
    for i in range(len(lis)):
        if c < len(lis[i]):
            c = len(lis[i])
    return c

c1 = bigword(fruits)
c2 = bigword(names)+1
c3 = bigword(animals)+1
print(fruits[0].rjust(c1)+names[0].rjust(c2)+animals[0].rjust(c3))
print(fruits[1].rjust(c1)+names[1].rjust(c2)+animals[1].rjust(c3))
print(fruits[2].rjust(c1)+names[2].rjust(c2)+animals[2].rjust(c3))
print(fruits[3].rjust(c1)+names[3].rjust(c2)+animals[3].rjust(c3))

