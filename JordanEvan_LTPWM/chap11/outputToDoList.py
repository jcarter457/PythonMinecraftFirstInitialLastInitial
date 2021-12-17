from mcpi.minecraft import Minecraft
mc=Minecraft.create()

toDoList=open("toDo.txt","r")

for line in toDoList:
    mc.postToChat(toDoList.readline())