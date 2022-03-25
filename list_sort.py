list_name = [102, 76, 18, 81, 46]
list_name.sort() #you can add other parameters to method 'sort'#
print(list_name)

list_name.sort(reverse=True) #sorting a list upside down (from the end)#
print(list_name)

list_name[2] = 'Young girl!!!' #'2' is idex of an item i want to change#
#list_name.sort() in this case if sort is emty there will be an error, because different time: str nd int#
print(list_name)