"""CH 6."""

# 6-1
# bentley = {
#     'species': 'dog',
#     'age': 18,
#     'eye_color': 'black',
#     'hair': 'salt and pepper',
# }

# for info in bentley:
#     print(info + ' ' + str(bentley[info]))

# 6-2
# favorite_nums = {
#     'jen': 3,
#     'jason': 13,
#     'trevor': 33,
#     'john': 41,
#     'franka': 2,
# }

# for person in favorite_nums:
#     print(person.title() +
#           "'s fav number is " +
#           str(favorite_nums[person]))

# 6-3
# glossary = {
#     'dictionary': 'data structure that holds data as values and uses keys to access those values',
#     'list': 'data structure that stores values and their position as indices',
#     'tuple': 'data structure that is immutable and can hold any value and remember their position as index',
# }

# for term in glossary:
#     print(term.title() + ": " + glossary[term].title())

# 6-5
# rivers = {
#     'nile': 'egypt',
#     'hudson': 'ny',
#     'danube': 'germany',
# }

# for river, country in rivers.items():
#     print(river.title() + ' runs through ' + country.title() + '.')

# for river in rivers.keys():
#     print(river.title())

# for country in rivers.values():
#     print(country.title())

# 6-6
# votes = {
#     'jen': 'c',
#     'trevor': 'ocaml',
#     'alexis': 'js',
# }

# people = ['jen', 'alexis', 'john', 'ellis']

# for person in people:
#     if person in votes.keys():
#         print('Thank you for voting, ' + person.title() + '!')
#     else:
#         print('Please take our poll, ' + person.title() + '!')

# 6-7
people = []
jen = {
    'name': 'jen',
    'location': 'nyc',
    'car': 'dodge caravan',
}

trevor = {
    'name': 'trevor',
    'location': 'california',
    'car': 'tesla',
}

kim = {
    'name': 'kim',
    'location': 'philly',
    'car': 'jaguar',
}

people.append(jen)
people.append(trevor)
people.append(kim)

for person in people:
    print(person['name'].title())

    for trait in person:
        print(trait)