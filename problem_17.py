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
        elif i < 30:
            return number_to_alphabet_count[20] + number_to_alphabet_count[i - 20]
        elif i < 40:
            return number_to_alphabet_count[30] + number_to_alphabet_count[i - 30]
        elif i < 50:
            return number_to_alphabet_count[40] + number_to_alphabet_count[i - 40]
        elif i < 60:
            return number_to_alphabet_count[50] + number_to_alphabet_count[i - 50]
        elif i < 70:
            return number_to_alphabet_count[60] + number_to_alphabet_count[i - 60]
        elif i < 80:
            return number_to_alphabet_count[70] + number_to_alphabet_count[i - 70]
        elif i < 90:
            return number_to_alphabet_count[80] + number_to_alphabet_count[i - 80]
        elif i < 100:
            return number_to_alphabet_count[90] + number_to_alphabet_count[i - 90]

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
