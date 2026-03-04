class snapchat:
    def __init__(self,username,password,friends):
        self.username= username #public
        self.__password= password #private 
        self._friends= friends  #protected
    def getpassword(self):
        return self.__password
    def setpassword(self,new_password):
        self.__password= new_password
    @property
    def oprFriends(self):
        return self._friends
    @oprFriends.setter
    def oprFriends(self,newfriend):
        self._friends.append(newfriend)
    
saaketh= snapchat('saaketh','12345',['praveen','nikhil'])
print(f'name before modification:{saaketh.username}')
saaketh.username= 'swapnil'
print(f'name after modification:{saaketh.username}')
print(f'password before modification:{saaketh.getpassword()}')
saaketh.setpassword('S@123')
print(f'password after modification:{saaketh.getpassword()}')
print(f'Friends before modification:{saaketh.oprFriends}')

saaketh.oprFriends='abhinandhan'
print(f'Friends before modification:{saaketh.oprFriends}')

