"""
Basics of Python
Lab 2, Part 3
"""

from dataclasses import dataclass

"""
The dataclass make classes easier in some ways. By automatically generating boilerplate code it saves coders time. 

The generic boilerplate it throws in can also be overriden by manually declaring it, as I have with __str__ below. 
"""

@dataclass
class Student:
    name: str
    starid: str
    gpa: float

    def __str__(self):
        return (f"\n{'*'*30}"
                f"\n{self.name}"
                f"\n{self.starid}"
                f"\nGPA: {self.gpa}"
                f"\n{'*'*30}\n")



def main():
    jon = Student("Jon", "ha39ai",3.9)
    jill = Student("Jill", "ja38ie",3.8)
    jamie = Student("Jamie", "ke82is",3.2)

    print(jon.name)
    print(jill.starid)
    print(jamie.gpa)
    print(jill,jon,jamie)

main()