"""names=['Ahmad','khalid','Saeed']
print(names[1])
for n in names:
    print(n)

student_name= "Saeed Ahmad"
for i in student_name:
    print(i,'-',end="")
print('###########')

for i in range(6,1): #==> [1,2,3,4,5]
    print(i)
print('###########')

for i in range(5,1,2):#==> [1,2,3,4,5]
    print(i)
print('###########')

for i in range(5,0,-1):#==> [5,4,3,2,1]
    print(i)
print('###########')
"""

"""k= int(input('enter k:'))
n=1
sum=0
for n in range(1,k+1):
    sum+=1/n**2
print('sum =',sum)
"""
n = int(input('enter number of integers:'))
sum = 0
for i in range(1,n+1):
    while True:
        mark = None
        try:
            mark = int(input("enter mark:"))
        except:
                mark = -1
        if 0<=mark<=100:
            sum += mark
            break
        else:
            print('invalid No.')
print('avg= ', sum / n)
