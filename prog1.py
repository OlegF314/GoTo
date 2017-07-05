def score(x, y):
    if x == y:
        return 1
    return -1


def check(table):
    for m in table:
        print(' '.join(map(str, m)))


def align(s, t):
    prevs = [[-2] + [0] * len(s) for i in range(len(t) + 1)]
    prevs[0] = [-2] * (len(s) + 1)
    matrix = [[0] + [None] * len(s) for i in range(len(t) + 1)]
    matrix[0] = [0] * (len(s) + 1)
    maxi = -1
    maxj = -1
    maxim = -1
    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            matrix[i][j] = max(
                0,
                score(s[j - 1], t[i - 1]) + matrix[i - 1][j - 1],
                score('-', s[j - 1]) + matrix[i][j - 1],
                score(t[i - 1], '-') + matrix[i - 1][j])
            if matrix[i][j] >= maxim:
                maxim = matrix[i][j]
                maxi = i
                maxj = j

            if score(s[j - 1], t[i - 1]) + matrix[i - 1][j -
                                                         1] == matrix[i][j]:
                prevs[i][j] = 0
            elif score('-', s[j - 1]) + matrix[i][j - 1] == matrix[i][j]:
                prevs[i][j] = -1
            else:
                prevs[i][j] = 1

            if not matrix[i][j]:
                #                i = 0
                #                j = 0
                prevs[i][j] = -2

    i = maxi
    k = maxj
    align_a = ''
    align_b = ''
    while (i > 0 or k > 0) and prevs[i][k] != -2:
        print(i, k)
        if i > 0 and k > 0 and prevs[i][k] == 0:
            align_a = t[i - 1] + align_a
            align_b = s[k - 1] + align_b
            i -= 1
            k -= 1
        elif i > 0 and prevs[i][k] == 1:
            align_a = t[i - 1] + align_a
            align_b = '-' + align_b
            i -= 1
        elif k > 0 and prevs[i][k] == -1:
            align_a = '-' + align_a
            align_b = s[k - 1] + align_b
            k -= 1

    print(align_a)
    print(align_b)


align('GCCCCCCCCAAAACCTT', 'AGCAAAACCTTTTTTTTTT')
