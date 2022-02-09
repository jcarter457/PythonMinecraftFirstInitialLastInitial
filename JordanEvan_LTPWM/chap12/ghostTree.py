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
        
    def growTree(self,state):
        if state==1:
            wood=17
            leaves=18
        else:
            wood,leaves=0,0
        
        #trunk
        mc.setBlocks(x,y,z,x,y+5,z,wood)
        
        
        #leaves
        mc.setBlocks(x-2,y+6,z-2,x+2,y+6,z+2,leaves)
        mc.setBlocks(x-1,y+7,z-1,x+1,y+7,z+1,leaves)
    
    def build(self):
        self.growTree(1)

    def clear(self):
        self.growTree(0)


pos = mc.player.getTilePos()
x = pos.x+3
y = pos.y
z = pos.z+3

ghostHouse = Building(x,y,z,10,6,8)
ghostHouse.build()

time.sleep(30)

ghostHouse.clear()
ghostHouse.x = 8
