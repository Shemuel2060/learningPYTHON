# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 07:30:26 2024

@author: Shemuel
"""

file = open("names.txt", "a") # open a file for writing to - appending data
while True:
    name = input("Enter name: ")
    if(name==""):
        break
    file.write(f"{name}\n")
file.close()