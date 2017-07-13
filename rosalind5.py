names = []
codes = []
procents = []
with open('/home/xenx/Downloads/rosalind_gc (3).txt') as f:
    for line in f:
        names.append('')
        codes.append('')
        procents.append(0)
with open('/home/xenx/Downloads/rosalind_gc (3).txt') as f:
    i = 0
    first = True
    for line in f:
#        print(line)
        if line[0] == '>':
            if not first:
                procents[i] = (codes[i].count('G') + codes[i].count('C')) / len(codes[i]) * 100
                i += 1
            else:
                first = False
            names[i] = line.strip()[1:]
            continue
#        print('1')
        codes[i] += line.strip()

print(names[procents.index(max(procents))], round(max(procents), 5), sep='\n')