class student:
    def __init__(self, id, name, course, mark):
        self.id = id
        self.name = name
        self.course = course
        self.mark = mark

    def set_mark(self, mark):
            if mark_input >= 0 and mark_input <= 100:
                return True
            else:
                return False

    def get_grade(self):
        if mark_input >= 70:
            print("First")
        elif mark_input >= 60 and mark_input <= 69:
            print("2/1")
        elif mark_input >= 50 and mark_input <= 59:
            print("2/2")
        elif mark_input >= 40 and mark_input <= 49:
            print("Third")
        else:
            print("Fail")
        

    def __str__(self):
        return f"{self.id}, {self.name}, {self.course}, {self.mark}"


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