
# dictionaries are unique and unordered
my_dict = {'name':'montek','age':(25,1,5),'name':'montek_verma'} # keys can be inetegers too
print(my_dict)


# list of dictionaries

dict_list = [
		{'name':'montek','age':25},
		{'name':'montek1','age':26},
		{'name':'montek2','age':27},
		{'name':'montek3','age':28},
		{'name':'montek4','age':[1,2,3,45,6]}		
]	
print(dict_list)

dict_dict = {
	'dict1' : {'name':'montek','age':25},
	'dict2' : {'name':'montek1','age':26},
}
print(sum(my_dict['age']))
dict_list[4]['name']='xyz'
print(dict_list)

demo = (1,2,3,4,5)
print("sum is : ",sum(demo))