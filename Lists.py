#Lists are ordered sequences that can hold a variety of object types. They use [] and commas to separate objects. Support indexing and slicing. 
#lists are ordered and changable. allow duplicates.

my_list = [1, 2, 3]
my_mixed_list = ['word', 1, 1.0]
print(len(my_mixed_list))
print(my_mixed_list[0])

#methods

my_mixed_list.append('six')
print(my_mixed_list)

my_mixed_list.insert(2, 'strawberries') #me insert specifikon poziten
print(my_mixed_list) 

my_mixed_list.remove('word')
print(my_mixed_list)

my_mixed_list[2] = 'grapefruit'
print(my_mixed_list)

my_mixed_list.pop(2) #specifikon qa me fshi
print(my_mixed_list)

my_mixed_list.reverse()
print(my_mixed_list)


