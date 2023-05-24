#  The self parameter is a reference to the current instance of the class,
#  and is used to access variables that belongs to the class.
#
#  It does not have to be named self , you can call it whatever you like,
#  but it has to be the first parameter of any function in the class:
#
#  def __init__(self, name, age):
#    self.name = name
#    self.age = age

from abc import ABC


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(x):
    print("Hello my name is " +  x.name)
    print("I am " + str(x.age) + " years old")

p1 = Person("John", 36) # seed instaniated object p1 (person 1), dervied from class Person
p1.myfunc() # call function within p1 object