from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
import time
shwrX=x
shwrY=y
shwrZ=z

width = 5
height = 5
length = 5

if shwrX<=x and shwrY<=y and shwrZ<=z:
    mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX+width,shwrY + height, shwrZ+length,8)
    time.sleep(10)
    mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX+width,shwrY + height, shwrZ+length,0)
else:
    mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX+width,shwrY + height, shwrZ+length,0)