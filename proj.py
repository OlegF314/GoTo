import sys
import math
def viterbi(S, O, pi, T, E, y):
    t = len(y)
    dynamic_array = [[None for i in range(t)] for j in range(len(S))]
    for i in range(len(S)):
        dynamic_array[i][0] = pi[S[i]] + E[S[i]][y[i]]
    way = [None for i in range(t)]
    for i in range(1, t):
        if not i % 1000:
            print(str(i) + '/' + str(t))
        for j in range(len(S)):
            max_max = MINUS_INFINITY
            for k in range(len(S)):
                current_max = dynamic_array[k][i - 1] + T[S[k]][S[j]] + E[S[j]][y[i]]
                if current_max > max_max:
                    dynamic_array[j][i] = current_max
                    if S[k] in ['T_plus', 'A_plus', 'G_plus', 'C_plus']:
                        way[i - 1] = '+'
                    else:
                        way[i - 1] = '-'
                    max_max = current_max
    max_max = MINUS_INFINITY
    for i in range(len(S)):
        current_max = dynamic_array[i][t - 1]
        if current_max > max_max:
            max_max = current_max
            if S[i] in ['T_plus', 'A_plus', 'G_plus', 'C_plus']:
                way[i - 1] = '+'
            else:
                way[i - 1] = '-'

    return way


def readf(file):
    genome = ''
    with open(file) as f:
        for line in f:
            if line[0] == '>':
                continue
            genome += line.strip()
    print(genome[:60])
    return genome


AM = 'A_minus'
GM = 'G_minus'
CM = 'C_minus'
TM = 'T_minus'
AP = 'A_plus'
GP = 'G_plus'
CP = 'C_plus'
TP = 'T_plus'
OKTER = 0.125
with open('/home/xenx/xo/out.txt', 'w') as f:
    MINUS_INFINITY = -999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    pi = {AP: 0.005, GP: 0.005, CP: 0.005, TP: 0.005, AM: 0.245, GM: 0.245, CM: 0.245, TM: 0.245}
    S = [AM, GM, CM, TM, AP, GP, CP, TP]
    O = ['A', 'C', 'G', 'T']
    T = {AM: {AM: 7/32, GM: 7/32, CM: 7/32, TM: 7/32, AP: 0, GP: 1/16, CP: 1/16, TP: 0},
         GM: {AM: 7/32, GM: 7/32, CM: 7/32, TM: 7/32, AP: 0, GP: 1/16, CP: 1/16, TP: 0},
         CM: {AM: 7/32, GM: 7/32, CM: 7/32, TM: 7/32, AP: 0, GP: 1/16, CP: 1/16, TP: 0},
         TM: {AM: 7/32, GM: 7/32, CM: 7/32, TM: 7/32, AP: 0, GP: 1/16, CP: 1/16, TP: 0},
         AP: {AM: 1/16, GM: 1/16, CM: 1/16, TM: 1/16, AP: 1/36, GP: 1/3, CP: 1/3, TP: 1/36},
         GP: {AM: 0.014, GM: 0.014, CM: 0.014, TM: 0.014, AP: 0.002, GP: 0.08, CP: 0.86, TP: 0.002},
         CP: {AM: 0.014, GM: 0.014, CM: 0.014, TM: 0.014, AP: 0.002, GP: 0.86, CP: 0.08, TP: 0.002},
         TP: {AM: 1/16, GM: 1/16, CM: 1/16, TM: 1/16, AP: 1/36, GP: 1/3, CP: 1/3, TP: 1/36}}
    E = {AM: {'A': 1, 'G': 0, 'C': 0, 'T': 0},
         GM: {'A': 0, 'G': 1, 'C': 0, 'T': 0},
         CM: {'A': 0, 'G': 0, 'C': 1, 'T': 0},
         TM: {'A': 0, 'G': 0, 'C': 0, 'T': 1},
         AP: {'A': 1, 'G': 0, 'C': 0, 'T': 0},
         GP: {'A': 0, 'G': 1, 'C': 0, 'T': 0},
         CP: {'A': 0, 'G': 0, 'C': 1, 'T': 0},
         TP: {'A': 0, 'G': 0, 'C': 0, 'T': 1}}
#    for emit in S:
#        for probability in O:
#            if E[emit][probability] != 0:
#                E[emit][probability] = math.log2(E[emit][probability])
#            else:
#                E[emit][probability] = MINUS_INFINITY
#    for transit in S:
#        for probability in S:
#            if T[transit][probability] != 0:
#                T[transit][probability] = math.log2(T[transit][probability])
#            else:
#                T[transit][probability] = MINUS_INFINITY
#    for start in S:
#        pi[start] = math.log2(pi[start])

    most_likely_state_seq =  viterbi(S, O, pi, T, E, readf('/home/xenx/Downloads/Yersinia pestis CO92.fasta'))

    print('>', file=f)
    i = 0
    while i < len(most_likely_state_seq) // 2:
        print(*most_likely_state_seq[i:i+70], sep='', file=f)
        i += 70
