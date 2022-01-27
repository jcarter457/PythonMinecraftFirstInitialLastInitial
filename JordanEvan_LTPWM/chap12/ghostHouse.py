from pcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

class Building(object):
    def__init__(self,x,y,z,width, height, depth):
        self.x = x
        self.y = y
        self.z = z
        
        self.width = width
        self.height = height
        self.depth = depth