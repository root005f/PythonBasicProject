#print all students with sum of mark>=40
names=['Saeed','jihad','abdulla','aya']
first=[22,17,21,19]
second=[18,22,20,23]
marks_sum=[]
for i in range(len(first)):
    marks_sum.append(first[i]+second[i])

students=list(zip(names,first,second,marks_sum))
result_index=[]
for i in range(len(students)):
    if students[i][3] >=40:
        result_index.append((i))


print(result_index)
