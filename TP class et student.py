
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

# class Student:
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.dic_grade = defaultdict(list)

#     def __repr__(self):
#         return(self.first_name + " " + self.last_name)
    
#     def add_grade(self, topic: str, grade: float):
#         if not (0 <= grade <= 20):
#             raise ValueError("Grade must be between 0 and 20.")
#         self.dic_grade[topic].append(grade)
    
#     def followed_topics(self):
#         return self.dic_grade.keys()
    
#     def compute_average(self, topic: str):
#         if self.dic_grade[topic] == []:
#             return -1
#         else:
#             G = 0
#             for g in self.dic_grade[topic]:
#                 G += g
#             return G/len(self.dic_grade[topic])

# try:
#     student = Student("Achille", "Talon")
#     student.add_grade("History", 10.)
#     student.add_grade("History", 12.)
#     if (student.compute_average("History") != 11.):
#         raise Exception("Issue in your average calculation.")
#     if (student.compute_average("French") != -1.):
#         raise Exception("If topic is not followed return -1")
# except Exception as e:
#     print('OOPS - There is an issue in your compute_average method.')
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')  

# 5

# class Student:
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.dic_grade = defaultdict(list)

#     def __repr__(self):
#         return(self.first_name + " " + self.last_name)
    
#     def add_grade(self, topic: str, grade: float) -> None:
#         if not (0 <= grade <= 20):
#             raise ValueError("Grade must be between 0 and 20.")
#         self.dic_grade[topic].append(grade)
    
#     def followed_topics(self) -> list:
#         return self.dic_grade.keys()
    
#     def compute_average(self, topic: str) -> float:
#         if self.dic_grade[topic] == []:
#             return -1
#         else:
#             G = 0
#             for g in self.dic_grade[topic]:
#                 G += g
#             return G/len(self.dic_grade[topic])
    
#     def report(self):        
#         """ génère un rapport formaté des moyennes par matière """
#         report_lines = []
#         header = f"Report for student {self.first_name} {self.last_name}"
#         report_lines.append(header)
#         report_lines.append("+===============+===============+")
#         report_lines.append("|     Topic     |    Average    |")
#         report_lines.append("+===============+===============+")
        
#         for topic in self.followed_topics():
#             average = self.compute_average(topic)
#             report_lines.append(f"|  {topic:<13}|    {average:>6.2f}     |") # Format topic left-aligned in 13 spaces, average right-aligned in 6 spaces with 2 decimals
#             report_lines.append("+---------------+---------------+")
        
#         return "\n".join(report_lines)

# try:
#     student = Student("Achille", "Talon")
#     student.add_grade("History", 10.)
#     student.add_grade("History", 12.)
#     if (student.compute_average("History") != 11.):
#         raise Exception("Issue in your average calculation.")
#     if (student.compute_average("French") != -1.):
#         raise Exception("If topic is not followed return -1")
# except Exception as e:
#     print('OOPS - There is an issue in your compute_average method.')
#     print(f"Error message : {e}")
# else:
#     print('Congrats ! Your implementation works !')



        