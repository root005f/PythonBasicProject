# previous loop 👆 (in lecture 9), we'll take it in another shortest way!
# another way to list names with its index as a number:
# merge the lists
names = ["saed", "jihad", "abdullah", "aya"]
# names.pop(0)                      # delete the element [meth 1] (this method specific for lists)
del names[0]                        # delete the element [meth 2] (this method for everything) >> this is best!
print(*range(0, len(names)))        # range(0,4)
print(list(range(0, len(names))))   # range(0,4)

for i in range(0, len(names)):      # [iterate]~~
    print(i, names[i])              # print names with its indexes!

# ~ _________________________________________ ~ method 1 (zip) #

names = ["saed", "jihad", "abdullah", "aya"]
first = [22,17,21,19]
second = [18,22,20,23]
Marks_Sum = []
for f,s in zip(first,second):
    Marks_Sum.append(f+s)           # [22+18, 17+22, ...] this method to sum to list in same time! (append)
print(Marks_Sum)

# ~ _________________________________________ ~ method 2 (enumerate) #

names = ["saed", "jihad", "abdullah", "aya"]
first = [22,17,21,19]
second = [18,22,20,23]
Marks_Sum = []
for i,f in enumerate(first):
    Marks_Sum.append(f + second[i])
print(Marks_Sum)

# ~ _________________________________________ ~ method 3 (range) #

names = ["saed", "jihad", "abdullah", "aya"]
first = [22,17,21,19]
second = [18,22,20,23]
Marks_Sum = []
for i in range(len(first)):
    Marks_Sum.append( first[i] + second[i])
# print(Marks_Sum)

# ~ _________________________________________ ~ #
students = (list (zip(names, first, second, Marks_Sum)))
max_sum = -1
max_index = -1
for i in range(len(students)):
    if max_sum < students[i][3]:
        max_sum = students[i][3]
        max_index = i
print(max_index,max_sum)

# ~ _________________________________________ ~ #
# ~ _________________________________________ ~ #


