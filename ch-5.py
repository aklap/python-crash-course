"""Chapter 5 exercises."""

# 5-1
# dog = 'Bentley'

# print("Is dog == 'Bentley'? I predict True.")
# print(dog == 'Bentley')
# print("\nIs dog == 'Lassie'? I predict False.")
# print(dog == 'Lassie')
# print('Bentley' == 'Lassie')
# print('' == '  ')
# print(False == 0)
# print(True == 1)
# print(123 == '123')
# print('cat' == 'CAT')
# print(len('cat') == len([1, 2, 4]))
# print(None == 0)
# print(None == False)
# print(1 > 0)
# print(1 > -1)
# print(-1.4 < 2)
# print(1 <= 6)
# print(1 > 0 and True)
# print(-9 < 10 or 20 < 1)

# if 1 in [1, 2, 3]:
#     print(True)

# 5-3 - 5-6
# alien_color = 'green'
# alien_color = 'red'
# alien_color = 'yellow'
# alien_color = 'grey'

# if alien_color == 'green':
#     print('Player earned 5 pts')
# elif alien_color == 'yellow':
#     print('Player earned 10 pts')
# elif alien_color == 'red':
#     print('Player earned 15 pts')
# else:
#     print('Player earned 10 pts')

# 5-6
# age = 78

# if age < 2:
#     print('You\'re a baby!')
# elif age >= 2 and age < 4:
#     print('You\'re a toddler!')
# elif age >= 4 and age < 13:
#     print('You\'re a kid')
# elif age >= 13 and age < 20:
#     print('You\'re a teen!')
# elif age >= 20 and age < 65:
#     print('You\'re an adult!')
# elif age >= 65:
#     print('You are OLD!')

# 5-7
# fruits = ['mango', 'mangosteen', 'persimmon', 'raspberries']

# if 'mango' in fruits:
#     print('have mango')

# if 'mangosteen' in fruits:
#     print('have mangosteen')

# if 'persimmon'in fruits:
#     print('have persimmon')

# if 'raspberries' or 'apples' in fruits:
#     print('have raspberries')

# if 'banana' in fruits:
#     print('have banana')
# else:
#     print('no banana')

# favorite_fruits = ['mango', 'papaya', 'blackberries']

# if 'mango' or 'apple' in favorite_fruits:
#     print('mango or apple')

# if 'papaya' in favorite_fruits:
#     print('You REALLY like papaya!')

# 5-8
# usernames = []
# usernames = ['admin', 'kitty8', 'sage92', 'warlock666', 'lotusblossom88']

# if not usernames:
#     print('No users')
# elif usernames:
#     for name in usernames:
#         if name == 'admin':
#             print('Hello admin, would you like to see the status report?')
#         else:
#             print('Hello ' + name + ', thanks for loggin in.')

# 5-10
# current_users = ['admin', 'kitty8', 'sage92', 'warlock666', 'lotusblossom88']

# new_users = [
#             'keyboard_queen77',
#             'mega_programmer90',
#             'Warlock666',
#             'lotUsblossom88'
#             ]

# for user in new_users:
#     if user.lower() in current_users:
#         print(user + ", you need a new username -- already taken.")

# 5-11
# nums = [i for i in range(1, 10)]
# print(nums)

# for i in nums:
#     if i == 1:
#         print(str(i) + 'st')
#     elif i == 2:
#         print(str(i) + 'nd')
#     elif i == 3:
#         print(str(i) + 'rd')
#     else:
#         print(str(i) + 'th')
