left = list()
right = list()
lines = open('Input/Day1.txt', 'r').readlines()
for line in lines:
    split = line.split('   ')
    left.append(int(split[0]))
    right.append(int(split[1]))

def part1():
    left.sort()
    right.sort()
    diff = []
    for i in (range(len(left))):
        diff.append(abs(left[i] - right[i]))
    print(sum(diff))

def part2():
    for i in (range(len(left))):
        left[i] = left[i] * right.count(left[i])
    print(sum(left))


if __name__ == "__main__":
    part1()

    part2()