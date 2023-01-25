#list
oreoList = [0,1,2,3]
print(oreoList) 
#loop
for x in oreoList:
    print(x)
#append
oreoList.append(4)
for x in oreoList:
    print(x)

print(oreoList)
# copy of list
crumbList = oreoList
print(crumbList)

#new list for concatenating with previous list
jumbleList = [5,6,7,8,9]
print(jumbleList)

#concatenate
for j in jumbleList:
    crumbList.append(j)
print(crumbList)

#reverse
crumbList.reverse()
print(crumbList)

