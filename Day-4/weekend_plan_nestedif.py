amount = int(input("enter the amount:"))

if amount > 50000:
    print("Go for the Investments")
elif amount > 20000:
    print("Go for the trip")
elif amount > 10000:
    print("Go for the clubbings")
elif amount > 5000:
    print("Go for the cafe/Restaurant")
elif amount > 1000:
    print("Go for the Shopping")
elif amount > 500:
    print("Go to Movie !")
elif amount > 100:
    print(" Go for Netflix Subscription ")
elif 20 < amount < 99 :
    print("Go for Street food")
else:
    print("Better stay at Home")
    
