import json

# Load data into a list
filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)
    
    # For each JSON objecect in the list of JSON
    for pop_dict in pop_data:
        # If the value in the current json obj for key 'Year' is 2010
        if pop_dict['Year'] == '2010':
            # Grab the values for name and population
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))  # Drop decimal
            row = pop_dict
            print(country_name + ": " + str(population))

