from math import log2
import sys
import  matplotlib.pyplot as plt
with open('/home/xenx/Downloads/norm_camp.tsv') as f:
    first = True
    names = []
    expression = []
    all_middle = []
    for line in f:
        if first:
            types = line.strip().split()[1:]
            border = types.index('case')
            lencase = len(types) - border
            first = False
            continue
        current_line = line.strip().split()
        names.append(current_line[0])
        expression_control = sum(map(float, current_line[1:border])) / (border - 1)
        expression_case = sum(map(float, current_line[border:])) / lencase
        expression.append(log2(expression_case / expression_control))
        all_middle.append(sum(map(float, current_line[1:])) / len(types))

with open('Big_dif_genes.txt', 'w') as f:
    for i in range(len(expression)):
        if abs(expression[i]) > 0.1:
            plt.plot([all_middle[i]], [expression[i]], 'ro')
            f.write(names[i])
            f.write('\n')
plt.show()