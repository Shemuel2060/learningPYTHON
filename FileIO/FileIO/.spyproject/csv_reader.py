# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:01:47 2024

@author: Shemuel
"""
import csv

members = []
# with open("names_birthdays.csv") as birthdays:
#     # get an iterable reader using the csv module
#     reader = csv.reader(birthdays)
#     for name,birthday in reader:
#         members.append({"name":name, "DOB":birthday})
        
# for member in sorted(members, key=lambda m: m["name"]):
#     print(f"{member['name']} : {member['DOB']}")


"""
v2. using csv.DictReader
"""

with open("names_birthdays1.csv") as birthdays:
    # get an iterable reader using the csv module
    reader = csv.DictReader(birthdays) # each line is a dict.
    for row in reader:
        members.append({"name":row["name"], "age":row["age"]})
        
for member in sorted(members, key=lambda m: m["name"]):
    print(f"{member['name']} : {member['age']}")
    
 # using dict reader uses the column headers to get the data  
# can change to get names with age or names with homes or 
# homes with age as per specification 
    
    
    
