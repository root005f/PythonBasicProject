"""# Dictionaries example - convert list to dictionary
dept_counts = [4, 2, 3, 2]
depts = ['DS&AI', 'CS', 'SE', 'IS']
deptss=dict(zip(depts,dept_counts)) # dict we use this word when we need to print as a dictionary rather than list
print(deptss)
"""
"""# Dictionaries example - count specs in list of student specs
# Print all specs count of student in each department

student_specs= ['DS&AI', 'CS', 'SE', 'IS','CS', \
                'SE', 'IS','DS&AI', 'CS','SE', \
                'CS', 'SE','IS']
specs= dict() # or {}
for s in student_specs:
    if s in specs:
        specs[s] +=1
    else:
        specs[s] =1
print(specs)"""

student_specs= ['DS&AI', 'CS', 'SE', 'IS','CS', \
                'SE', 'IS','DS&AI', 'CS','SE', \
                'CS', 'SE','IS','ART','DNT','ENG', \
                'SE','CS','MGM','OTHER']
student_count=0
specs= {'DS&AI':0, 'CS':0, 'SE':0, 'IS':0,'OTHER':0}
for s in student_specs:
    if s in specs and s != 'OTHER':
        specs[s] +=1
        student_count +=1
    else:
        specs['OTHER'] +=1
print(specs)
print("number of student in FIT: ", student_count)