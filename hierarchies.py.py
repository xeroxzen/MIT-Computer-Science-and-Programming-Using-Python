"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

import random


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)


class Cat(Animal):
    def speak(self):
        print('meow')

    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)


class Rabbit(Animal):
    def speak(self):
        print('meep')

    def __str__(self):
        return "rabbit:"+str(self.name)+":"+str(self.age)


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print('Hello')

    def age_diff(self, other):
        # alternate way: diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years olders than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)

    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)


class Student(Person):
    def __self__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat now")
        else:
            print("I am watching TV")

    def __str__(self):
        return "Student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
