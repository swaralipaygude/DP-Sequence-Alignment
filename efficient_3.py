from time import time
import sys
import psutil
from basic_3 import basic

delta = 30

def memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss / 1024)
    return memory_consumed


def read_ip(filename):
    input_file = open(filename, 'r')
    input_list = [line.rstrip() for line in input_file.readlines()]

    string1 = input_list[0]
    pos_str1, pos_str2 = [], []
    index = 0

    for i in range(1, len(input_list)):
        if input_list[i].isnumeric():
            pos_str1.append(int(input_list[i]))
        else:
            index = i
            string2 = input_list[index]
            break

    for i in range(index + 1, len(input_list)):
        if input_list[i].isnumeric():
            pos_str2.append(int(input_list[i]))

    return string1, string2, pos_str1, pos_str2


def create_str(string, pos_str):
    previous_string = string
    for i in pos_str:
        current_string = previous_string
        current_string = current_string[:i + 1] + previous_string + current_string[i + 1:]
        previous_string = current_string
    return previous_string


def alpha(x, y):
    alpha_matrix = [[0, 110, 48, 94],
                    [110, 0, 118, 48],
                    [48, 118, 0, 110],
                    [94, 48, 110, 0]]
    bases = ['A', 'C', 'G', 'T']
    i = bases.index(x)
    j = bases.index(y)
    return alpha_matrix[i][j]


def efficient(X, Y):
    total_cost = 0
    output1, output2 = "", ""

    if len(X) == 0:
        for i in range(len(Y)):
            total_cost = total_cost + delta
            output1 = output1 + '_'
            output2 = output2 + Y[i]

    elif len(Y) == 0:
        for i in range(len(X)):
            total_cost = total_cost + delta
            output1 = output1 + X[i]
            output2 = output2 + '_'

    elif len(X) == 1 or len(Y) == 1:
        cost, n1, n2, _ = basic(X, Y)
        total_cost = total_cost + cost
        output1 = output1 + n1
        output2 = output2 + n2

    else:
        # Divide
        xmid = int(len(X) / 2)

        left_score = scores(X[:xmid], Y, len(X[:xmid]) + 1, len(Y) + 1)
        right_score = scores(X[xmid:][::-1], Y[::-1], len(X[xmid:]) + 1, len(Y) + 1)

        # get the min index value to split string Y
        right_score.reverse()
        get_mid = []
        for left, right in zip(left_score, right_score):
            get_mid.append(left + right)
        ymid, _ = min(enumerate(get_mid), key=lambda a: a[1])

        # Conquer
        cost_left = efficient(X[:xmid], Y[:ymid])
        cost_right = efficient(X[xmid:], Y[ymid:])

        # Combine
        total_cost = cost_left[0] + cost_right[0]
        output1 = cost_left[1] + cost_right[1]
        output2 = cost_left[2] + cost_right[2]

    return total_cost, output1, output2


def scores(sequence_a, sequence_b, lena, lenb):
    score = [0 for i in range(lenb)]
    previous_score = [0 for i in range(lenb)]

    for j in range(1, lenb):
        previous_score[j] = previous_score[j - 1] + delta

    for i in range(1, lena):
        score[0] = previous_score[0] + delta
        for j in range(1, lenb):
            mismatch = previous_score[j - 1] + alpha(sequence_a[i - 1], sequence_b[j - 1])
            y_gap = score[j - 1] + delta
            x_gap = previous_score[j] + delta
            score[j] = min(mismatch, y_gap, x_gap)
        previous_score[:] = score[:]

        Lastline = [0 for i in range(lenb)]
        Lastline[:] = previous_score[:]
    return Lastline


if __name__ == "__main__":
    delta = 30
    s1, s2, s1_pos, s2_pos = read_ip(sys.argv[1])
    final_string1 = create_str(s1, s1_pos)
    final_string2 = create_str(s2, s2_pos)

    start = time()
    cost, s_1, s_2 = efficient(final_string1, final_string2)
    end = time()
    time = (end - start) * 1000
    memory = memory()

    with open(sys.argv[2], "w") as f:
        string = "{}\n{}\n{}\n{}\n{}".format(cost, s_1, s_2, time, memory)
        f.writelines(string)
