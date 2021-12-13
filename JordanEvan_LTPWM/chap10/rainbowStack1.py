from mcpi.minecraft import Minecraft
mc = Minecraft.create()

oneDimensionalRainbowlist = [1,2,3,4,5]

pos = mc.player.getTilePos()

x = pos.x+1
y = pos.y
z = pos.z

for color in oneDimensionalRainbowlist:
    mc.setBlock(x,y,z,35, color)
    y +=1