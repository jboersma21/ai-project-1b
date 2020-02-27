"""
Project Part 1b

Team 6

Colin Moody, Ohad Beck, Charlie MacVicar, Jake Boersma

"""

import sys
import initial_state

class world():

    def __init__(self, num_country, d_bound, weights, countries):
        self.num_country = num_country
        self.d_bound = d_bound
        self.weights = weights
        self.countries = countries


def main(argv):
    weights = initial_state.create_resource_dict()
    initial_state.print_resource_dict(weights)

    countries = initial_state.create_country_dict()
    initial_state.print_country_dict(countries)


if __name__ == "__main__":
    main(sys.argv)
