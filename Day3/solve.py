import re
from collections import defaultdict

with open("Day3\input.txt", "r") as input_file:
    input_lines = input_file.readlines()


def part01():
    onLocationClaim = defaultdict(lambda: 0)
    TWO_OR_MORE_CLAIM = 0

    for line in input_lines:
        # the input has a form of #x @ x,x: x*x format
        # where each of the x signifies important information about the claim for
        # fabric cutting of each elf.
        # re.sub() matches each of the extra characters and replaces them with a white space
        # the returned string is stripped from its whitespace and then split accordingly
        # returing only the numbers we wanted :)
        stripped_line = re.sub(r'[#@,:x]', ' ', line).strip(" ").split()
        claim_id, x, y, width, height = [int(n) for n in stripped_line]

        # loop over each width and height to find replicating claims
        # increment if repeated
        for i in range(width):
            for j in range(height):
                point = (x+i, y+j)
                onLocationClaim[point] += 1
                if onLocationClaim[point] == 2:
                    TWO_OR_MORE_CLAIM += 1

    print(TWO_OR_MORE_CLAIM)


def part02():
    locationClaimers = defaultdict(set)
    uniqueLocationClaimers = []

    # fill the dict with necessarry data about point claimers and their claim id
    # as a dictionary
    for line in input_lines:
        stripped_line = re.sub(r'[#@,:x]', ' ', line).strip(" ").split()
        claim_id, x, y, width, height = [int(n) for n in stripped_line]

        for i in range(width):
            for j in range(height):
                point = (x+i, y+j)
                locationClaimers[point].add(claim_id)

    # find how many unique points are under each claim id
    # if it is exactly their length * weight then we are done

    # stores the ids of locationclaimers with size exactly 1
    one_locationers = [locationClaimers[i]
                       for i in locationClaimers.keys() if len(locationClaimers[i]) == 1]

    # for each claim id we try to match their area with the point counts each of them
    # claimed, say 3 has claimed 4 points and its size is 4 means it haven't shared any points
    # with any other id
    for line in input_lines:
        stripped_line = re.sub(r'[#@,:x]', ' ', line).strip(" ").split()
        claim_id, x, y, width, height = [int(n) for n in stripped_line]

        size = width * height
        if (one_locationers.count({claim_id}) == size):
            uniqueLocationClaimers.append(claim_id)

    print(uniqueLocationClaimers)
