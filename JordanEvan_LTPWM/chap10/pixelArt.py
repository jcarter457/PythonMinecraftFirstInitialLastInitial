from mcpi.minecraft import Minecraft
mc = Minecraft.create()

blocks = [[35,35,22,22,22,22,35,35,],[35,22,35,35,35,35,22,35,],[22,35,22,35,35,22,35,22,],[22,35,35,35,35,35,35,22,],[22,35,22,35,35,22,35,22,],[22,35,35,22,22,35,35,22,],[35,22,35,35,35,35,22,35,],[35,35,22,22,22,22,35,35,]]

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

for row in reversed(blocks):
    for block in row:
        mc.setBlock(x,y,z,block)
        x += 1
    y += 1
    x = pos.x