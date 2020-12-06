print("learning dictionaries")
#dictionary doesnt have indexes
#you can name indexes as names not in numbers 
dictionaries_1={'bananas':5,'oranges':3}
#for each element (bananas 5)
#banan=KEYS,5=VALUE
#keys are like indexes
print(dictionaries_1['bananas']) #RETURNS 5 JUST LIKE ARRAY HERE INSTEAD OF ZERO AS INDEX BANANAS ARE INDEX

#THIS METHOD RETURNS VALUE FOR A GIVEN KEY IF THE PARTICULAR KEY IS FOUND 
#else it will return "none"
print(dictionaries_1.get('bananas'))
print(dictionaries_1.get('hello')) 
#EACH KEY IN DICTIONARY CAN STORE LISTS ALSO and also a dictionery THATS COOL!!!!!!!!!!
contacts_dictionary ={
    'subbu': ['344557','subbu@gamail.com'],
    'ramu' : ['344344','ramu@gamail.com']
}
print(contacts_dictionary['subbu'])
print(contacts_dictionary['ramu'])
#to count the numbers of time the words are repeated
sentence ="I like the name Subbu because the name Subbu is the best"
word_counts={
    'I':1,
    'like':1,
    'the':1,
    'name':1,
    'Subbu':1,
    'because':1,
    'is':1,
    'best':1
}
#dict.items()
#returns list of tuples
print(word_counts.items())
#dict.keys
#returns list of keys
print(word_counts.keys())
#dict.values()
#returns list of values
print(word_counts.values())


#dict.pop()
#deletes the elements of the dictionary call it keys
word_counts.pop('like')
print(word_counts)
#dict.popitem
#deletes the elements of the dictionary last KEYS
word_counts.popitem()
print(word_counts)

#how to add new elements to the dictionary
word_counts['psycho']=2
print(word_counts)

#dict.clear()
#deletes all contents of the dictionary
word_counts.clear()
print(word_counts)