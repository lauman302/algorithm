def is_subsequence(line_1, line_2):
    len_1, len_2 = len(line_1), len(line_2)
    if len_1 == 0:
        return True

    if len_1 > len_2:
        return False

    i = 0
    for j in range(len_2):
        if line_1[i] == line_2[j]:
            i += 1
            if i == len_1:
                return True

    return False


if __name__ == '__main__':
    line_1 = input()
    line_2 = input()
    print(is_subsequence(line_1, line_2), end='')