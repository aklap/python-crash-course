def car_profile(manufacturer, model, **info):
    """Builds and prints a car's profile."""
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model'] = model

    for key, val in info.items():
        profile[key] = val

    return profile