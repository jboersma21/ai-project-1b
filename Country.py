"""
Project Part 1b

Team 6

Colin Moody, Ohad Beck, Charlie MacVicar, Jake Boersma

"""

import sys


class Country:

    def __init__(self, name, resource_dict, weight_dict):
        self.name = name                    # country name
        self.resources = resource_dict      # dictionary containing amount of resources the country possesses
        self.weights = weight_dict          # dictionary containing resources and corresponding weights

    def little_u(self):
        housing_val = self.weights['R23']*((1 - self.resources['R1']) / (2 * (self.resources['R23'] + 5)))
        alloy_val = self.weights['R21']*self.resources['R21']
        electronics_val = self.weights['R22']*self.resources['R22']
        waste_val = (-self.weights["R21'"]*self.resources["R21'"]) - (self.weights["R22'"]*self.resources["R22'"]) - (-self.weights["R23'"]*self.resources["R23'"])
        little_util = housing_val + alloy_val + electronics_val + waste_val
        return little_util

def main(argv):
    print("")


if __name__ == "__main__":
    main(sys.argv)