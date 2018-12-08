# 4-1
pizzas = ['margherita', 'pepperoni', 'plain', 'sausage', 'mushroom', 'prosciutto', '4 cheese', 'white', 'veggie']
# for pizza in pizzas:
#     # print(pizza + '\n')
#     print('I like ' + pizza + ' pizza.\n')

# print('I really like pizza!')

# 4-2
# mammals = ['playtpus', 'dolphin', 'man']

# for mammal in mammals:
#     # print(mammal)
#     print('A ' + mammal + ' would make a great pet.')

# print('All these animals are mammals.')

# 4-3
# for num in range(1, 21):
#     print(num)

# 4-4
# print([i for i in range(1, 1000001)])

# 4-5
# mil_list = [i for i in range(1, 1000001)]

# print(max(mil_list))
# print(min(mil_list))
# print(sum(mil_list))

# 4-6
# Create list of ints from 1-20
# nums = [i for i in range(1, 21)]

# # Loop through nums
# for num in nums:
#     # Check the current int is not even
#     if num % 2 != 0:
#         print(num)

# 4-7
# threes = [i for i in range(3, 31, 3)]

# for i in threes:
#     print(i)

# 4-8
# cubes = [i**3 for i in range(1, 11)]

# for i in cubes:
#     print(i)

# 4-9
# see above

# 4-10
# print('The first 3 items are:')
# print(pizzas[:3])
# print('The middle 3 items are:')
# print(pizzas[3:6])
# print('The last 3 items are:')
# print(pizzas[-3:])

# 4-11
# friend_pizzas = pizzas[:]

# pizzas.append('goat cheese')
# friend_pizzas.append('anchovy')

# print('My favorite pizzas are:\n')
# for pizza in pizzas:
#     print(pizza)

# print('My friend\'s favorite pizzas are:\n')
# for pizza in friend_pizzas:
#     print(pizza)

# 4-12
# ? Already did this above

# 4-13
foods = ('kung pao chicken', 'noodles', 'rice', 'roast duck', 'greens')

for food in foods:
    print(food)

# foods[0] = 'bao'

foods = ('tofu', 'bao', foods[2], foods[3], foods[4])

for food in foods:
    print(food)
