# This a test file for experiment
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    print("hey")
    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    def full_profile(self):
        return f"Name: {self.firstname} {self.lastname} Age: {self.age}"