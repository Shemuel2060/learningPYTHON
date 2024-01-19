# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 07:08:29 2024

@author: Shemuel
"""

"""
v1. Using writer
Write to csv files. Can be viewed and used in excel
"""
import csv

title = input("Book Title: ")
author = input("Book Author: ")


# with open("books.csv", "a", newline='') as file:
#    writer = csv.writer(file)
#    row = writer.writerow([title,author])
        
        
"""
v2. Using DictWriter - safer even in reading
"""
with open("books.csv", "a", newline='') as file:
   writer = csv.DictWriter(file, fieldnames=["Title","Author"])
   """
   fieldnames takes a list of the the column names, which
   act as the dictionary keys in writing each row.
   """
   row = writer.writerow({"Title":title, "Author":author})
