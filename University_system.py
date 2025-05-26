class Person:
    def __init__(self, name, NIN):
        self.name = name
        self.NIN = NIN
     
    def displayDetails(self):
        print(f'''
              Name: {self.name}
              NIN: {self.NIN}
              ''')

class Staff(Person):
    def __init__(self, name, NIN, staffNO):
        super().__init__(name, NIN)
        self.staffNO = staffNO
        
    def displayDetails(self):
        print(f'''
              Name: {self.name}
              NIN: {self.NIN}
              Staff Number: {self.staffNO}
              ''')

class Student(Person):
    def __init__(self, name, NIN, student_ID):
        super().__init__(name, NIN)
        self.student_ID = student_ID
        
    def displayDetails(self):
        print(f'''
              Name: {self.name}
              NIN: {self.NIN}
              StudentID: {self.student_ID}
              ''')

class Lecturer(Staff):  # Lecturer is a specialized Staff
    def __init__(self, name, NIN, staffNO, lecturerID, Course):
        super().__init__(name, NIN, staffNO)
        self.lecturerID = lecturerID
        self.Course = Course
        
    def displayDetails(self):
        print(f'''
              Name: {self.name}
              NIN: {self.NIN}
              Staff Number: {self.staffNO}
              LecturerID: {self.lecturerID}
              Course taught: {self.Course}
              ''')

# Create objects
person1 = Person("Mushabe", "C012fE") 
staff1 = Staff("Mike", "C2223KF", "206B") 
lecturer1 = Lecturer("Agaba", "C000f4500E", "205C", "2222", "BSSE") 

# Call display methods
person1.displayDetails()
staff1.displayDetails()
lecturer1.displayDetails()