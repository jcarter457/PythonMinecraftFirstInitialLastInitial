from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    return 103
def water():
    return 9
def wool():
    return 35
def lava():
    return 11
def TNT():
    return 46
def flower():
    return 38
def diamondBlock():
    return 57

block=melon()

pos = mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z

mc.setBlock(x,y,z,block)