
def factorial(a):
    n=1
    while a!=1:
        n=(n*a)
        a=a-1
       
    return n

num=int(input("Enter a number:"))
print("Factorial of",num,"is:",factorial(num))