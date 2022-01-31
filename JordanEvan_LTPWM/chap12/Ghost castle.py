from mcpi.nibecraft import Minecraft
mc = Minecraft.create()
import time

class Building(object):
    def __init__(self,x,y,z,width, height, depth,name):
        self.x = x
        self.y = y
        self.z = z
        
        self.width = width
        self.height = height
        self.depth = depth
        
        self.name = name
        
    def build(self):
        mc.setBlocks(self.x,self.y,self.z,self.x+self.width,self.y+self.height,self.z+self.depth,4)
    
        mc.setBlocks(self.x+1,self.y+1,self.z+1,self.x+self.wodth-1,self.y+self.height-1,self.z+self.depth-1,0)
    def clear(self):
        mc.setBlocks(self.x,self.y,self.z,self.x+self.width,self.y+self.height,self.z+self.depth,0 )
        
    def getInfo():
        
pos = mc.player.getTilePos()
x = pos.x+3
y = pos.y
z = pos.z+3

ghostCastle = NamedBuilding(x,y,z,10,16,16, "Ghost Castle")
ghostCastle.build()

time.sleep(30)

ghostCastle.clear()