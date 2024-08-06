# [sep] & [end]
"""
print('3mmak',"Ronaldo 👀", 7,sep=" " , end=' --- ' )
print('Fawzi', 'Raed', 'Attal')


x =10
X =True

print("fawzi", "raed", x, X)

print(type(x)==float)
print(type(X)==float)
print(id(x))

# [+]
x=2+x
print(x)
print(id(x))



# [^]
# x = x**2
# print(x)
# print(id(x))



# [÷]
# x=x//2
# print(x)
# print(id(x))



# methid 1: [input] & covert from str to int:
name = input("Enter Your name: ")
# print("your name is: ", name)



method 2: [convert str to int]:
birthyaer = input("Enter your birthyear: ")
birthyaer = int(birthyaer)
age = 2024 - birthyaer
print("Your age is: ",age)



# to summarize lines, (same exammble):
birthyaer = int(input("Enter your birthyear: "))
age = 2024 - birthyaer
# print("Your age is: ",age)




# [total hours (GPA)]:
totalHours = int(input("Enter Total credit hours: "))
score = float(input("Enter your score: "))

gpa = score / totalHours
# print("your GPA is: ", gpa)


# summarize lines, (same exammble):
print("your name is: ", name, "age is: ", "gpa is: ", gpa)
"""


print( ("0"*5 + "\n")*5 )
print("\n"+"--------------------------------"+"\n")

# Boolean: [0 as str] = true, [0 as int] = false, else == true.
# in pyton, just [True, False], start capitalization!
print(bool(0))
print(bool(2))
print(bool(-55))
print(bool("0"))
print(bool("fawzi"))

print(int(False))
print(int(True))
print(int(True+1))
print(int(True+2))















# sep: Delete space.
# end: (by default make [space]).
# Arithmatic Operation: [^]==[**].
# change dataType: int(   ) or str(    ) or bool(    ).
# to take value from user:  x = input("Enter a number: ")