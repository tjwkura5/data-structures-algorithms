from collections import defaultdict 
s = "1:max:4, 2:ann:0, 3:alb:2, 4:edmond:2, 5:bruce:0"
emp_names = {}
top_managers = []
employee_directory = defaultdict(list)

# you are given a string
# "1:max:4, 2:ann:0, 3:alb:2, 4:edmond:2"

# the format of the string is "id:name:manager_id"

# Print this: 

# Ann
# - Alb
# - edomnd
# -- max

def split_string(string, delimiter):
    return string.split(delimiter)

def print_directory(string):
    for employee in split_string(string, ', '):
        id, name, manager_id = split_string(employee, ':')
        emp_names[id] = name
        employee_directory[manager_id].append(id)
        if manager_id == '0':
            top_managers.append(id)
    for mananager in top_managers:
        helper(mananager, 0)

def helper(emp_id, level):
    plevel = level * '-' + ' ' if level > 0 else ''
    print(f'{plevel}{emp_names[emp_id]}')
    for emp in employee_directory[emp_id]:
        helper(emp, level+1)


print_directory(s)