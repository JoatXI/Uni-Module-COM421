class student:
    def __init__(self, id, name, course):
        self.id = id
        self.name = name
        self.course = course
        self.mark = 0
        
# Defining a __str__ method that returns the complete student details as a string.
    def __str__(self):
        return f"{self.id}, {self.name}, {self.course}, {self.mark}"

    def set_mark(self):
        if mark_input >= 0 and mark_input <= 100:
            return True
        else:
            return False

# Defining a method that returns the students' grades as a string based on the mark.
    def get_grade():
        if mark_input >= 70:
            return "First"
        elif mark_input >= 60 and mark_input <= 69:
            return "2/1"
        elif mark_input >= 50 and mark_input <= 59:
            return "2/2"
        elif mark_input >= 40 and mark_input <= 49:
            return "Third"
        else:
            return "Fail"

# Returning a boolean indicating whether the mark is above or below the 40.            
    def did_pass():
        if mark_input >= 40:
            return True
        else:
            return False
        
    print(get_grade())
    print(did_pass())

# Creating a list of students/pupils.
pupils = []
for num in range(5):
    id_input = int(input("Enter student id: "))
    name_input = input("Enter student name: ")
    course_input = input("Enter student course: ")
    mark_input = int(input("Enter student mark: "))

    student1 = student(id_input, name_input, course_input, mark_input)
    pupils.append(student1)
    
for x in pupils:
    print(x)
    