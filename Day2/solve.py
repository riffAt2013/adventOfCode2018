from collections import defaultdict

inputFile = open(
    r'C:\Users\RIFAT\Documents\adventOfCode2018\Day2\input.txt', "r")
lines = inputFile.readlines()


def part01():
    TWO_TIME_LETTERS = 0
    THREE_TIME_LETTERS = 0

    for line in lines:
        char_count = defaultdict(lambda: 0)

        # for aabbcc itll be 'a':2, 'b':2 and such
        for char in line:
            char_count[char] += 1

        # if in one line, two or more char is exactly twice or THRICE, DONT REPEAT!
        setOfFrequency = set(char_count.values())
        if 2 in setOfFrequency:
            TWO_TIME_LETTERS += 1
        if 3 in setOfFrequency:
            THREE_TIME_LETTERS += 1

    print("Checksum: ", THREE_TIME_LETTERS * TWO_TIME_LETTERS)

# readymade function of hamming distance :P, courtesy to internet
def hamming_distance(string1, string2):
    distance = 0

    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1

    return distance


def part02():
    # we need to work with hamming distance here
    hamming_dict = {}
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            line1 = lines[i].strip()
            line2 = lines[j].strip()

            hamming_dict[hamming_distance(line1, line2)] = line1+"|"+line2

    MIN_HKEY = min(hamming_dict.keys())
    MIN_HKEY_VALUE = hamming_dict[min(hamming_dict.keys())]
    print(f"min hamming key: {MIN_HKEY}, min hamming key value {MIN_HKEY_VALUE}")

    string1, string2 = MIN_HKEY_VALUE.split('|')
    output = ""
    for i in range(len(string1)):
        if string1[i] == string2[i]: output += string1[i]

    print(output)


    

