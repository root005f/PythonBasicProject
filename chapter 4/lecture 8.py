"""marks=[1,4,3,2,5,6]
marks2=[10,20,30]
marks_all=marks+marks2
print(marks_all)
#slicing----> indexing
print(marks_all[0:4]) # it will print all between 0 till 3 but not the last which is 4 (the last in the specific range)
print(marks_all[:4]) # it will print all from the beginning till the 3 not the last
print(marks_all[2:]) # it will print all from 2 till the last
print(marks_all[:]) # it will print all
print(marks_all[2:999])# it does not matter if the second index was more than the last or last+1
print(marks_all[::2])# it will print all but with step over 2 index for each till the end
print(marks_all[-1:])# it will print the last index in the list
"""

"""write a program that enters numbers of student (n)
and enter their names and marks, store them in a list,
then find the maximum mark(print the student name)
and find the ave for these marks
"""
"""number = int(input('Enter number of student:'))
max,avg,sum = 0,0,0
max_student= []
marks = []
names = []
for i in range(0,number):
    name = input('enter name:')
    mark = float(input('enter mark:'))
    marks.append(mark)
    names.append(name)
    sum += mark
    if mark >= max:
        max = mark
        max_student = name
avg=sum/number
print(marks,names)
print(avg,max,max_student)"""

number = int(input('Enter number of student:'))
max = 0
max_student= []
marks = []
names = []
for i in range(0,number):
    name = input('enter name:')
    mark = float(input('enter mark:'))
    marks.append(mark)
    names.append(name)
    if mark > max:
        max = mark
        max_student.clear()
        max_student.append(name)
    elif mark == max:
        max_student.append(name)

print(marks,names)
print(max)
print(max_student)