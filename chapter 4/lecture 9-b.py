# tuple application with list
marks=[15,18,25,20]
names =['Saeed','ahmad','abdulla','aya']
all_student = zip(names,marks)
for names,marks in all_student: # or replace the names,marks with i,j
    print(names,marks) # and here replace the names,marks with i,j
print(type(all_student))
