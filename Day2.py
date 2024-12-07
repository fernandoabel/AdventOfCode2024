reports = open('Input/Day2.txt', 'r').readlines()

def check_report(levels):
    levels_safe = list()
    safe = [True]

    increasing = None
    for i in range(len(levels) - 1):
        safe = True
        if (levels[i] > levels[i + 1] and increasing == False) or (levels[i] < levels[i + 1] and increasing == True):
            safe = False
        if abs(levels[i] - levels[i + 1]) > 3 or abs(levels[i] - levels[i + 1]) < 1:
            safe = False

        increasing = levels[i] > levels[i + 1]
        levels_safe.append(safe)

    return levels_safe

def part1():
    safe_count = 0

    for report in reports:
        levels = [int(item) for item in report.split(' ')]
        levels_safe = check_report(levels)
        if levels_safe.count(False) == 0:
            safe_count += 1
    print("Part1", safe_count)

def part2():
    safe_count = 0

    for report in reports:
        levels = [int(item) for item in report.split(' ')]
        levels_safe = check_report(levels)
        print(levels, levels_safe)
        if levels_safe.count(False) == 0:
            safe_count += 1
            print("\tFirst scenario", safe_count,"/", len(reports))
        else:
            # print(levels, levels_safe)
            #print('\t######################################')
            safe = False
            for index in range(len(levels)):
                levels2 = levels[:index] + levels[index+1 :]
                levels2_safe = check_report(levels2)

                if levels2_safe.count(False) == 0:
                    print("\t\t", index, levels2, levels2_safe)
                    safe = True
                    break

            if safe:
                safe_count += 1
            else:
                print("\t\t", levels, levels_safe)


            #print('\t######################################')

    print("Part2", safe_count)


if __name__ == "__main__":
    #part1()

    part2()