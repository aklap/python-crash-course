from collections import OrderedDict


ordered_dict = OrderedDict()


def glossary(word, definition):
    """Prints definition of a term."""
    ordered_dict[word] = definition
    print('Added ' + word + '!')

# Exercises
# glossary('cat1', 'feline animal')
# glossary('dog2', 'canine animal')
# glossary('keyboard3', 'input device')

# for word, definition in ordered_dict.items():
#     print(word.title() + ' ' + definition)
