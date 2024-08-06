n = int(input('enter number of integers:'))
if n > 0:
    i = 0
    sum = 0
    while i < n:
        mark = None
        try:
            mark = int(input("enter mark:"))
        except:
            mark = -1
        if 0 <= mark <= 100:
            sum += mark
            i += 1
        else:
            print('invalid No.')
    print('avg= ', sum / n)
else:
    print('error')
