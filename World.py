"""
Project Part 1b

Team 6

Colin Moody, Ohad Beck, Charlie MacVicar, Jake Boersma

"""

import sys
import initial_state
import Country
import numpy as np
from scipy.stats import variation
from copy import deepcopy

from config import configuration


def gini_index(np_arr):
    """Calculate the Gini coefficient of a numpy array.
        Source Citation: https://github.com/oliviaguest/gini
    """

    if np.amin(np_arr) < 0:
        np_arr -= np.amin(np_arr)  # Values cannot be negative

    np_arr += 0.0000001  # Values cannot be 0
    array = np.sort(np_arr)  # Values must be sorted

    index = np.arange(1, array.shape[0] + 1)  # Index per array element
    n = array.shape[0]  # Number of array elements

    gini = (np.sum((2 * index - n - 1) * array)) / (n * np.sum(array))  # Gini index

    return gini


def gini_1(np_arr):
    sorted_x = np.sort(np_arr)
    n = len(np_arr)
    cumx = np.cumsum(sorted_x)
    # The above formula, with all weights equal to 1 simplifies to:
    return (n + 1 - 2 * np.sum(cumx) / cumx[-1]) / n

def gini_2(x):
    # (Warning: This is a concise implementation, but it is O(n**2)
    # in time and memory, where n = len(x).  *Don't* pass in huge
    # samples!)

    # Mean absolute difference
    mad = np.abs(np.subtract.outer(x, x)).mean()
    # Relative mean absolute difference
    rmad = mad/np.mean(x)
    # Gini coefficient
    g = 0.5 * rmad
    return g


class World(object):

    def __init__(self, d_bound, weight_dict, country_dict):
        self.num_country = len(country_dict)    # number of countries in the world
        self.d_bound = d_bound                  # deepest level at which successors are generated
        self.weights = weight_dict              # resources and their corresponding weights
        self.countries = {}                     # dictionary of country objects

        for country in country_dict:
            name = country
            resources = country_dict[country]  # resources for specific country
            new_country = Country.Country(name, resources, weight_dict)  # create country object with name and resources
            self.countries[name] = new_country  # add country object to countries dictionary

    def get_deep_copy(self):
        return deepcopy(self)

    def print_search_state(self):
        for country in self.countries:
            country_obj = self.countries[country]
            print(country)
            for resource in country_obj.resources:
                print('\t' + resource, country_obj.resources[resource])

    def little_u_array(self):
        u_lst = []
        for country in self.countries.values():
            utility = country.little_u()
            u_lst.append(utility)

        return np.array(u_lst)

    def transfer(self, exporter, destination, resource):
        if self.countries[exporter].resources[resource] < 1.0:
            return False
        self.countries[exporter].resources[resource] -= 1.0
        self.countries[exporter].resources[resource] += 1.0
        return True

    def get_big_u(self):
        # to-do: add gini computation (boersma)
        return 0


def generate_successor(current_state):
    successors = list()

    # Add every transformation for every country
    for country in current_state.countries.keys():
        for operator in configuration["transformations"]:
            tmp_world = current_state.get_deep_copy()
            if tmp_world.countries[country].transform(transformation=operator):
                successors.append((tmp_world, tmp_world.get_big_u()))

    # Add every transfer for every pair of countries (both ways)
    for exporter in current_state.countries.keys():
        for destination in current_state.countries.keys():
            if exporter != destination:
                for resource in configuration["resources"]:
                    tmp_world = current_state.get_deep_copy()
                    if tmp_world.transfer(exporter=exporter, destination=destination, resource=resource):
                        successors.append((tmp_world, tmp_world.get_big_u()))

    return successors


def main(argv):
    weights = initial_state.create_resource_dict()
    print(weights)

    countries = initial_state.create_country_dict()
    print(countries)

    d_bound = 3     # to-do: make global class var

    new_world = World(d_bound, weights, countries)
    # print(new_world.weights)
    # print(new_world.num_country)
    # print(new_world.d_bound)
    country1 = new_world.countries['Atlantis']
    # print(country1.resources)
    print(country1.weights)

    print(new_world.little_u_array())
    lu = new_world.little_u_array()
    print(gini_index(lu))
    print(gini_1(lu))

    successors = generate_successor(new_world)
    print len(successors)


if __name__ == "__main__":
    main(sys.argv)
