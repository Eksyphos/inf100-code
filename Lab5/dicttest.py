mydict = {
    'movedirection':[
            {
        'Up': 'north',
        'Right': 'east',
        'Down':'south',
        'Left':'west',
        },
            {
        'w': 'north',
        'd': 'east',
        's':'south',
        'a':'west',
        },
        [1,2,3,4,5],
        [1,2,3,4,5,6],
    ],
    'otherdict':[1,2,3,4,5],
    'third':'sweat'
                }

for key in mydict:
    if type(mydict[key])==list:
        print (type(mydict[key]))
        for i in range(len(mydict[key])):
            print (mydict[key][i])

# for val in mydict:
#     print (val)

# listlist = [[1,2,3,4],[5,6,7,8]]
# for index in listlist:
#     print (set,i)


# print (listlist)


# direction = ['','']
# eventkey = 'a'
# i = 1
# if eventkey in mydict['movedirection'][i]:
#         direction[i] = mydict['movedirection'][i][eventkey]

# print (direction)

# mylist = [0,1,2,3,4,5,6,7,8,9,10,11,12]
# newlist=[]
# for val in mylist:
#     newlist.append(val%3)

# print (mylist)
# print (newlist)
