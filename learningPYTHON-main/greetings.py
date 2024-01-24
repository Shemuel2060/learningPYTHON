# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:13:43 2024

@author: Shemuel
"""

def main():
    hello("Samuel")
    goodbye("Samuel")
    print("success!")
    
    
def hello(name="world"):
    return "hello, "+ name

def goodbye(name="world"):
    return "goodbye, "+ name
    
if __name__ == "__main__": # ensures main is only called when it is this 
                            #script that is run
    main()
    
