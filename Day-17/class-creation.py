class Flipkart:
    discount =10
    
    @classmethod
    def updatediscount(cls,newdiscount):
        cls.discount=newdiscount
        print(f'{cls.discount} is your discount')
        
    def  userinfo(self,name,phonenumber):
        self.name=name
        self.phonenumber=phonenumber
        print(f'Username:{self.name}')
        print(f'Phone number: {self.phonenumber}')
        
    @staticmethod
    def banner():
        print("welcome to the flipkart\n 10% discount is going on,shop now")



praveen=Flipkart()
praveen.userinfo('praveen',9876543210)
praveen.updatediscount(30)
Flipkart.updatediscount(40)
praveen.banner()
Flipkart.banner()

saaketh=Flipkart()
saaketh.userinfo('saaketh',9876543210)

swapnil=Flipkart()
swapnil.userinfo('swapnil',9876543210)
