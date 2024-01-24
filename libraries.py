# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 07:29:11 2024

@author: Shemuel
"""

#######################################
### LIBRARIES

"""
Modules - or libraries 
--> code defined to be reused elsewhere. Improves reusability of code.
--> can define own modules/libraries.
--> to use modules, import them or import specific functions from them

"""
#######################################

import random
# can import specific functions i.e. 
# from random import choice

# random choosing
names = ["Berith", "Azurah", "Bethel", "Moriah"]
chosen = random.choice(names)
# print("Chosen Name: ", chosen)

# random shuffling
random.shuffle(names) # modifies the list
# for name in names:
#     print(name)
    

# getting random integers
n = random.randint(1,10) # 1 and 10 inclusive
# print(n)


###########################################
### COMMAND-LINE ARGUMENTS
###########################################


# import sys

# print(sys.argv[0]) # name of the file, libraries.py
# print("My name is: ", sys.argv[1])


# # for several arguments on the CL
# print("============== MORE THAN 2 ARGUMENTS=====================")
# if len(sys.argv) < 2:
#     print("Too few arguments")
# for arg in sys.argv[1:]: # start from the first argument
#     print(arg)


#######################################
### PACKAGES

"""
INSTALL packages using pip - python package manager
Then IMPORT them into your program and use them similar
way as using libraries.
"""
#######################################

## cowsay

########
## APIs - Application Programming Interfaces
"""
Third-party services. We write code to talk to them, get
data from them and use that data. We can define our own
APIs - basic ones are actually the functions we write.
"""

# import cowsay


# cowsay.cow("hello")



########################
## MAKING http/ https requests like in a browser
########################

import sys
import json # to format json objects properly

import requests

if len(sys.argv) !=2: # ensure name of singer, band passed.
    sys.exit();

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])

wez = response.json()

format_wez = json.dumps(wez, indent=2)
# print(format_wez)


for result in wez["results"]:
    print(result["collectionName"],":",result["trackName"])





























