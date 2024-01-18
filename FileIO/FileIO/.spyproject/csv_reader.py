# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:01:47 2024

@author: Shemuel
"""
import csv

with open("names_birthdays.csv") as birthdays:
    # get an iterable reader using the csv module
    reader = csv.reader(birthdays)
    for name,birthday in reader:
        print(f"{name}-->{birthday}")
    
    