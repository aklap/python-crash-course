from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit code for given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None  # Tricky! Indent once more and it will almost always fail

# Test method
# print(get_country_code('Andorra'))
# print(get_country_code('Afghanistan'))
# print(get_country_code('United Arab Emirates'))