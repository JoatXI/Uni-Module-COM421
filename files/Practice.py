class student:
    def __init__(self, id, name, course):
        self.id = id
        self.name = name
        self.course = course
        self.mark = 0
        
# Defining a __str__ method that returns the complete student details as a string.
    def __str__(self):
        return f"{self.id}, {self.name}, {self.course}, {self.mark}"

    def set_mark(self, mark_input):
        if mark_input >= 0 and mark_input <= 100:
            self.mark = mark_input
            return True
        else:
            return False

# Defining a method that returns the students' grades as a string based on the mark.
    def get_grade(self):
        if self.mark >= 70:
            return "First"
        elif self.mark >= 60 and self.mark <= 69:
            return "2/1"
        elif self.mark >= 50 and self.mark <= 59:
            return "2/2"
        elif self.mark >= 40 and self.mark <= 49:
            return "Third"
        else:
            return "Fail"

# Returning a boolean indicating whether the mark is above or below the 40.            
    def did_pass(self):
        if self.mark >= 40:
            return True
        else:
            return False
        
    

# Creating a list of students/pupils.
pupils = []
for num in range(5):
    id_input = int(input("Enter student id: "))
    name_input = input("Enter student name: ")
    course_input = input("Enter student course: ")
    mark_input = int(input("Enter student mark: "))

    student1 = student(id_input, name_input, course_input, mark_input)
    pupils.append(student1)
    
    print(student1.get_grade())
    print(student1.did_pass())
    
for x in pupils:
    print(x)
    