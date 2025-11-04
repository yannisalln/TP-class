
from collections import defaultdict

# 1

# class Student:
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name

#     def __repr__(self):
#         return(self.first_name + " " + self.last_name)


# try:
#     student = Student("Achille", "Talon")
#     if repr(student) != "Achille Talon":
#         raise Exception("There is an issue in your __repr__ method.")
# except Exception as e:
#     print('OOPS - There is an issue in your code.')
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')


# 2

# class Student:
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.dic_grade = {}

#     def __repr__(self):
#         return(self.first_name + " " + self.last_name)
    
#     def add_grade(self, topic: str, grade: float):
#         self.dic_grade[topic] = grade

# try:
#     student = Student("Achille", "Talon")
#     student.add_grade("History", 10.)
#     student.add_grade("History", 12.)
# except Exception as e:
#     print('OOPS - There is an issue in your add_grade method.')
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')

# 3 

# class Student:
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.dic_grade = {}

#     def __repr__(self):
#         return(self.first_name + " " + self.last_name)
    
#     def add_grade(self, topic: str, grade: float):
#         self.dic_grade[topic] = grade
    
#     def followed_topics(self):
#         return self.dic_grade.keys()

# try:
#     student = Student("Achille", "Talon")
#     student.add_grade("History", 10.)
#     topics = student.followed_topics()
#     if len(topics) != 1 or "History" not in topics:
#         raise Exception(f"Expecting ['History'] got {topics}")
# except Exception as e:
#     print('OOPS - There is an issue in your followed_topics method')
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')

# 4

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.dic_grade = {}

    def __repr__(self):
        return(self.first_name + " " + self.last_name)
    
    def add_grade(self, topic: str, grade: float):
        self.dic_grade[topic] = grade
    
    def followed_topics(self):
        return self.dic_grade.keys()