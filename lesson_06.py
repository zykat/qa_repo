## DATA Structures in Python ###
#
# -- List --- spisok -- changeable
#
my_list = ['test1','test2', 'test3']
print(f'my_list: {my_list}')
# print(f'3rd element of my_list: {my_list[2]}')
# ###
# for i in  my_list:
#     print(i)
# ###
# my_list[0] = 2948
# my_list[2] = True
# print(f'new my_list: {my_list}')
# ###
# print(len(my_list))
# ###
# my_list.append(4567)
# print(f'edited my_list: {my_list}')
#
# -- Tuple -- kortege -- unchangeable
my_tuple = (6789,'test2', 'test3')
print(f'my_tuple: {my_tuple}')
# print(f'2nd element of my_tuple: {my_tuple[1]}')
#
### DICTIONARY --- slovari -- changeable
my_dictionary = {
    "name": "John",
    "last_name": "Doe",
    "DOB": "2022-03-30",
    "Feature": "Likes Python!"
}
print(f'my dictionary: {my_dictionary}')
#
# my_dictionary['name'] = "Fenix"
# print(my_dictionary)
#
# my_dictionary2 = {
#     "name": "John",
#     "Name": "Ricky HO",
#     "last name": "Doe",
#     "DOB": "2022-03-30",
#     "Feature": "Likes Python!",
#     555: "integer",
#     "list colors": ["red", "green", "blue"]
# }
# print(my_dictionary2)
# print(my_dictionary['DOB'])
# print(len(my_dictionary['DOB']))
#
### SET -- mnozhestva -- print just unique values
#
my_set = {'element1', 'element2', 'element3'}
my_set2 = {'element1', 'element2', 'element3','element1', 'element2'}
print(f'my_set: {my_set}')
print(f'my_set2: {my_set2}')
print(len(my_set2))