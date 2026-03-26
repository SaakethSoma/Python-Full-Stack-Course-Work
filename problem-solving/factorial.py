#factorial of a number using recursion
def factorial(n,fact):
    if n==0:
        return fact

    return factorial(n-1,fact*n)

print(factorial(5,1))
print(factorial(7,1))
print(factorial(4,1))
print(factorial(8,1))


#without using recursion
n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact) 