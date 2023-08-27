from typing import List


def insert_into_array(arr: List[str], index: int, new_item: str):
    return arr[:index] + [new_item] + arr[index:]


def create_matrix(n: int, m: int) -> List[List[int]]:
    return [[0 for _ in range(n+1)] for _ in range(m+1)]


def minimal_distance(word1: str, word2: str):
    n = len(word1)
    m = len(word2)
    dp = create_matrix(n, m)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 0:
                dp[i][j] = j  # Initialize the first row
            elif j == 0:
                dp[i][j] = i  # Initialize the first column
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1,
                    dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1)
                )

    distance = dp[n-1][m-1]
    print(distance)
    cur_i = n-1
    cur_j = m-1
    cur_word = list(word2)

    print(''.join(cur_word))
    while distance > 0:
        deletion = dp[cur_i][cur_j-1]
        insertion = dp[cur_i-1][cur_j]
        substitution = dp[cur_i-1][cur_j-1]
        if substitution < distance:
            cur_word[cur_j] = word1[cur_i]
            cur_i -= 1
            cur_j -= 1
            distance = substitution
            print(''.join(cur_word))
        elif deletion < distance:
            cur_word[cur_j] = ''
            cur_j -= 1
            distance = deletion
            print(''.join(cur_word))
        elif insertion < distance:
            cur_word = insert_into_array(cur_word, cur_j+1, word1[cur_i])
            cur_i -= 1
            distance = insertion
            print(''.join(cur_word))
        else:
            cur_i -= 1
            cur_j -= 1


if __name__ == '__main__':
    import sys
    minimal_distance(sys.argv[1], sys.argv[2])