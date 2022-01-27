from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class location(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
        
bedroom = location(64,52, -8)
mc.player.setTilePos(bedroom.x,bedroom.y, bedroom.z)