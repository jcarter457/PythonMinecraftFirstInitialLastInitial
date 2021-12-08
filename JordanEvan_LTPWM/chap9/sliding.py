from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time
import random

pos = mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z


while True:
    x+=random.uniform(-0.2,0.2)
    z+=random.uniform(-0.2,0.2)
    y=mc.getHeight(x,z)
    mc.player.setPos(x,y,z)
    time.sleep(0.02)
    
    