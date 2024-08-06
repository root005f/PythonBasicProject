"""score= float( input ("enter the mark: ") )
if 90<=score<=100:    # Chained relational operator
    print("A")
elif 80<=score<=90:   # Chained relational operator
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >=60 and score <70:
    print("D")
elif score < 60 and score >=0:
    print("F")
else:
    #print("invalid")
    pass
"""

mark,gpa= 90,3.5
"""
if mark is not 90:
    print('good')
else:
    print("outstanding")"""
if mark in (90,89,91):
    print('outstanding')
else:
    print("good")


