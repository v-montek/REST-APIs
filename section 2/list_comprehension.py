# list comprehension allows you to build lists
my_list = [x for x in range(10)] # range(5) will return a list; we could also have written my_list=[range(5)]
print(my_list)
print([x for x in range(10) if x%2==0])

x = ['sdvs','       Sdfcv','AAS       ']
y = [person.lower().strip() for person in x]
print(y)