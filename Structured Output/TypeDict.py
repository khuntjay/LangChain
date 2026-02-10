from typing import  TypedDict

class Person(TypedDict):
    name:str
    age:int


new_dict: Person = {'name':"jay", "age":56 }

print(new_dict)