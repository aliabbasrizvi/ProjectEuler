"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by only moving to the right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right
by only moving right and down.
"""

TOTAL_ROWS = 80
TOTAL_COLUMNS = 80

def generate_matrix(file_contents):
  row = 0
  matrix = [[0 for x in xrange(TOTAL_COLUMNS)] for y in xrange(TOTAL_ROWS)]
  for line in file_contents:
    values = line.strip().split(',')
    for idx in xrange(len(values)):
      matrix[row][idx] = int(values[idx])
    row += 1
  return matrix

def get_min_sum(matrix, x, y):
  if x == TOTAL_ROWS or y == TOTAL_COLUMNS:
    return 0

  current_number = matrix[x][y]
  return min(current_number + get_min_sum(matrix, x, y + 1), current_number + get_min_sum(matrix, x + 1, y))


def get_sum(file_name):
  with open(file_name) as file_contents:
    matrix = generate_matrix(file_contents)

  return get_min_sum(matrix, 0, 0)

if __name__ == '__main__':
  print get_sum('p081_matrix.txt')