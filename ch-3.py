# 3-1 Names
# names = ['alexis', 'leah', 'chloe']
# print(names[0], names[1], names[-1])

# 3-2 greetings
# message = ', good morning!'
# print(names[0] + message)
# print(names[1] + message)
# print(names[2] + message)

# 3-3 own list
# vehicles = ['hot air balloon', 'Jaguar x-type', 'Hearse']
# print("I would like to own a " + vehicles[0])
# print("I would like to own a " + vehicles[1])
# print("I would like to own a " + vehicles[2])

# 3-4
guests = ['Einstein', 'Turing', 'Lovelace']

# print('Hi ' + guests[0] + ', please meet me for a wonderful dinner at 8 tonight!')
# print('Hi ' + guests[1] + ', please meet me for a wonderful dinner at 8 tonight!')
# print('Hi ' + guests[2] + ', please meet me for a wonderful dinner at 8 tonight!')

# 3-5
# print('Oops! Looks like ' + guests[1] + ' can\'t make it tonight.')

guests[1] = 'Knuth'

# print('Hi ' + guests[0] + ', please meet me for a wonderful dinner at 8 tonight!')
# print('Hi ' + guests[1] + ', please meet me for a wonderful dinner at 8 tonight!')
# print('Hi ' + guests[2] + ', please meet me for a wonderful dinner at 8 tonight!')

# 3-6
# print('Found a bigger table for tonight! The more the merrier!')

guests.insert(0, 'Hopper')
guests.insert(2, 'Liskov')
# guests.insert(len(guests), 'Johnson')
guests.append('Johnson')

# print(guests)

# print('Hi ' + guests[0] + ', please meet me for a wonderful dinner at 8 tonight!')
# print('Hi ' + guests[1] + ', please meet me for a wonderful dinner at 8 tonight!')
# print('Hi ' + guests[2] + ', please meet me for a wonderful dinner at 8 tonight!')
# print('Hi ' + guests[3] + ', please meet me for a wonderful dinner at 8 tonight!')
# print('Hi ' + guests[4] + ', please meet me for a wonderful dinner at 8 tonight!')
# print('Hi ' + guests[5] + ', please meet me for a wonderful dinner at 8 tonight!')

# 3-7
# print('Sorry folks, can only invite 2 people tonight.')

# uninvited = guests.pop()
# print('So terribly sorry, ' + uninvited + ', I must request you not come tonight. Another time!')
# uninvited = guests.pop()
# print('So terribly sorry, ' + uninvited + ', I must request you not come tonight. Another time!')
# uninvited = guests.pop()
# print('So terribly sorry, ' + uninvited + ', I must request you not come tonight. Another time!')
# uninvited = guests.pop()
# print('So terribly sorry, ' + uninvited + ', I must request you not come tonight. Another time!')
# print('\nI request your presence tonight, ' + guests[0] + ' for a wonderful dinner.')
# print('\nI request your presence tonight, ' + guests[1] + ' for a wonderful dinner.')
# del guests[0]
# del guests[0]

# print(guests)

# 3-8
# destinations = ['tahiti', 'senegal', 'japan', 'mongolia', 'germany']
# print(destinations)

# print(sorted(destinations))
# print(destinations)
# print(sorted(destinations, reverse=True))
# print(destinations)
# destinations.reverse()
# print(destinations)
# destinations.reverse()
# print(destinations)
# destinations.sort()
# print(destinations)
# destinations.sort(reverse=True)
# print(destinations)

# 3-9
# print("I'm inviting " + str(len(guests)) + " people to dinner tonight.")

# 3-10
# cities = ['nyc', 'la', 'portland', 'austin']

# print('Cities sorted a-z:')
# print(sorted(cities)) # NOTE: sorted FUNCTION returns a value, a copy of the changed argument
# print('Cities sorted z-a')
# print(sorted(cities, reverse=True))
# print('Cities destructively sorted a-z')
# cities.sort() # NOTE: the sort METHOD called on the object, an array, does NOT return anything
# print(cities)
# print('Cities destructively sorted in reverse')
# cities.sort(reverse=True)
# print(cities)
# print('Cities reversed destructively back to a-z')
# cities.reverse() # NOTE: the reverse METHOD called on the object, an array, does NOT return anything
# print(cities)
# print('Cities reversed destructively z-a')
# cities.reverse()
# print(cities)


