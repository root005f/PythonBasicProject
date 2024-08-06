name =[]
names= list()
namess= [10,20,30,True,'saeed',[1,[10,20]],5.2]
print(namess)
for i in namess:
    print(i)
print(type(namess))
print(namess[4])
print(len(namess))#length
print(namess[len(namess)-1])# print last index
print(namess[5][1][0])# print nested list index
marks=[1,2,3,4,5,6]
marks2=[10,20,30]
marks_all=marks+marks2
print(marks_all)
marks_all.sort()
print(marks_all)
marks_all.reverse()
print(marks_all)
marks_all.append(99)
print(marks_all)
marks_all.insert(0,100)
print(marks_all)