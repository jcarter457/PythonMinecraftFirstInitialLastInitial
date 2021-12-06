from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z

def getWoolState(color):
    if color=="pink":
        blockstate=6
    elif color=="lime":
        blockstate=5
    elif color=="orange":
        blockstate=1
    else:
        blockstate=0
    return blockstate
colorString=input("Enter a block color: ")
state=getWoolState(colorString)

mc.setBlock(x,y,z,35,state)
        