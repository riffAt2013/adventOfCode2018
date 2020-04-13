inputFile = open('Day1\input.txt', "r")
lines = inputFile.readlines()

def partOne():
    result = 0
    for line in lines:
        result += int(line)

    print(result)


def partTwo():
    distinct_sum = set()
    sum = 0


    # hacky way to repeat the loop over
    # notice w/o the while the loop will end at the last value from
    # the input.txt, however our problem description tells us to loop
    # over as many times as possible.

    # there might have been more overkill ways to repeat a loop over
    # but this is the best way :)
    while sum not in distinct_sum:
        for line in lines:
            distinct_sum.add(sum)
            sum += int(line)
            print(sum)

            if sum in distinct_sum:
                print(f"Final result would be {sum}")
    
    
    
    
    
