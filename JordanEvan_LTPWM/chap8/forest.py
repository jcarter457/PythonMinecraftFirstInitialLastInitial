from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import math

def growTree(x, y, z):
    mc.setBlocks(x, y, z, x, y+4, z, 17)
    mc.setBlocks(x-2, y+5, z-2, x+2, y+5, z+2, 18)
    mc.setBlocks(x-1, y+6, z-1, x+1, y+6, z+1, 18)

pos = mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z

mc.setBlocks(x-40,y-1,z-40,x+40,y-1,z+40, 2)


for i in range (50):
    rand=random.randint(-35,35)
    growTree(x+(i*2),y,z+rand)