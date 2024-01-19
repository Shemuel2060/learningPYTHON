# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 09:07:26 2024

@author: Shemuel
"""

"""
v1. Read contents of the file and split line at comma
"""

# with open("home.csv") as home:
#     for line in sorted(home):
#         row=line.rstrip().split(",") # split string at comma
#         print(f"{row[0]} : {row[1]}")
        
        
        
"""
v2. Split returns a list of two values - make readable by 
separating them into separate variables instead of a single
list output as before.
"""
# with open("home.csv") as home:
#     for line in sorted(home):
#         name, age=line.rstrip().split(",") # split string at comma
#         print(f"{name} : {age}")


"""
v3. Not sorting file content. 
1. Put the file content into a list of dictionaries
2. Sort the contents by name or by age

"""
members = [] # empty list to contain dictionaries

with open("home.csv") as home:
    for line in home:
        name, age = line.rstrip().split(",")
        # put name and age into a dictionary
        home_dict = {"name":name, "age":age}
        # add each dictionary to the list
        members.append(home_dict)

# testing - printing out each dictionary
# for dict in members:
#     print(dict)

# does not work because we can not compare dictionaries.
# for dict in sorted(members):
#     print(dict)

# define a function to return the name- use this as key in sorting
def get_name(member):
    return member["name"]

# def get_age(member): ### defined a lambda/anonymous function instead
#     return member["age"]


def sort_by_names(un_list):
    """
    takes an unsorted list of dictionaries, and sorts them
    by name.
    Parameters
    ----------
    un_list : list
        list of dictionaries with names and ages.

    Returns
    -------
    list
        list of dictionaries sorted by names.

    """
    return sorted(un_list, key=get_name)

def sort_by_ages(un_list):
    """
    takes an unsorted list of dictionaries, and sorts them
    by age.

    Parameters
    ----------
    un_list : list
        list of unsorted dictionaries.

    Returns
    -------
    list
        list of dictionaries sorted by age.

    """
    return sorted(un_list, key=lambda member: member['age']) 


def print_sorted(s_list):
    for member in s_list:
        print(f"{member['name']} is {member['age']}" )

print("==========sorting by name==========")
name_sorted = sort_by_names(members)
print_sorted(name_sorted)
print("==========sorting by age==========")
age_sorted = sort_by_ages(members)
print_sorted(age_sorted)
