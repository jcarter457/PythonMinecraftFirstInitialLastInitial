from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class location(object):
    def _init_(self,x,y,z):
        self.x = x
        
        
bedroom = location(64,52, -8)
mc.player.setTilePos(bedroom.x,bedroom.y, bedroom.z)