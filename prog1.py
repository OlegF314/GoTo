def score(x, y):
    if x == y:
        return 1
    return  -1

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
            matrix[i][j] = max(0, score(s[j - 1], t[i - 1]) + matrix[i - 1][j - 1], score('-', s[j - 1]) + matrix[i][j - 1], score(t[i - 1], '-') + matrix[i - 1][j])
            if matrix[i][j] >= maxim:
                maxim = matrix[i][j]
                maxi = i
                maxj = j
            if not matrix[i][j]:
#                i = 0
#                j = 0
                prevs[i][j] = -2
            if score(s[j - 1], t[i - 1]) + matrix[i - 1][j - 1] == matrix[i][j]:
                prevs[i][j] = 0
            elif score('-', s[j - 1]) + matrix[i][j - 1] == matrix[i][j]:
                prevs[i][j] = -1
            else:
                prevs[i][j] = 1
    way = [[maxi, maxj]]
    i = maxi
    j = maxj
    endi = 0
    endj = 0
    while [i, j] != [0, 0]:
        check(prevs)
        check(way)
        print(i, j, prevs)
        if matrix[i][j] == 0:
            way.append([i, j])
            endi = i
            endj = j
            i = 0
            j = 0
        if prevs[i][j] or i * j == 0:
            if prevs[i][j] - 1 and j != 0:
                way.append([i, j - 1])
                j -= 1
            elif i != 0:
                way.append([i - 1, j])
                i -= 1
        else:
            way.append([i - 1, j - 1])
            i -= 1
            j -= 1
    print(list(range(-1, len(s) + 1)))
    for i in range(len(t) + 1):
        print([i] + matrix[i])
    check(way)
#    for i in range(1, len(way) - 1):
#        if way[i][0] == way[i + 1][0]:
#            t = t[:way[i][0]] + '-' + t[way[i][0]:]
#        elif way[i][1] == way[i + 1][1]:
#            s = s[:way[i][1]] + '-' + s[way[i][1]:]
#    if len(s) > len(t):
#        t += '-' * (len(s) - len(t))
#    elif len(t) > len(s):
#        s += '-' * (len(t) - len(s))
    print(s[endj:maxj - 1])
    print(t[endi:maxi - 1])

#with open('/home/xenx/Downloads/small.fastq') as f:
#    first = True
#    ref = ''
#    ref_name = ''
#    for line in f:
#        if first:
#            ref_name = line.strip()
#            first = False
#            continue
#        ref += line.strip()
#        print(line)
align('TTTAAACTTT', 'AGCAAAACCTTTTTTTTTT')
