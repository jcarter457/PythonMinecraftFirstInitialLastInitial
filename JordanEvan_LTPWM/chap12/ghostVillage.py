from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


class Building(object):
    def __init__(self,x,y,z,width, height, depth):
        self.x = x
        self.y = y
        self.z = z
        
        self.width = width
        self.height = height
        self.depth = depth
    
    def buildDoor(self,val):
        if val==1:
            mc.setBlock(self.x+1,self.y+2,self.z,0)
            mc.setBlock(self.x+1,self.y+1,self.z,64)
        else:
            mc.setBlock(self.x+1,self.y+1,self.z,0)
    
    def buildWindow(self,val):
        if val==1:
            mc.setBlocks(self.x+3,self.y+2,self.z,self.x + self.width-3, self.y + self.height-4, self.z + self.depth,20)
            mc.setBlocks(self.x+3,self.y+2,self.z+1,self.x + self.width-3, self.y + self.height-4, self.z + self.depth-1,0)
        else:
            mc.setBlocks(self.x+3,self.y+2,self.z,self.x + self.width-3, self.y + self.height-4, self.z + self.depth,0)
    
    def build(self):
        mc.setBlocks(self.x, self.y, self.z, self.x + self.width, self.y + self.height, self.z + self.depth, 4)
        mc.setBlocks(self.x + 1, self.y +1, self.z +1, self.x +self.width -1, self.y + self.height -1, self.z +self.depth -1, 0)
        self.buildDoor(1)
        self.buildWindow(1)
        
    def clear(self):
        mc.setBlocks(self.x, self.y, self.z, self.x + self.width, self.y + self.height, self.z + self.depth, 0)
        self.buildDoor(0)
        self.buildWindow(0)
        

pos = mc.player.getTilePos()
x = pos.x+3
y = pos.y
z = pos.z+3
ghostHouse = Building(x,y,z,10,6,8)
shop = Building(x+ 12, y, z, 8, 12, 10)

ghostHouse.build()
shop.build()

time.sleep(30)

ghostHouse.clear()
shop.clear()