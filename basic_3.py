from time import time
import sys
import psutil

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


def calculate_opt(x, y):
    m = len(x) + 1
    n = len(y) + 1

    opt = [[0] * n for i in range(m)]  # initalize opt(m,n) matrix

    for i in range(m):
        for j in range(n):
            if j == 0:
                opt[i][0] = i * delta  # initailze first row to k*delta
            if i == 0:
                opt[0][j] = j * delta  # initailze first column to k*delta

    for i in range(1, m):
        for j in range(1, n):
            mismatch = opt[i - 1][j - 1] + alpha(x[i - 1], y[j - 1])  # (Xm,Yn) match-mismatch cost
            y_gap = opt[i][j - 1] + delta  # _Xm is not matched
            x_gap = opt[i - 1][j] + delta  # _Yn is not matched
            opt[i][j] = min(mismatch, y_gap, x_gap)

    return opt


def top_down(opt, s1, s2):
    output1, output2 = "", ""
    m, n = len(s1), len(s2)
    i, j = m, n

    while i > 0 or j > 0:
        if i > 0 and j > 0 and opt[i][j] == opt[i - 1][j - 1] + alpha(s1[i - 1], s2[j - 1]):
            output1 = output1 + s1[i - 1]
            output2 = output2 + s2[j - 1]
            i = i - 1
            j = j - 1

        else:
            if i > 0 and opt[i][j] == opt[i - 1][j] + delta:
                output1 = output1 + s1[i - 1]
                output2 = output2 + "_"
                i = i - 1

            elif j > 0 and opt[i][j] == opt[i][j - 1] + delta:
                output1 = output1 + "_"
                output2 = output2 + s2[j - 1]
                j = j - 1

    output1 = output1[::-1]
    output2 = output2[::-1]
    return opt[m][n], output1, output2, m + n


def basic(string1, string2):
    dp = calculate_opt(string1, string2)
    return top_down(dp, string1, string2)


if __name__ == "__main__":
    delta = 30
    s1, s2, s1_pos, s2_pos = read_ip(sys.argv[1])
    final_string1 = create_str(s1, s1_pos)
    final_string2 = create_str(s2, s2_pos)

    start = time()
    cost, s_1, s_2, problem_size = basic(final_string1, final_string2)
    end = time()
    # print(problem_size)
    time = (end - start) * 1000
    memory = memory()

    with open(sys.argv[2], "w") as f:
        string = "{}\n{}\n{}\n{}\n{}".format(cost, s_1, s_2, time, memory)
        f.writelines(string)
