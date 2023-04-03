# WAP to find the Factorial using Recursions method

C= 0 # counter
def F(n):  
    global C
    if n == 0:
        return 1
    else:
        C = C + 1
        return n * F(n-1)

a = int(input("Enter a number: ")) # User Input 
print("The Factorial of", a, "is", F(a)) 
print("Number of recursions taken:", C) # No of Recursions taken 
