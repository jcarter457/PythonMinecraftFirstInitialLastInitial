from pickle import dump
locations = {'John': 'Forest','Phillipa':'Mountains','Pete':'City'}

secretFile=open("secretFile2.txt","wb")
dump(locations,secretFile)