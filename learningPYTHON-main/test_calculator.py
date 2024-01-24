# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:04:44 2024

@author: Shemuel
"""

from calculator import square



def main():
    test_positives()
    test_negatives()
    test_zero()
    print("Success!")
    
    
    
def test_positives():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negatives():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
    
    
   


    
if __name__ == "__main__":
    main()