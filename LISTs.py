print("learning lists")
#lists are datastructure
#initializing lists
#collection of stuff in a order
l=[1,2,3]
#can print the entire list of
print(l)



#can hold mixture of datatypes unlike arrays and can also hold another list
a=[1,'s',"string",1.222,[1,2,"super"]]
 #for loop for printing the elements of the lists   
for i in range(len(a)):
    print(a[i])


print("few functions in the lists ")
names=["subbu","john","james"]
print (names)
#this function adds an element to the existing as a last element of list
#you can use it when dont care about the order in which the elements are arranged
names.append("virat Kholi")
print(names)


#this function enables to add an element to the list at a  particular index in a list
#you can use it when order matters 
names.insert(1,"pandey")
print (names)

#this function removes the element from the list
#note that paramaters you pass is case sensitive 
names.remove("john")
print(names)

#this function reverses the order of the list
names.reverse()
print(names)

numbers=[10,4,7,23,45]
#this function sorts the elements of the list in ascending order by default
numbers.sort()
print(numbers)

