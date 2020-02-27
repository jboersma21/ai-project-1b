"""
Project Part 1b

Team 6

Colin Moody, Ohad Beck, Charlie MacVicar, Jake Boersma

"""

import sys
import initial_state
import Country


class World:

    def __init__(self, d_bound, weight_dict, country_dict):
        self.num_country = len(country_dict)  # number of countries in the world
        self.d_bound = d_bound  # deepest level at which successors are generated
        self.weights = weight_dict  # resources and their corresponding weights
        self.countries = {}  # dictionary of country objects

        for country in country_dict:
            name = country
            resources = country_dict[country]  # resources for specific country
            new_country = Country.Country(name, resources, weight_dict)  # create country object with name and resources
            self.countries[name] = new_country  # add country object to countries dictionary

    def print_search_state(self):
        for country in self.countries:
            country_obj = self.countries[country]
            print(country)
            for resource in country_obj.resources:
                print('\t' + resource, country_obj.resources[resource])


def main(argv):
    weights = initial_state.create_resource_dict()
    print(weights)

    countries = initial_state.create_country_dict()
    print(countries)

    d_bound = 3

    new_world = World(d_bound, weights, countries)
    # print(new_world.weights)
    # print(new_world.num_country)
    # print(new_world.d_bound)
    country1 = new_world.countries['Atlantis']
    # print(country1.resources)
    print(country1.weights)


    new_world.print_search_state()
    print(country1.little_u())

if __name__ == "__main__":
    main(sys.argv)
