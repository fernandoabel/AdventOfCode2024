import re

memory = open('Input/Day3.txt', 'r').read()
print(memory)
i = 0 # Position

def readChar():
    global memory, i
    char = memory[i]
    i+=1
    return char

def findMultiplications():
    global memory, i
    multiplications = []

    current = str()
    state = "BEGIN"
    DO_DONT = True

    while True:
        match state:
            case "BEGIN":
                c = readChar()

                while c.isspace():
                    c = readChar()

                if c.isalpha():      state = "ALPHA"
                elif i >= len(memory): state = "END"

            case "END":
                break

            case "ALPHA":
                while c.isalpha() or c == "'":
                    current += c
                    c = readChar()

                if c == "(":
                    if current == "mul":
                        state =  "("
                    elif (current == "do" or current == "don't"):
                        state = "EMPTY_FUNCTION"
                    else:
                        state = "BEGIN"
                        current = str()
                else:
                    state = "BEGIN"
                    current = str()

            case "EMPTY_FUNCTION":
                current += c
                c = readChar()
                current += c
                if current == 'do()':
                    DO_DONT = True
                    state = "BEGIN"
                    current = str()
                elif current == "don't()":
                    DO_DONT = False
                    state = "BEGIN"
                    current = str()
                else:
                    state = "BEGIN"
                    current = str()

            case "NUMERIC":
                while c.isnumeric():
                    current += c
                    c = readChar()

                if c == ',': state = ","
                elif c == ')': state = ")"
                else:
                    state = "BEGIN"
                    current = str()

            case "(":
                current += c

                c = readChar()
                if c.isnumeric(): state = "NUMERIC"
                else:
                    state = "BEGIN"
                    current = str()

            case ")":
                current += c

                if DO_DONT:
                    print("Do Word", current)
                    multiplications.append(current)
                    current = str()
                else:
                    print("Don't do Word", current)
                    current = str()
                state = "BEGIN"

            case ",":
                current += c
                c = readChar()
                if c.isnumeric():
                    state = "NUMERIC"
                else:
                    state = "BEGIN"
                    current = str()
    return multiplications

def findRegexMul():
    return re.findall(r"mul\(\d+,\d+\)", memory);

def part1():
    sum = 0
    multiplications = findRegexMul()
    for mul in multiplications:
        x, y = re.search(r"\d+,\d+", mul).group().split(',')
        sum = sum + (int(x)*int(y))
    print(sum)

def part2():
    sum = 0
    multiplications = findMultiplications()
    for mul in multiplications:
        x, y = re.search(r"\d+,\d+", mul).group().split(',')
        sum = sum + (int(x) * int(y))
    print(sum)


if __name__ == "__main__":
    part1()
    part2()
