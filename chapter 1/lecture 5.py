"""k = int(input('enter k:'))
n = 1
sum = 0
while n<=k:
    sum += 1/n**2
    n += 1
print('sum =',sum)"""

# do the 1/n!
# f=f*n

k = int(input('enter a number:'))
result=''
while k != 0:
    r = k % 2
    #print(r, end='')
    result = str(r) + result
    k = k//2
print(result)
