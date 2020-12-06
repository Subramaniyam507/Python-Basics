print("learning tuple")
#similar to lists but they are immutable
#sometimes few things should be immutable 
credit_card1=(123123212212221,"joe rogan","11/20",123)
credit_card2=(122332233444444,"subbu","11/21",133)
#you can have list of tuples 
#you can have more number of tuples in a list but you cannot change anything that is tuple
credit_cards=[credit_card1,credit_card2]
print(credit_cards)

person1=("subbu",25,"pizza")
person2=("ramesh",29,"vada")
#unpacking tuples
#name,age,favfood=personTuple
#print(name)
#print(age)
# print(favfood)

#unpacking via for loop
#creating a list of people
people=[person1,person2]

for name,age,favfood in people:
    print(name)
    print(age)
    print(favfood)
    print()



