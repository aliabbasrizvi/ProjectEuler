""" Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator
would confirm that 211 = 2048 < 37 = 2187. However, confirming that 632382518061 > 519432525806 would
be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines
with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
import math

def get_largest_number(file_name):
    current_index = 0
    largest_index = 0
    largest_value = 0
    with open(file_name) as file_contents:
        for line in file_contents:
            current_index += 1
            number, power = line.strip().split(',')
            current_value = float(power) * math.log10(float(number))
            if current_value > largest_value:
                largest_index = current_index
                largest_value = current_value

    return largest_index

if __name__ == '__main__':
    print get_largest_number('p099_base_exp.txt')
