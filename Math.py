class Math(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.result = 0;

    def add(self):
        self.result = self.x+self.y
        return(self.result)

    def sub(self):
        self.result = self.x-self.y
        return(self.result)

    def mul(self):
        self.result = self.x*self.y
        return(self.result)

    def div(self):
        self.result = self.x/self.y
        return(self.result)
    
    def __str__(self):
        return "The result is: "+str(self.result)

if __name__ == "__main__":
    a = Math(10,2)
    
    a.add()
    print(a)
    a.sub()
    print(a)
    a.mul()
    print(a)
    a.div()
    print(a)
    
