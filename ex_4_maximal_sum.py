import sys


def possible_parent_with_3_child(mat, ro, co):
    possible_coordinates = [
        [ro, co],
        [ro, co + 1],
        [ro, co + 2],
        [ro + 1, co],
        [ro + 1, co + 1],
        [ro + 1, co + 2],
        [ro + 2, co],
        [ro + 2, co + 1],
        [ro + 2, co + 2],
    ]
    result = []
    for i in range(len(possible_coordinates)):
        if 0 <= ro < len(mat) and 0 <= co < len(mat[0]):
            result.append(possible_coordinates[i])
    return result


rows, cols = [int(x) for x in input().split(' ')]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

max_row = None
max_col = None
sum_max_matrix = - sys.maxsize
for i in range(len(matrix) - 3 + 1):
    for j in range(len(matrix[0]) - 3 + 1):
        current_sum = 0
        for row, col in possible_parent_with_3_child(matrix, i, j):
            current_sum += matrix[row][col]
        if current_sum > sum_max_matrix:
            sum_max_matrix = current_sum
            max_row = i
            max_col = j

l_max = []
for row, col in possible_parent_with_3_child(matrix, max_row, max_col):
    l_max.append(matrix[row][col])
print(f'Sum = {sum_max_matrix}')
print(*l_max[:3])
print(*l_max[3:6])
print(*l_max[6:9])
