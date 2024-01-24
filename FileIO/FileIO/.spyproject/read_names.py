# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 08:41:21 2024

@author: Shemuel
"""

"""
To read names, we specify "r" optionally. ALternatively, if
we do not specify any specifier, it automates to reading. 
"""

"""
v1. 

We iterate through the file and read the names as is. No
modifications or further processing done on the names. 
"""
# with open('names_v2.txt') as file:
#     for name in file:
#         print(name.rstrip())



"""
v2. Sort the names list

1. We create an empty list
2. We populate the list with the names
3. We print out the sorted version of the list in ascending order
"""

# names = [] # empty list to contain the names
# with open("names_v2.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# # sort the names list and print them on the console
# for name in sorted(names):
#     print(name)


"""
v3. Sort the file content

1. We create an empty list
2. We populate the list with the names
3. We print out the sorted version of the list in ascending order
"""

# names = [] # empty list to contain the names
# with open("names_v2.txt") as file:
#     for line in sorted(file):
#         # --- further processing of the names here---
#         names.append(line.rstrip())

# # --- further processing of the names here---

# # sort the names list and print them on the console
# for name in names:
#     print(name)  
    
"""
v4. Sort in descending order.

1. We create an empty list
2. We populate the list with the names
3. We print out the sorted version of the list in descending order
"""

names = [] # empty list to contain the names
with open("names_v2.txt") as file:
    for line in sorted(file, reverse=True):
        # --- further processing of the names here---
        names.append(line.rstrip())

# --- further processing of the names here---

# sort the names list and print them on the console
for name in names:
    print(name) 
    
    
    
    
    
    