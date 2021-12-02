from mcpi.minecraft import Minecraft
mc = Minecraft.create()

air=0
water=9
dirt=3

while True:
    pos = mc.player.getTilePos()
    blockBelow=mc.getBlock(pos.x,pos.y-1,pos.z)
    if blockBelow!=air and blockBelow!=water and blockBelow!=dirt and blockBelow!=2:
        mc.setBlock(pos.x,pos.y-1,pos.z,41)
    elif blockBelow==dirt:
        mc.setBlock(pos.x,pos.y-1,pos.z,2)
    