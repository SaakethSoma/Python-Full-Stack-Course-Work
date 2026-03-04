class instagramV1:
    def __init__(self,username):
        self.username=username
        print(f" hey {self.username}, welcome to the Instagram!!!")
    def reels(self):
        print("you can upload and scroll the reels")
    def posts(self):
        print("you can post your pictures")

class instagramV2(instagramV1):
    def __init__(self,username):
        super().__init__(username)
    def story(self):
        print("you can upload the story")

class instagramV3(instagramV2):
    def __init__(self,username):
        super().__init__(username)
    def note(self):
        print("you can upload a note")

class live:
    def launchlive(self):
        print("now you can go on live")
class verification:
    def verify(self):
        print("you can verify your account for better features")
class instagramV4(instagramV3,live,verification):
    def __init__(self,username):
        super().__init__(username)

class creator(instagramV4):
    def __init__(self,username):
        super().__init__(username)
    def insights(self):
        print("you can check your posts insights")
class business(instagramV4):
    def __init__(self,username):
        super().__init__(username)
    def buttons(self):
        print("you can contact them mail and number")
    

saaketh=instagramV1('saaketh')
saaketh.reels()
saaketh.posts()
nikhil=instagramV2('Nikhil')
nikhil.reels()
nikhil.posts()
nikhil.story()
praveen=instagramV3('praveen')
praveen.reels()
praveen.posts()
praveen.story()
praveen.note()
sandeep=instagramV4('sandeep')
sandeep.reels()
sandeep.posts()
sandeep.story()
sandeep.note()
sandeep.launchlive()
sandeep.verify()

