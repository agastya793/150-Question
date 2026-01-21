''' Create a function that:

Takes basic salary

Adds 20% HRA house rent allowance

Adds 10% DA  Dearness Allowance

Returns total salary'''

def calculate_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    total = basic + hra + da
    return total
salary = calculate_salary(300000)
print("total salary:" , salary)    