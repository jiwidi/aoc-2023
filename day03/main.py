import re

def read_input():
    content = open('input.txt', 'r').readlines()
    return content


def puzzle_one(content):
    found_numbers = []
    for i,line in enumerate(content):
        for match in re.finditer(r'\d+', line):
            number = match.group()
            if number[0] != '0':
                found_numbers.append([i, match.start(), len(number), int(number)])


    def check_range(x, y):
        if (x<0 or y<0 or x>=len(content) or y>=len(content[x])):
            return False
        if(re.match(r'[^0-9.]', content[x][y])):
            return True
        return False

    sol = 0
    for number in found_numbers:
        print(number)
        line = number[0]
        index = number[1]
        length = number[2]
        possible_ranges = [
            (line-1, index+i) for i in range(-1, length+1)
        ] + [
            (line, -1), (line, length)
        ] + [
            (line+1, index+i) for i in range(-1, length+1)
        ]
        valid = False
        for possible_range in possible_ranges:
            valid = valid or check_range(*possible_range)
        print(valid)
        if valid:
            sol += number[3]
    return sol

def main():
    content = read_input()
    print("Solution for puzzle one", puzzle_one(content))
    # print("Solution for puzzle two", puzzle_two(content))


if __name__ == '__main__':
    main()