#Question 4
#Use the next() function to find the first element in a list of dictionaries whose attribute ‘x’ = 5. Default to an empty dictionary if not found.

x = 5
emptyDict = {}
mylist = iter([x])
x = next(mylist, emptyDict)
print(x)
x = next(mylist, emptyDict)
print(x)
