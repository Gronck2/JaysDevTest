def minimal_distance(word1: str, word2: str):
    m = len(word1)
    n = len(word2)
    prev_row = list(range(n + 1))  # initialize according condition that word1 is ""
    cur_row = [0] * (n + 1)  # initialize with zeroes

    for i in range(1, m + 1):
        cur_row[0] = i
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                cur_row[j] = prev_row[j - 1]  # no new operation copy from previous list
            else: # if letters don't match check what kind of operation is less expansive
                cur_row[j] = min(prev_row[j - 1], prev_row[j], cur_row[j - 1]) + 1
                # operation: change, delete, insert

        prev_row = cur_row
        cur_row = [0] * (n + 1)

    return prev_row[-1]


if __name__ == '__main__':
    import sys
    minimal_distance(sys.argv[0], sys.argv[1])