# Test to update and commit and push!  #



# Dictionary syntax:

names={569:"Aya",237:"Rania",256:"Raneem",5:"Fawzi"}
print(names[237])
names[174]="Khaled"         #new key
names[569]="Aya H."         #Existing key (change value)
del names[256]
print(names)

specs = {"DS":1,"CS":1,"SE":3,"IS":2}
specs["DS"]+=3

print("VR" in specs)        #Flase
print("DS&AI" in specs)     #True : Chicking if the element is in dictionary or not...if it is exist>> spec[] +=1
print("VR" not in specs)    #True : Chicking if it is in dictionary or not... if it not exist>> spec[] =1 (next lecture)!
print("DS" not in specs)    #Flase
print(specs)
for v in specs:
    print(v,specs[v])

