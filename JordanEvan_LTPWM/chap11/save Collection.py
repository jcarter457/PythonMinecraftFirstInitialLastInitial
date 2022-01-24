import pickle


structureName = input("what for you want to call the structure?")

pickleFile = open("pickleFile", "wb")
pickleFile.dump(structure)