def is_permutation(vector):
    for i in range(len(vector)):
        if i not in vector:
            return False
    return True


def read_dataset():
    with open('dataset.txt', 'r') as f:
        lines = f.readlines()
    number_of_points = int(lines[0][:-1])
    points = []
    for i in range(number_of_points):
        line = lines[i + 1]
        point = [int(line[:line.find(' ')]), int(line[line.find(' ') + 1:-1])]
        points.append(point)
    min_len_path = float(lines[number_of_points + 1][:-1])
    max_len_path = float(lines[number_of_points + 2][:-1])
    return number_of_points, points, min_len_path, max_len_path


def count_unique_genes(vector):
    result = 0
    for i in range(len(vector)):
        if i in vector:
            result += 1
    return result


def length_of_path(permutation, points):
    result = 0
    for i in range(len(permutation)):
        index = permutation[i]
        index_prev = permutation[i - 1]
        result += ((points[index][0] - points[index_prev][0]) ** 2 +
                   (points[index][1] - points[index_prev][1]) ** 2) ** 0.5
    return result


def evaluation_function(vector, points, min_l, max_l):
    if is_permutation(vector):
        len_of_path = length_of_path(vector, points)
        return ((len_of_path - max_l) / (min_l - max_l)) ** 2
    else:
        return (count_unique_genes(vector) - 1) / (len(vector) - 1) - 1


number_of_points, points, min_len_of_path, max_len_of_path = read_dataset()


def fitness(weights):
    return evaluation_function(weights, points, min_len_of_path, max_len_of_path)