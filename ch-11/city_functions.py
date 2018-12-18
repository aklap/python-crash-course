"""Functions related to cities."""


def format(city, country, population=''):
    """Join city and country in one string."""
    formatted_str = city.title() + ', ' + country.title()

    if population:
        formatted_str += ' - '
        formatted_str += population

    return formatted_str