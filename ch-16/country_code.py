from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit code for given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # If country not found, return None
        else:
            return None

# Test method
print(COUNTRIES)
print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Zambia'))


