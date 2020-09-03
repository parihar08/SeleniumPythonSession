#input: "Welcome@#%^&to(*Python!^&*Programming"
#output: String contains special characters

#input: "Welcome to Python Programming"
#output: No special characters in string

import re

str = "Welcome@#%^&to(*Python!^&*Programming"
regex = re.compile('[!@#%c&_~{}:<>?$*&]')

if(regex.search(str) == None):
    print("No special characters in string")
else:
    print("String contains special characters")
