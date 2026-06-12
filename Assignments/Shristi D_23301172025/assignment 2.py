#Shristi Dhoundiyal
#23301172025
#Assignment 2
#Find sum of first 10 natural numbers
k=0
for i in range (1,11):
    k=k+i
print("sum is", k)

#Find factorial of a number
num=int(input("Enter a number"))
f=1
for i in range (1,num+1):
    f=f*i
    i=i+1
print(f, "is the factorial")
    
#Print fibonacci series
a=int(input("Enter how many fibonacci elements"))
print(0)
print(1)
def fibonacci(a):
        num1=0
        num2=1
        for i in range(2,a):
            num3=num1+num2
            print(num3)
            num1=num2
            num2=num3
fibonacci(a)
        
    
#Find largest among 3 numbers
def largest(a,b,c):
    if a==b or a==c or b==c or a==b==c:
        print("Please input distinct numbers")
    if a>b and a>c:
        print(a,"is the largest number")
    elif b>a and b>c:
        print(b, "is the largest number")
    else:
        print(c, "is the largest number")
        
x=int(input("Enter an integer"))
y=int(input("Enter an integer"))
z=int(input("Enter an integer"))
largest(x,y,z)

        
#Create student result system (input student details, input marks, calculate percentage, display grade, use)

def student_result_system():
    ans="y"
    while ans=="y":
        name=input("Enter name of the student")
        roll=int(input("Enter roll number of student"))
        maths=int(input("Enter maths marks of student out of 100"))
        eng=int(input("Enter english marks of student out of 100"))
        sci=int(input("Enter science marks of student out of 100"))
        total=maths+eng+sci
        percentage=(total/3)*100
        print("grade of the student", name, "is", grade(percentage))
        ans=input("Do you want to enter more student details? (y/n)")

def grade(per):
    if per>=81:
        return("A")
    elif per>=61:
        return("B")
    elif per>=41:
        return("C")
    else:
        return("D")
student_result_system()

    
