class Student:
    def __init__(self, name, course, year, section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section 
    
    def introduce(self):
        print("     Name   : " + self.name)
        print("     Course : " + self.course)
        print("     Year   : " + self.year)
        print("     Section: " + self.section)

listOfStudents = []

while True: 
    print()
    name = input("Name   : ")
    course = input("Course : ")
    year = input("Year   : ")
    section = input("Section: ")
    stud = Student(name, course, year, section)
    listOfStudents.append(stud)
    print()
    choice = input("Create another student?[Y/N]: ")
    if choice == 'Y' or choice == 'y': pass
    else: break

i=1
for student in listOfStudents:
    print()
    print("Student #" + str(i))
    student.introduce()
    i += 1
