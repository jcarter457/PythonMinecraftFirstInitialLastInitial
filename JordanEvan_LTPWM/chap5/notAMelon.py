from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos = mc.player.getPos()
x = 10
y = 11
z = 12
melon = 103
block = mc.getBlock(x,y,z)

notMelon = block != melon

mc.postToChat("you need to get some food:" + str(notMelon))