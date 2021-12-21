from mcpi.minecraft import Minecraft
mc=Minecraft.create()

toDoList=open("toDo.txt","r")

mc.postToChat(toDoList.read())