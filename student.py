from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.dic_grade = defaultdict(list)

    def __repr__(self):
        return(self.first_name + " " + self.last_name)
    
    def add_grade(self, topic: str, grade: float) -> None:
        if not (0 <= grade <= 20):
            raise ValueError("Grade must be between 0 and 20.")
        self.dic_grade[topic].append(grade)
    
    def followed_topics(self) -> list:
        return self.dic_grade.keys()
    
    def compute_average(self, topic: str) -> float:
        if self.dic_grade[topic] == [] or topic not in self.dic_grade.keys():
            return -1
        else:
            G = 0
            for g in self.dic_grade[topic]:
                G += g
            return G/len(self.dic_grade[topic])
    
    def report(self):        
        """ génère un rapport formaté des moyennes par matière """
        report_lines = []
        header = f"Report for student {self.first_name} {self.last_name}"
        report_lines.append(header)
        report_lines.append("+===============+===============+")
        report_lines.append("|     Topic     |    Average    |")
        report_lines.append("+===============+===============+")
        
        for topic in self.followed_topics():
            average = self.compute_average(topic)
            report_lines.append(f"|  {topic:<13}|    {average:>6.2f}     |") # Format topic left-aligned in 13 spaces, average right-aligned in 6 spaces with 2 decimals
            report_lines.append("+---------------+---------------+")
        
        return "\n".join(report_lines)