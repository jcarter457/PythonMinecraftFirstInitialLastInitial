from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x+5
y = pos.y
z = pos.z
width = 10
height = 5
length = 6
blockType = 4
air = 0
mc.setBlocks(x,y,z,x+width,y+height,z+length,blockType)
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1,air)


gift=mc.getBlock(pos.x,y-1,z)
if gift==57:
    mc.setBlocks(x,y+1,z+4,x,y+2,z+3,air)
else:
    mc.postToChat("Place a offering on the pedistal")