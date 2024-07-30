#Creating a List
my_list = [1, 2, 3, 4, 5]
#Adding an element to the List
my_list.append(6)
#Removing an element from the List
my_list.remove(4)
#Modifying an element in the List
my_list[0] = 10
print("updated list:",my_list)

#Creating a dictionary
my_dict = {'name': 'Govind', 'age': 23, 'city': 'Rudrapur'}
#Adding
my_dict['gender'] = 'Male'
#Removing
del my_dict['age']
#Modifying
my_dict['city'] = 'Bhimtal'
print("Updated Dictionary:", my_dict)

#Creating a set
my_set = {1,2,3,4,5,6}
#Adding
my_set.add(7)
#Removing
my_set.remove(2)
#Modifying
my_set.discard(3)
my_set.add(8)
print ("Updated Set:" , my_set)