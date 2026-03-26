#checking palindrome of a given number
num = int(input("Enter a number: "))
entered_value=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10

if entered_value == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")



#checking palindrome of a given string
s=input("Enter a string: ")
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")