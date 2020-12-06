print("learning the concept of sets")
#sets are similar to list 
# no duplicates in a sets
#it is mutable
# not indexed 
#you can cast set to a list. sets will eliminate all the duplicates
#you can also list to set 
s={'blueberry','rasberry'}
print(s)
s.add('strawberry')
print(s)
s.add('blueberry')#no duplicates allowed
print(s)

list_of_numbers=[1,2,3,4,5,4,5,6,6]#allows duplicates but how to remove duplicates
set_no_duplicates=set(list_of_numbers)#casting a list to set
print(set_no_duplicates)

list_no_duplicates=list(set_no_duplicates)#casting set to list
print(list_no_duplicates)


library_1={'harry potter','hunger games','lord of the rings'}
library_2={'harry potter','Romeo and juliet'}

#union of two sets of libraries
union_of_two_sets=library_1.union(library_2)
print(union_of_two_sets)

#intersection of two sets of libraries
intersectionof_two_sets=library_1.intersection(library_2)
print(intersectionof_two_sets)

#elements that belongs only to a particular set   
elements_in_onlyset_library1=library_1.difference(library_2)
print(elements_in_onlyset_library1)

elements_in_onlyset_library2=library_2.difference(library_1)
print(elements_in_onlyset_library2)