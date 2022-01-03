import pickle
secretFile=open("secretFile2.txt","rb")
locations=pickle.load(secretFile)
print(locations)