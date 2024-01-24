# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 07:39:28 2024

@author: Shemuel
"""
import random

class Student:
    
    # a class variable - available to all instances
    hobbies = ["reading","writing","singing"]
    
    @classmethod # a class method.
    def get_hobby(cls): #cls references the class.
        return random.choice(cls.hobbies)
    
    @classmethod
    def createStudent(cls):
        name = input("Name? ")
        house = input("House? ")
        status = input("Day or Boarding (D or B)? ")
        return cls(name,house,status)
    
    # constructor/initialization method
    def __init__(self,name,house,status="BOARDING"):
        self.name = name
        self.house = house 
        self.status = status # Day or Border.
    # special method to convert object to str  
    def __str__(self):
        return f"{self.name} lives in {self.house}"
    
    
    # getters and setters
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        # validation
        if not name:
            raise ValueError("Missing Name")  
        self._name = name
    
    @property # indicates a getter
    def house(self):
        return self._house
    
    @house.setter
    def house(self,room):
        # validation
        if room not in ["SunnySide","RiverBank",
                        "HillTop"]:
            raise ValueError("Missing House!")
        self._house = room
        
    @property # indicates a getter
    def status(self):
        return self._status
    
    @status.setter
    def status(self,status):
        if status not in ["D","B"]:
            raise ValueError("Invalid student status") 
        if status == "D":
            status = "Day".upper()
        if status == "B":
            status = "Boarding".upper()
            
        self._status = status
    
    
    # other methods here...
    
########################################################

class Candidate(Student):
    def __init__(self, name,house,status,age):
        super().__init__(name,house,status)
        self.age = age


########################################################    
    
def main():
    # create a student object   
    student = Student.createStudent()
    print(student.name, "|", student.house,"|", student.status)
    # using class method and variable.
    print(f"Hobby: {Student.get_hobby()}")
    # print(student.status.upper()+" student")
    

if __name__=="__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    