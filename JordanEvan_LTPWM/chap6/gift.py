from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x=10
y=11
z=12
gift=mc.getBlock(x,y,z)

if gift==57:
    mc.postToChat("Cool")
    
elif gift==6:
    mc.postToChat("Ok")
    
else:
    mc.postToChat("Bring a gift to "+str(x)+", "+str(y)+", "+str(z))
    