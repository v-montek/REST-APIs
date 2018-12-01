
grades_tuple = ('sum_t','abc',80,47,85)
grades_list = ['sum_l','abc',80,47,85] # lists are ordered

grades_list.append('hello') #adds an item at the end
grades_list.reverse()

#grades_tuple.append(12) tuples are immutable
grades_tuple=grades_tuple+(100,109)

grades_set = {70,80,90,101,101,70} # sets are unordered and unique
grades_list[0]='hell'
grades_set.add('xyz')
print((grades_list[0],grades_tuple[0],grades_set))

#set operations

set_one = {1,2,3,4,5}
set_two = {5,6,7,8,1}
print(set_one.intersection(set_two))
print(set_one.issuperset(set_two))
print(set_one.difference(set_two))
print(set_one.union(set_two).difference(set_one.intersection(set_two)))
