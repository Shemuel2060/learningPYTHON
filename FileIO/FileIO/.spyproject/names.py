# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 07:30:26 2024

@author: Shemuel
"""

"""
OPENING AND WRITING TO A FILE v1.
 
In this version we explicitly close the file at the end. 
This is okay, but may be easily forgotten especially with 
large code. v2. presents a better approach.
"""
# file = open("names.txt", "a") # open a file for writing to - appending data
# while True:
#     name = input("Enter name: ")
#     if(name==""):
#         break
#     file.write(f"{name}\n")
# file.close()



"""
OPENING AND WRITING TO A FILE v2.

In this version, we do not explicitly call the close method on 
the file, but simply use the with keyword when opening the file.
v2. 
"""
with open("names_v2.txt", "a") as file:
    while True:
        name = input("Enter a name: ")
        if(name==""):
            break
        file.write(f"{name}\n")
        





