s = input()
triplets = []
proteins = []
for i in range(3, len(s) + 1, 3):
    triplets.append(s[i - 3:i])
for triplet in triplets:
    if triplet[0] == 'U':
        if triplet[1] == 'C':
            proteins.append('S')
        elif triplet[1] == 'U':
            if triplet[2] in ['C', 'U']:
                proteins.append('F')
            else:
                proteins.append('L')
        elif triplet[1] == 'A':
            if triplet[2] in ['C', 'U']:
                proteins.append('Y')
            else:
                proteins.append('_')
        elif triplet[2] in ['C', 'U']:
            proteins.append('C')
        elif triplet[2] == 'A':
            proteins.append('_')
        else:
            proteins.append('W')
    elif triplet[0] == 'C':
        if triplet[1] == 'C':
            proteins.append('P')
        elif triplet[1] == 'G':
            proteins.append('R')
        elif triplet[1] == 'U':
            proteins.append('L')
        elif triplet[2] in ['U', 'C']:
            proteins.append('H')
        else:
            proteins.append('Q')
    elif triplet[0] == 'A':
        if triplet[1] == 'C':
            proteins.append('T')
        elif triplet[1] == 'U':
            if triplet[2] == 'G':
                proteins.append('M')
            else:
                proteins.append('I')
        elif triplet[1] == 'G':
            if triplet[2] in ['C', 'U']:
                proteins.append('S')
            else:
                proteins.append('R')
        elif triplet[2] in ['C', 'U']:
            proteins.append('N')
        else:
            proteins.append('K')
    elif triplet[1] == 'U':
        proteins.append('V')
    elif triplet[1] == 'C':
        proteins.append('A')
    elif triplet[1] == 'G':
        proteins.append('G')
    elif triplet[2] in ['A', 'G']:
        proteins.append('E')
    else:
        proteins.append('D')
print(''.join(proteins)[:''.join(proteins).find('_')])