#Aaron OBryant
#CMIS 102 6982
#07/19/2022
#Week 5 Assignment
#This program will calculate the weighted grade for students enrolled in CMIS


#Welcome--
print('\nWelcome to CMIS Gradbook!\t')

def name_grade(student_name):
    
#Input--
    discussion = int(input("What is {}'s discussion grade score?: ".format(student_name)))
    quiz = int(input("What is {}'s quiz grade score?: ".format(student_name)))
    assignment = int(input("What is {}'s assignment grade score?: ".format(student_name)))



    return discussion * 0.2 + quiz * 0.5 + assignment * 0.3

#Output--
    
def main():
    student_names = ["Harry", "Hermione", "Ron", "Draco"]
    student_grades = []
    
    for student_name in student_names:
        student_grade = name_grade(student_name)
        student_grades.append(student_grade)
        print("{}'s average is: {}".format(student_name, student_grade))
        
    head_of_class = max(student_grades)
    student_index = student_grades.index(head_of_class)

#Highest grade 
    print("{} has the highest grade: {}".format(student_names[student_index], head_of_class))

    
# Execute
main()
