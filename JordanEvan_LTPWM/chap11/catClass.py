class cat(object):
    def _init_(self, name, weight):
        self.name = name
        self.weight = weight
        
fluff = cat("fluff",4.5)
print(fluff.weight)
fluff.weight = 5