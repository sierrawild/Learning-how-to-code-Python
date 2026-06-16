class Box():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
name = "Garry"
surname = "Lee"

student = Box(name, surname)


print(f'{student.name} {student.surname} is awesome')