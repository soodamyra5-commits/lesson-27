class myclass:
    __privateVar = 27
    def __privateMeth(self):
        print("I'm in the class myclass")
    def hello (self):
        print("The private var value is", myclass.__privateVar)
        self.__privateMeth()
obj  =myclass() 
obj.hello()