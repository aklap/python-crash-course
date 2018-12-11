"""Ch 8."""

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


def make_album(artist, album, tracks=1):
    """Return dictionary containing artist, album."""
    album = {
        'name': artist,
        'title': album,
        'tracks_count': tracks,
    }

    return album

# print(make_album('NIN', 'Pretty Hate Machine'))
# print(make_album('Beatles', 'Abbey Road'))
# print(make_album('Kanye West', 'Kandhi'))

# print(make_album('High Functioning Flesh', 'Stuff', 10))

while True:
    print('Answer the questions to save info about your music collection. To quit, answer \'q\' at any time.')

    artist = input('What is the artist?\n')

    if artist == 'q':
        break

    album = input('What is the album title?\n')

    if album == 'q':
        break

    print('Added ' + artist.title() + '\'s' + album.title())

make_album(artist, album)