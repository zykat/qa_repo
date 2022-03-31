## DATA Structures in Python ###
#
# -- List --- spisok -- changeable
#
# my_list = ['test1','test2', 'test3']
# print(f'my_list: {my_list}')
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
# my_tuple = (6789,'test2', 'test3')
# print(f'my_tuple: {my_tuple}')
# print(f'2nd element of my_tuple: {my_tuple[1]}')
#
### DICTIONARY --- slovari -- changeable
# my_dictionary = {
#     "name": "John",
#     "last_name": "Doe",
#     "DOB": "2022-03-30",
#     "Feature": "Likes Python!"
# }
# print(f'my dictionary: {my_dictionary}')
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
# my_set = {'element1', 'element2', 'element3'}
# my_set2 = {'element1', 'element2', 'element3','element1', 'element2'}
# print(f'my_set: {my_set}')
# print(f'my_set2: {my_set2}')
# print(len(my_set2))
#
### HOMEWORK ####
#
# 1) Write a program/function that prints list entities one by one. As an input use a list.
# 	e.g. print_entities(["a", "b", "c"]) should return:
# 		"a"
# 		"b"
# 		"c"
#
# ent = ["a", "b", "c"]
# def print_entities(x):
#     for i in x:
#         print(i)
# print_entities(ent)
# === +

# 2) Write a program/function that converts strings into tuples.
# 	e.g. convert("abide") should return tuple like:
# 		("a", "b", "i", "d", "e")
#
t = "abide"
# def convert(x):
#     list = []
#     for i in x:
#         list.append(i)
#     print(tuple(list))
# === -
# def convert(text):
#     new_list = []
#     for item in text:
#         new_list.append(item)
#     print(tuple(new_list))
#
# convert(t)
# ===
# def convert(x):
#     return(tuple(x))
# print(convert(t))

# 3) Write a program/function that removes duplicates and returns only unique values as a list.
# 	e.g. remove_dups("abcdadab") should return ["a", "d", "c", "b"]. Note, order of elements in the list is not important!
# t = "abcdadab"
# def remove_dups(x):
#     set = {''}
#     for i in x:
#         set.add(i)
#     list = []
#     list.append(set)
#     print(list)
# === -
# def remove_dups(text):
#     print(list(set(text)))
# remove_dups(t)
# 4) Write a program/function that collects certain data as parameters and returns a dictionary object.
# 	e.g. client("John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261") should return a dictionary object like:
# 		{
# 			"Name": "John",
# 			"Lastname": "Doe",
# 			"DOB": "01/23/1934",
# 			"Sex": "Male",
# 			"City": "San Antonio",
# 			"State": "TX",
# 			"ZipCode": "78261"
# 		}
#
# def create_client(name, last_name, dob, sex, city, state, zip_code):
#     client = {
#         "Name": name,
#         "LastName": last_name,
#         "DOB": dob,
#         "Sex": sex,
#         "City": city,
#         "State": state,
#         "ZipCode": zip_code
#     }
#     print(client)
#
# create_client("John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261")