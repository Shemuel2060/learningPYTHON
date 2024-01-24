# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 09:26:31 2024

@author: Shemuel
"""

import re # import regex module

email = input("Enter email: ")

# r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$"
# r"^\w+@\w+\.(com|edu|org|gov)$  

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|org|gov)$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")


