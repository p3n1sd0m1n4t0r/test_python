list_name = ['John Carter', 'Verossica Maiden', 'Rick Sanchez']
print(list_name[1]) #index starts its count from 0, not from 1!!!#
print(list_name[-1]) #you can select indexes from the end of a list, for ex. -1(last), -2, -3 and so on#

for name in list_name: #if the name is in a list#
    print(name)

list_name.append('Jessus Christ') #.append is a method to add an item#
print(list_name)

list_name.pop() #.pop is a method to delete last item#
print(list_name)

verelable_name = list_name.index('Rick Sanchez') #.index shows index number of an item#
print(verelable_name)

print(len(list_name)) #len shows length of a list, how many items do we have there#