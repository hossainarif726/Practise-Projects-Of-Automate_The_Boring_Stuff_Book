#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def collatz(number):
    while number != 1:
        if number%2==0:
            number = number // 2
            print(number)
        else:
            number = (3 * number) + 1
            print(number)
try:
    collatz(int(input()))
        
except ValueError:
    print('ERROR : You must enter an integer')
    collatz(int(input()))

