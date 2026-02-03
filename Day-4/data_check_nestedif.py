data={
'saaketh':{'status': True ,'Python': 100, 'MySql' : 99, 'SoftSkills': 85},
'Ravi':{'status':False ,'Python': None , 'MySql' : None , 'SoftSkills': None},
'Nikhil':{'status':True ,'Python': 50 , 'MySql' : 70, 'SoftSkills': 20},
'swapnil':{'status':True ,'Python': 60, 'MySql' : 88 , 'SoftSkills': 76},
'praveen':{'status':True ,'Python': 98 , 'MySql' : 92, 'SoftSkills': 87 }}
 
user=input("enter the student name:")

if user in data :
    if data[user] ['status']:
        sum= data[user]['Python']+data[user]['MySql']+data[user]['SoftSkills']
        avg=sum/3
        if avg > 80:
            print(f"congrats {user} !!!\n You got A grade")
        elif  avg > 60 :
            print(f"Better Luck {user} !!!\n You got B grade")
        elif avg > 40:
            print(f"Need Improvement {user} !!!\n You got C grade")
        else:
            print(f"{user}, failed in the exam\n Bring Your Parents")
    else:
        print(f"{user}didn't write any exams.")
else :
    print(f"{user } not found")


