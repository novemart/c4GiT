# firstName = "Martina"
# lastName = "Yusuf"
# print(firstName, lastName, sep='@')
#
# belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# belgiumList = belgium.split(',')
# print(belgiumList, firstName, sep='?')

#myList = [2, "Martina", ['apples', 'oranges'], 7.34]
# print(myList[0])
# print(myList[-1])
# print("I have", len(myList), "elements in my list")
# for element in myList:
#     print(element)
#
# print(myList[2][1])
# #myList[2] -> ['apples, oranges'] ->[1]
#
# print(myList[-2][1])
# print(myList[-2][-1])
#print(min(myList))

# myTuple = 3, "Martina", 4.5, 23454, 5432645453
# print(myTuple[-2])
# print(len(myTuple))

#myTuple[1] = "notMartina"
#myTuple = myTuple + "Hello"
# a = 5
# b = 7
#
# a, b = b, a
#a = 6+7

#unpacking
# var1, var2, var3 = myTuple
# print(var1)
# print(var2)
# print(var3)

# var1, var2, *var3, var4 = myTuple
# print(var1)
# print(var2)
# print(var3)
# print(var4)


# myList = ['apples', 'oranges', 'milk']
# #add elements to the left hand side
# myList[:0] = ['bread', 'eggs']
# print(myList)
#
# myList[:0] = ['tomatoes']
# print(myList)
#
# myList[:0] = ('biscuits',)
# print(myList)
#
# #add elements to the end
# #myList = myList + ['chocolate']
# myList += ['chocolate', 'flowers']
# print(myList)
#
# myList.append('bird food')
# print(myList)
#
# myList.extend(['cat food','butter'])
# print(myList)
#
# myList[len(myList):] = ['tea']
# print(myList)

#specific position
# myList.insert(3, 'bananas')
# print(myList)
#
# #removing elements
# del myList[2:6]
# print(myList)
#
# returnedElement = myList.pop(6)
# print(returnedElement)
#
# myList.remove('flowers')
# print(myList)

mySet = {2, 654, 7547, 35, 2, 35, 654756, 57645}
print(mySet)

myDict = {'UK': 'London', 'FR': 'Paris', 'GR': 'Athens'}
print(myDict['UK'])

myDict['GER'] = "Berlin"
print(myDict)

print(myDict.values())

for k, v in myDict.items():
    print(k)
    print(v)
