# mydict = {'movedirection':[
#                     {
#                 'Up': 'north',
#                 'Right': 'east',
#                 'Down':'south',
#                 'Left':'west',
#                 },
#                     {
#                 'w': 'north',
#                 'd': 'east',
#                 's':'south',
#                 'a':'west',
#                 }
#                 ]}
# direction = ['','']
# eventkey = 'a'
# i = 1
# if eventkey in mydict['movedirection'][i]:
#         direction[i] = mydict['movedirection'][i][eventkey]

# print (direction)

mylist = [0,1,2,3,4,5,6,7,8,9,10,11,12]
newlist=[]
for val in mylist:
    newlist.append(val%3)

print (mylist)
print (newlist)
