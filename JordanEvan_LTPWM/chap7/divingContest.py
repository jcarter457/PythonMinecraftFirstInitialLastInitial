from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
pos= mc.player.getPos()
highscore=0

while True:
    ndwquovbg=input("Start")
    score=0
    pos= mc.player.getPos()
    blockAbove=mc.getBlock(pos.x,pos.y+2,pos.z)
    
    while blockAbove==8 or blockAbove==9:
        time.sleep(1)
        pos=mc.player.getPos()
        blockAbove=mc.getBlock(pos.x,pos.y+2,pos.z)
        score = score+1
        mc.postToChat("Current score: " + str(score))
    
    mc.postToChat("Final score: " + str(score))
    
    if score>6:
        finalPos=mc.player.getTilePos()
        mc.setBlocks(finalPos.x-5, finalPos.y+10, finalPos.z-5,finalPos.x+5, finalPos.y+10, finalPos.z+5,38)
    if score>highscore:
        finalPos=mc.player.getTilePos()
        mc.setBlock(finalPos.x,finalPos.y-1,finalPos.z,41)
        highscore=score