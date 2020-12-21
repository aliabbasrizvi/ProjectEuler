""" If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the numbers from 1 to
1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
"and" when writing out numbers is in compliance with British usage.
"""

number_to_alphabet_count = {
  1: len('one'),
  2: len('two'),
  3: len('three'),
  4: len('four'),
  5: len('five'),
  6: len('six'),
  7: len('seven'),
  8: len('eight'),
  9: len('nine'),
  10: len('ten'),
  11: len('eleven'),
  12: len('twelve'),
  13: len('thirteen'),
  14: len('fourteen'),
  15: len('fifteen'),
  16: len('sixteen'),
  17: len('seventeen'),
  18: len('eighteen'),
  19: len('nineteen'),
  20: len('twenty'),
  30: len('thirty'),
  40: len('forty'),
  50: len('fifty'),
  60: len('sixty'),
  70: len('seventy'),
  80: len('eigthy'),
  90: len('ninety'),
  100: len('hundred'),
  1000: len('thousand')
}

def get_alphabet_count__upto_100(i):
        if i <= 20 or i % 10 == 0:
            return number_to_alphabet_count[i]
        else:
            return number_to_alphabet_count[(i / 10) * 10] + number_to_alphabet_count[i - (i / 10) * 10]

def get_total_alphabet_count(range_end):
    result = 0
    for i in xrange(1, range_end + 1):
        if i < 100:
            result += get_alphabet_count__upto_100(i)
        elif i % 100 == 0 and i != 1000:
            result += number_to_alphabet_count[i / 100] + number_to_alphabet_count[100]
        elif i < 1000:
            result += number_to_alphabet_count[i / 100] + number_to_alphabet_count[100] + \
                      len('and') + get_alphabet_count__upto_100(i - (i / 100) * 100)
        elif i == 1000:
            result +=  number_to_alphabet_count[i / 1000] + number_to_alphabet_count[i]

    return result

if __name__ == '__main__':
    print get_total_alphabet_count(1000)
