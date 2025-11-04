from student import Student

# 1
class Class:
    def __init__(self, classname: str):
        self.classname = classname
        self.list_student = []

    def add_student(self, student: Student):
        self.list_student.append(student)

    def __len__(self):
        return len(self.list_student)

    def __repr__(self):
        return f"Class {self.classname} - {len(self)} student(s)"
    
try:
    classe = Class("P20")
    student = Student("Matthieu", "Mazière")
    classe.add_student(student)
    if len(classe) != 1:
        raise Exception('OOPS - There is an issue in your __len__ method.')
    if repr(classe) != "Class P20 - 1 student(s)":
        raise Exception('OOPS - There is an issue in your __repr__ method.')
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')