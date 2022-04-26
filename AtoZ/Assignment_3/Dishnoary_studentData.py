class Student:
    def GetStudent(self):
        self.rollno = input("Enter Roll No:")
        self.name = input("Enter Name:")
        self.physicsMarks = int(input("Enter Physics Marks:"))
        self.chemistyMarks = int(input("Enter Chemistry Marks:"))
        self.mathMarks = int(input("Enter Maths Marks:"))
        return (self.rollno)

    def PutStudent(self):
        print(self.rollno, self.name, ((self.physicsMarks + self.chemistyMarks + self.mathMarks) / 3))

    def Search(self, min, max):
        per = (self.physicsMarks + self.mathMarks + self.chemistyMarks) / 3
        if (per >= min and per <= max):
    # print()
