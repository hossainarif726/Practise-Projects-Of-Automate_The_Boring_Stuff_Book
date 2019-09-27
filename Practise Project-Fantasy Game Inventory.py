#!/usr/bin/env python
# coding: utf-8

# In[7]:


def display_inventory(inventory):
    print('INVENTORY:')
    total = 0
    for k,v in inventory.items():
        print(v,k)
        total += v
    print('Total Number Of Items:',total)

inv = {'arrow':12,
       'gold coin':42,
       'rope':1,
       'torch':6,
       'dagger':1}

display_inventory(inv)

def add_inventory(inventory,new_inventory):
    
    for i in new_inventory:
        if i == 'arrow':
            inventory['arrow'] = inventory['arrow']+1
        elif i == 'gold coin':
            inventory['gold coin'] = inventory['gold coin']+1
        elif i == 'rope':
            inventory['rope'] = inventory['rope']+1
        elif i == 'torch':
            inventory['torch'] = inventory['torch']+1
        elif i == 'dagger':
            inventory['dagger'] = inventory['dagger']+1
    return display_inventory(inventory)
            
loot = ['rope','torch','torch','dagger','arrow','arrow','arrow']
print('\nAfter Loot ',end ='')
add_inventory(inv,loot)


# In[ ]:




