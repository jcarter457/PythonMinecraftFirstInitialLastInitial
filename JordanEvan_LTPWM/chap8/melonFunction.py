from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def melon():
    pos = mc.player.getPos()
    x=pos.x
    y=pos.y
    z=pos.z
    dist=1
    seconds=5
    block=103
    mc.setBlock(x,y-dist,z,block)
    time.sleep(seconds)
    
while True:
    melon()