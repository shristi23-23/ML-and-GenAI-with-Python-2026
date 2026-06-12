#Assignment 1

#Find area of rectangle
l=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
a=l*b
print(a, "is the area of the rectangle")

#Find simple interest
p=int(input("Enter Principal amount: "))
r=int(input("Enter Rate: "))
t=int(input("Enter Time in years: "))

si=(p*r*t)/100

print(si, "is the simple interest")

#Convert temperature from Celsius to Farenheit
c=int(input("Enter Temperature in Degree celsius: "))
f=(c*(9/5))+32
print(f, "is the temperature in Farenheit")

#Calculate average of 3 numbers
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
z=int(input("Enter a number: "))

average=(x+y+z)/3

print("Average of the 3 numbers",x, "," ,y, "and",z ,"is", average)

#Find square and cube of a number
num=int(input("Enter a number: "))
sq=num**2
cub=num**3
print(sq, "is the square of", num)
print(cub, "is the cube of", num)

#Swap two numbers without third variable
a=int(input("Enter a number"))
b=int(input("Enter a number"))
print("Before swap")
print("a=",a)
print("b=",b)
a,b=b,a
print("After swap")
print("a=",a)
print("b=",b)

#Create a student report program that take student details using input(), store marks in variables, calculate total and percentage, use comments, use proper indentation

#loop to enter details of students
ans="yes"
while (ans=="yes"):
    name=input("Enter name of student: ")
    maths=int(input("Enter maths marks of student out of 100: "))
    eng=int(input("Enter english marks of student out of 100: "))
    sci=int(input("Enter science marks of student out of 100: "))
    total=maths+sci+eng
    percentage=(total/3)*100
    ans=input("Do you want to enter more details? (yes/no)")
    

    
