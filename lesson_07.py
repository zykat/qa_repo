## FILES handling in PYTHON ##
# keys:
# 'r' - read file
# 'w' - write file
# 'a' - append to file
# 'x' - create file
#### read file ####
# file = open('text.txt', 'r')
# # # read file
# # print(file.read())
# # # read by row
# # print(file.readline())
# # # read first 4 signs
# # print(file.read(4))
#
# ## Cycle with file ##
# for line in file:
#     print(line)
# # close file
# file.close()

#### create and write file ####
# file = open('test1.txt','w')
# file.write('new test file')
# file.close()
# file = open('test1.txt', 'r')
# print(file.read())
# file.close()

# with open("test2.txt",'r') as file:
#     #file.write('test test text')
#     print(file.read())

### HOMEWORK ###
"""
7.1 Create a program/function that gets a parameter as a text,
    creates file "text.txt" and inserts the text into the file.
    As the result of the program/function, we have to get our file "text.txt"
    with the content from the parameter.
"""
# file = open('text.txt', 'w')
# file.write("1. new file")
# file = open('text.txt',"r")
# print(file.read())
# file.close()
###
# def create_a_file_with_text(text: str):
#     with open('text2.txt', 'w') as file:
#         file.write(text)
#
# create_a_file_with_text("text3")
# with open('text2.txt', 'r') as f:
#     print(f.read())
# f.close()
###
"""
7.2 Create a program/function that gets 2 parameters,
    first parameter a file name,
    second parameter character (letter, number) 
    and replaces all characters in the file to 0 which equals the second parameter.
    E.g. we have a file "my_text.txt" with the text "Hello Python! Lesson 7",
    we pass the second parameter as "e" to the program/function, and as the result
    text in the file will be "H0llo Python! L0sson7" 
"""
# def replace(f_name: str, letter: str)-> None:
#     with open(f_name, 'r') as file:
#          content = file.read()
#     transform = content.replace(letter, '0')
#     with open(f_name, 'w') as f:
#         f.write(transform)
# replace("text.txt", '1')
