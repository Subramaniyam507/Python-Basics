print("learning indexing slicing and striding a list or strings")
digits=[1,2,3,4,5,6,7,8,9,10,11,12]
#java doesnt allow negative indexing throw exception
#but python is great it allows negative indexing
#like if you wanna determine the 2nd last or 3rd last element of a list you can use negative indexingSlicingStriding
#which basically means you can traverse a lists or arrays in both directions in python unlike java

print(digits[-5])
#using length as a method not variable in python . coz in java length is a final variable
print(len(digits))
#slicing of a list can be done in this way
#slicing means just cutting a part of a list starting from a particular index to particular max index
#note that initial index is inclusive and final index is exclusive
print (digits[0:5])
print(digits[4:-2])


#slicing can be done in strings as well
#like substring method in java
names="Subramaniyam Narayanan"
print(names[0:12])

#striding basically means jump few elemnts of a list in a particular sequence
#starts from an initial index and prints every element after incrementing 3 indexes
print(digits[0:10:3])
#you can also stride in reverse direction the range of index should be given in reverse order as well
# dont give "0 to 10 NO TO THE END TO THE NO" doesnt make any sense 
print(digits[10:0:-2])

#slicing using loops
for i in range(0, len(digits)):
    print(digits[0:i])


window_size=7
#slicing with equal no of elements
for i in range(len(digits)-(window_size-1)):
    print(digits[i:i+window_size])