"""Chaper 10."""

# 10-1

with open('notes.txt') as file_object:

    print('\nRead in the entire file first:\n')

    contents = file_object.read()
    print(contents)

with open('notes.txt') as file_object:

    print("\nRead a file in line by line:\n")

    for line in file_object:
        print(line)

with open('notes.txt') as file_object:

    lines = file_object.readlines()

print('\nPrint lines stored in a list:\n')

for line in lines:
    print(line)

# 10-2

# with open('notes.txt') as f:

#     # for line in file_object:
#     #     line = line.replace('Python', 'Ruby')
#     #     print(line)

#     lines = f.readlines()

# for line in lines:
#     line = line.rstrip().replace('Python', 'Ruby')
#     print(line)

# filename = 'love.txt'

# with open(filename, 'a') as f:
#     f.write('I love finding meaning in datasets!\n')
#     f.write('I love creating apps that run in the browser!')

# 10-3
# filename = 'name.txt'

# username = input('What\'s your name?\n')

# with open(filename, 'w') as f:
#     f.write(username)

# 10-4
# with open('guest_book.txt', 'a') as f:

#     while True:
#         name = input('What is your name?\n')

#         if name == 'quit':
#             break

#         print('Hello, ' + name + '!')

#         f.write(name + '\n')

# 10-5
# filename = 'answers.txt'

# with open(filename, 'a') as f:
#     while True:
#         answer = input('Why do you like programming?\n')

#         if answer == 'q':
#             break
#         else:
#             f.write(answer + '\n')


# 10-6 10-7
# while True:
#     try:
#         first_num = input('Enter first number:\n')

#         if first_num == 'quit':
#             break

#         second_num = input('Enter second number:\n')

#         if second_num == 'quit':
#             break

#         print(int(first_num) + int(second_num))
#     except:
#         print('One of your inputs was not a number!')

# 10-8
# try:
#     with open('cats.txt') as f:
#         cats = f.read()

#     print(cats)

#     with open('dogs.txt') as f:
#         dogs = f.read()

#     print(dogs)
# except:
#     # print('File not found!')
#     pass

# 10-10
# import os

# books = os.listdir('books')

# for book in books:
#     with open('books/' + book) as f:
#         words = f.read()
#         count = words.lower().count('the')

#     print(book + ' has ' + str(count) + ' occurences of the word "the".\n')

# 10-11, 10-12
# import json

# filename = 'favorite_num.txt'

# try:
#     with open(filename) as f:
#         favorite_num = json.load(f)
# except FileNotFoundError:
#     favorite_num = input('What\'s your favorite number?\n')

#     with open(filename, 'w') as f:
#         json.dump(favorite_num, f)
# else:
#     print('I know your favorite number! It\'s ' + favorite_num + '.')
