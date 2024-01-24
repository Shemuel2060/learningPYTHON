# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 06:25:42 2024

@author: Shemuel
"""

from greetings import hello

def main():
    test_default()
    test_argument()
    print("Success!")


def test_default():
    assert hello() == "hello, world"
    
def test_argument():
    assert hello("Samuel") == "hello, Samuel"
    

if __name__ == "__main__":
    main()