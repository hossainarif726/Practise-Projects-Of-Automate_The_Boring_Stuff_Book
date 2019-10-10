#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#regex for phone number

import pyperclip,re

phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?              # area code
                        (\s|-|\.)?                      # separator
                        (\d{3})                         # first three digit
                        (\s|-|\.)                       # separator
                        (\d{4})                         # last four digit
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
                        )''', re.VERBOSE)

#regex for email address

emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+        # username
                        @                        # @symbol
                        [a-zA-Z0-9.-]+           # domain name
                        (\.[a-zA-Z]{2,4})        # dot-anything
                        )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    
    matches.append(phoneNum)
    
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied To Clipboard:\n')
    print('\n'.join(matches))
    
else:
    print('No Phone Number Or Email Address Found')


# In[ ]:




