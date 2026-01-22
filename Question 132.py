'''   Student Result System
 Task:

Input marks

Calculate percentage

Return Pass/Fail'''

def student_result(marks):
    percentage = sum(marks) / len(marks)

    if percentage >= 40:
        return "pass"
    else:
        return "Fail"
    
print(student_result([45,67,89,76]))    