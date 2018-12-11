"""Ch 7."""

# 7-1
# car = input('What kind of car would you like?\n')

# print('Let me see if I can find you a ' + car + '.')

# 7-2
# group_size = input('How many in your group?\n')

# if int(group_size) > 8:
#     print('You\'ll need to wait.')
# else:
#     print('Your table is ready!')

# 7-3
# num = input('Please give me a number\n')

# if int(num) % 10 == 0:
#     print('Hey, that\'s a multiple of 10!')
# else:
#     print('No, that\'s not a multiple of 10.')

# 7-4
# active = True

# while active:
#     topping = input('Please enter a topping:\n')

#     if topping.lower() == 'quit':
#         active = False
#     else:
#         print('Added ' + topping + '!')

# 7-5
# while True:
#     age = input('What is your age?\n')

#     if age.lower() == 'quit':
#         break
#     elif int(age) < 3:
#         print('Your ticket is free')
#     elif int(age) >= 3 and int(age) <= 12:
#         print('Your ticket is $10')
#     elif int(age) > 12:
#         print('Your ticket is $15')

# 7-7
# while True:
#     print('running to infinity!')

# 7-8
# sandwich_orders = ['pbj', 'BLT', 'grilled cheese', 'salami', 'turkey']
# 7-9
# sandwich_orders = [
#     'PBJ',
#     'pastrami',
#     'BLT',
#     'pastrami',
#     'grilled cheese',
#     'salami',
#     'turkey',
#     'pastrami'
# ]

# finished_sandwiches = []

# print('Deli ran out of pastrami!')

# while sandwich_orders:
#     current_order = sandwich_orders.pop(0) # .pop the first el not last

#     if current_order == 'pastrami':
#         continue # pastrami already removed, start loop over
#     else:
#         print('I made your ' + current_order + ' sandwich.')
#         finished_sandwiches.append(current_order)

# print('\nFinished all orders!')

# 7-10
# poll_active = True
# responses = {}

# while poll_active:
#     name = input('What is your name?\n')
#     dream_vacation = input('What is your dream vacation?\n')
#     responses[name] = dream_vacation

#     repeat = input('Anyone else want to respond?\n')

#     if repeat.lower() == 'no':
#         poll_active = False

# for name, response in responses.items():
#     print(name.title() + ' responded: ' + response.title())
