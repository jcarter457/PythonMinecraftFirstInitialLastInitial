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
    
    def upgrade(self):
        
        mc.setBlocks(self.x + 1, self.y, self.z +1, self.x + self.width -1,self.y, self.z + self.depth - 1, 35, 6)
        
        #flowers
        mc.setBlocks(self.x -1, self.y, self.z -1, self.x -1, self.y , self.z + self.depth +1, 37)
        
        mc.setBlocks(self.x -1 , slef.y self.z- 1, slef.x + self.width +1 ,se;f.y, self.z - 1 ,37)
        
        mc.setblocks(self.x + self.width + 1, self.y, self.z -1, self.x + self.width + 1, self.y, self.z + self.depth + 1, 37)
        
        mc.setBlocks(self.x -1, self.y, self.z + self.depth + 1, self.s + self.wdth, self.y, self.z = self.depth +1, 37)
        
     def buildDoor(self,val):
        if val==1:
            mc.setBlock(self.x+1,self.y+2,self.z,0)
            mc.setBlock(self.x+1,self.y+1,self.z,64)
        else:
            mc.setBlock(self.x+1,self.y+1,self.z,0)
        
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
ghostHotel = Building(x,y,z,10,6,8)

ghostHotel.build()

time.sleep(30)

ghostHotel.clear()