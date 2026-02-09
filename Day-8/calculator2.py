def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def mod(a,b):
    return a%b

exp=input("enter the exp:")

for i in exp:
    if i=='+':
        a,b=exp.split('+')
        print(add(int(a),int(b)))
    elif i=='-':
        a,b=exp.split('-')
        print(subtract(int(a),int(b)))
    elif i=='*':
        a,b=exp.split('*')
        print(multiply(int(a),int(b)))
    elif i=='/':
        a,b=exp.split('/')
        print(divide(int(a),int(b)))
    elif i=='%':
        a,b=exp.split('%')
        print(mod(int(a),int(b)))
        
