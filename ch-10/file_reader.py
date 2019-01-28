filename = './pi_digits.txt'

with open(filename) as file_object:
    # Exercise 1
    # contents = file_object.read()
    # print(contents.rstrip())

    # Exercise 2
    # for line in file_object:
    #     print(line.rstrip())

    # Exercise 3
    lines = file_object.readlines()
    pi_string = ''

for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter bday as mmddyy:\n")

if birthday in pi_string:
    print('Bday appear in pi!')
else:
    print('No bday in pi!')

