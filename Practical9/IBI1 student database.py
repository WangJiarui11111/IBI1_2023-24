class Student:  
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name=name
        self.major=major
        self.scores_of_portfolio=code_portfolio_score
        self.scores_of_group_project=group_project_score
        self.scores_of_exam=exam_score 
    def print(self):
         print(f"Name: {self.name}, Major: {self.major}, Code Portfolio Score: {self.scores_of_portfolio}, Group Project Score: {self.scores_of_group_project}, Exam Score: {self.scores_of_exam}")  
#For example:
student = Student("Jay", "BMI", 90, 90, 90)   
student.print()