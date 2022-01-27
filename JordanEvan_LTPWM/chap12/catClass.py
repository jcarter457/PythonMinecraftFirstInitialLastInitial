class cat(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def eat(self,food):
        self.weight=self.weight+0.05
        print(self.name +" is eating " + food)
    def eatAndSleep(self, food):
        self.eat(food)
        print(self.name + " is now sleeping... ")
    
fluff = cat("fluff",4.5)
#print(fluff.weight)
#fluff.weight = 5
#fluff.eat("tuna")
fluff.eatAndSleep("tuna")