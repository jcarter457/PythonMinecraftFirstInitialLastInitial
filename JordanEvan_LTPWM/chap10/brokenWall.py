from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

def broken():
    brokenBlocks=[48,67,4,4,4,4]
    block = random.choice(brokenBlocks)
    return block

pos = mc.player.getTilePos()
x,y,z = pos.x, pos.y, pos.z

brokenWall = []
height, width = 5, 10

for outer in range(10):
    brokenWall.append([])
    for inner in range(10):
        wall = random.randint(2,4)
        brokenWall[outer].append(wall)
        
mc.setBlock(x,y,z,)