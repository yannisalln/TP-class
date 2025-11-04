from student import Student

# 1

# class Class:
#     def __init__(self, classname: str):
#         self.classname = classname
#         self.list_student = []

#     def add_student(self, student: Student):
#         self.list_student.append(student)

#     def __len__(self):
#         return len(self.list_student)

#     def __repr__(self):
#         return f"Class {self.classname} - {len(self)} student(s)"
    
# try:
#     classe = Class("P20")
#     student = Student("Matthieu", "Mazière")
#     classe.add_student(student)
#     if len(classe) != 1:
#         raise Exception('OOPS - There is an issue in your __len__ method.')
#     if repr(classe) != "Class P20 - 1 student(s)":
#         raise Exception('OOPS - There is an issue in your __repr__ method.')
# except Exception as e:
#     print("OOPS - Something's wrong")
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')

# 2

# class Class:
#     def __init__(self, classname: str):
#         self.classname = classname
#         self.list_student = []

#     def add_student(self, student: Student) -> None:
#         self.list_student.append(student)

#     def __len__(self) -> int:
#         return len(self.list_student)

#     def __repr__(self) -> str:
#         return f"Class {self.classname} - {len(self)} student(s)"
    
#     def get_student(self, first_name: str, last_name:str):
#         for student in self.list_student:
#             if student.first_name == first_name and student.last_name == last_name:
#                 return student
#         return None
        
# try:
#     classe = Class("P20")
#     student = Student("Matthieu", "Mazière")
#     classe.add_student(student)
#     new_student = classe.get_student("Matthieu", "Mazière")
#     assert student == new_student
#     new_student = classe.get_student("Jérôme", "Adnot")
#     assert new_student is None
# except Exception as e:
#     print("OOPS - Something's wrong")
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')

# 3

class Class:
    def __init__(self, classname: str):
        self.classname = classname
        self.list_student = []

    def add_student(self, student: Student) -> None:
        self.list_student.append(student)

    def __len__(self) -> int:
        return len(self.list_student)

    def __repr__(self) -> str:
        return f"Class {self.classname} - {len(self)} student(s)"
    
    def get_student(self, first_name: str, last_name:str):
        for student in self.list_student:
            if student.first_name == first_name and student.last_name == last_name:
                return student
        return None
    
    def load_students_from_file(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                first_name, last_name = line.strip().split(',')
                student = Student(first_name, last_name)
                self.add_student(student)
    
try:
    classe = Class("P1920")
    classe.load_students_from_file('doc_classe.csv')
    print(len(classe))
    if len(classe) != 38:
        raise Exception('OOPS - There is an issue in your load_from_file method')
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works ! ')