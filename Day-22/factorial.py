import csv
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
        

with open("facttc.csv","r")as file:
    reader=csv.DictReader(file)
    print(reader)
    for row in reader:
        if factorial(int(row['input'])) == int(row['output']):
            print("test case is passed for",row['input'])
        else:
            print("test case failed for",row['input'])
