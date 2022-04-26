class Person:
    def __init__(self, fname, lname):
        self.fristname = fname
        self.lastname = lname

        def myfun(self):
            print("my name is" + self.lastname)


class Child(Person):
    def __init__(self, fname, lname):
        Person.__init__(fname, lname)
        x = Child("parag", "pande")
        x.myfun()
