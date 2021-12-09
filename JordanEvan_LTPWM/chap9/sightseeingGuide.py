from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {'Door':(-59.5,16,96.5), 'Spawn':(0,99,0), 'The Endless Void': (0,-99,0)}

choice=""
while choice!="exit":
    choice=input("Enter a location ('exit to close): ")
    if choice in places:
        location=places[choice]
        x,y,z=location[0],location[1],location[2]
        mc.player.setTilePos(x,y,z)