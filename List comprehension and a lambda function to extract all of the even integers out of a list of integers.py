#Question 3
#Use list comprehension and a lambda function to extract all of the even integers out of a list of integers


tables = [lambda x=x: x*1 for x in range(1, 20)]
for table in tables:
  print(table())   
