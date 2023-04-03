#WAP for factorial using loop Method

a = int(input("Enter a number: "))
f = 1
c=0
for i in range(1,a+1):
    f = f*i
    c=c+1
print("The factorial of",a,"is",f)
print("No of loop run is: ", c)
