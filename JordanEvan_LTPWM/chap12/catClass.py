class Cat(object):
    owner = "Craig"
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    def eat(self,food):
        self.weight=self.weight+0.05
        print(self.name +" is eating " + food)
        
    def eatAndSleep(self, food):
        self.eat(food)
        print(self.name + " is now sleeping... ")
    
    def getWeightInGrams(self):
        return self.weight * 1000
    
    
fluff = Cat("fluff",4.5)
print(fluff.owner)
stella = Cat("Stela",3.9)
print(stella.owner)

print(fluff.weight)
fluff.eat("tuna")
fluff.eatAndSleep("tuna")

print(fluff.getWeightInGrams())