"""Ch 8."""
# import profile
# from profile import car_profile
# from profile import car_profile as cp
# import profile as pf
from profile import *
# 8-1


# def display_message():
#     """Print a string."""
#     print("I'm learning about functions.")

# display_message()

# 8-2


# def favorite_book(title):
#     """Print favorite book title as string."""
#     print("One of my favorite books is " + title + '.')

# favorite_book('Thus Spake Zarathustra')

# 8-3


# def make_shirt(size="Large", text="I love Python"):
#     """Print size and text of tshirt."""
#     print('You ordered a shirt in ' +
#           size +
#           ' and with the text: ' +
#           text)

# make_shirt('Medium', 'Alexis is a great programmer!')
# make_shirt()
# make_shirt('Medium')
# make_shirt('X-Small', 'I love dogs!')

# 8-5


# def describe_city(city, country='USA'):
#     """Print city and country in string."""
#     print(city.title() + ' is in ' + country.title())

# describe_city('NYC')
# describe_city('SF')
# describe_city('Seattle')
# describe_city('Montreal')

# 8-6


# def city_country(city, country):
#     """Return concatenated string with city, country."""
#     return city.title() + ', ' + country.title()

# print(city_country('new york city', 'united states'))
# print(city_country('paris', 'france'))
# print(city_country('london', 'united kingdom'))

# 8-7


# def make_album(artist, album, tracks=1):
#     """Return dictionary containing artist, album."""
#     album = {
#         'name': artist,
#         'title': album,
#         'tracks_count': tracks,
#     }

#     return album

# print(make_album('NIN', 'Pretty Hate Machine'))
# print(make_album('Beatles', 'Abbey Road'))
# print(make_album('Kanye West', 'Kandhi'))

# print(make_album('High Functioning Flesh', 'Stuff', 10))

# while True:
#     print('Answer the questions to save info
            # About your music collection.
            # To quit, answer \'q\' at any time.')

#     artist = input('What is the artist?\n')

#     if artist == 'q':
#         break

#     album = input('What is the album title?\n')

#     if album == 'q':
#         break

#     print('Added ' + artist.title() + '\'s' + album.title())

# make_album(artist, album)

# 8-9
# magicians = ['Eugene', 'Fred', 'Harriet']


# def show_magicians(names):
#     """Print name of each magician."""
#     for name in names:
#         print(name)

# show_magicians(magicians)

# 8-10


# def make_great(names):
#    """Appends the string "the Great" to each name given"""

    # for name in names:
    #     current_magician = names.pop(0)
    #     names.append(current_magician + ' the Great!')

# make_great(magicians)
# show_magicians(magicians)

# make_great(magicians[:])
# show_magicians(magicians)

# 8-12


# def sandwich_order(*items):
#     """Prints summary of a sandwich order."""
#     print('You ordered a sandwich with:\n')

#     for item in items:
#         print(item)

# sandwich_order('pickles', 'ham', 'mayo')
# sandwich_order('turkey', 'cranberry relish', 'mash potatoes', 'gravy')
# sandwich_order(
#         'peanut butter', 'cinnamon', 'bananas',
#         'marshmallow'
# )


# def build_profile(first, last, **info):
#     """Prints information from a user."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last

#     for k, v in info.items():
#         profile[k] = v

#     return profile

# print(build_profile('alexis', 'lp', pets='bentley', location='nyc'))

# def car_profile(manufacturer, model, **info):
#     """Builds and prints a car's profile."""
#     profile = {}
#     profile['manufacturer'] = manufacturer
#     profile['model'] = model

#     for key, val in info.items():
#         profile[key] = val

#     return profile

# 8-15

# print(profile.car_profile('Ford', 'Model T', color='black', doors='4'))
# print(car_profile('Ford', 'Model T', color='black', doors='4'))
# print(cp('Ford', 'Model T', color='black', doors='4'))
# print(pf.car_profile('Ford', 'Model T', color='black', doors='4'))
print(car_profile('Ford', 'Model T', color='black', doors='4'))
