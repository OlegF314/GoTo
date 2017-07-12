#print([string[i - key:i] for i in range(key)])
def dump_graph(outgoing, viz_fname):
    with open(viz_fname, 'w') as out_f:
        print('digraph ag{', file=out_f)
        for left, dict in outgoing.items():
            for right in dict:
                round_coverage = dict[right][0]
                print(left + '[label="{}"]'.format(left), file=out_f)
                print(right + '[label="{}"]'.format(right), file=out_f)
                print(
                    left + ' -> ' + right +
                    '[label="C = {}"]'.format(round_coverage),
                    file=out_f)
        print('}', file=out_f)


def sequening_mistakes_fix(graph_in, graph_out, bordercov, borderlen, covs, lens):
    vertices = list(graph_out.keys())
    for vert in vertices:
        next_vertices = list(graph_out[vert].keys())
        for neigh in next_vertices:
            if graph_out[vert][neigh][0] >= bordercov or len(graph_out[vert][neigh][1]) >= borderlen:
                continue
            del covs[covs.index(graph_out[vert][neigh][0])]
            del lens[lens.index(len(graph_out[vert][neigh][1]))]
            del graph_out[vert][neigh]
            del graph_in[neigh][vert]



def create_de_brujn_graph(file, k):
    first = True
    for read in get_reads(file):
        if first:
            graph_in = add_read_in(cut(read, k), {}, k)
            graph_out = add_read_out(cut(read, k), {}, k)
            first = False
        else:
            add_read_in(cut(read, k), graph_in, k)
            add_read_out(cut(read, k), graph_out, k)
            # print(len(graph_out))
    graph_in, graph_out, covs, lens = make_graphs_easier(graph_in, graph_out, k)
    bordercov = sum(covs) / len(graph_out) / 3
    borderlen = sum(lens) / len(graph_out) / 3
    while min(covs) <= bordercov and min(lens) <= borderlen:
        sequening_mistakes_fix(graph_in, graph_out, bordercov, borderlen, covs, lens)
        graph_in, graph_out, covs, lens = make_graphs_easier(graph_in, graph_out, k)
    print(len(graph_out))
    return graph_in, graph_out


def make_graphs_easier(graph_ins, graph_outs, key):
    outs_keys = list(graph_outs.keys())

    for vert in outs_keys:
        if vert not in graph_ins:
            continue
        if len(graph_ins[vert]) != 1 or len(graph_outs[vert]) != 1:
            continue

        outing = list(graph_outs[vert].keys())[0]
        ining = list(graph_ins[vert].keys())[0]
        s = graph_ins[vert][ining][1] + graph_outs[vert][outing][1][key:]
        graph_ins[outing][ining] = [len(graph_ins[vert][ining][1]) * graph_ins[vert][ining][0]/len(s) + len(graph_outs[vert][outing][1]) * graph_outs[vert][outing][0]/len(s), s]
        graph_outs[ining][outing] = [len(graph_ins[vert][ining][1]) * graph_ins[vert][ining][0]/len(s) + len(graph_outs[vert][outing][1]) * graph_outs[vert][outing][0]/len(s), s]

        del graph_ins[vert]
        del graph_outs[vert]
        del graph_ins[outing][vert]
        del graph_outs[ining][vert]
    covs = []
    lens = []
    for vert in graph_outs:
        for neigh in graph_outs[vert]:
            covs.append(graph_outs[vert][neigh][0])
            lens.append(len(graph_outs[vert][neigh][1]))

    return graph_ins, graph_outs, covs, lens



def get_reads(filename):
    i = 0
    reads = []
    with open(filename) as f:
        for line in f:
            if i % 4 == 1:
                reads.append(line.strip())
            i += 1
    return reads


# def cut(string, key):
#     array = []
#     for i in range(key, len(string) + 1):
#         array.append(string[i - key:i])
#     return array

def cut(string, key):
    array = []
    for i in range(len(string) - key + 1):
        array.append(string[i:i+key])
    return array


def add_read_out(array, out, key):
    for i in range(len(array) - 1):
        if array[i] not in out:
            out[array[i]] = {}
        if array[i + 1] not in out[array[i]]:
            out[array[i]][array[i + 1]] = [0, array[i] + array[i + 1][key - 1:]]
        out[array[i]][array[i + 1]][0] += 1
    return out


def add_read_in(array, inning, key):
    for i in range(len(array) - 1):
        if array[i + 1] not in inning:
            inning[array[i + 1]] = {}
        if array[i] not in inning[array[i + 1]]:
            inning[array[i + 1]][array[i]] = [0, array[i] + array[i + 1][key - 1:]]
        inning[array[i + 1]][array[i]][0] += 1
    return inning

# print(get_reads('/home/xenx/Downloads/s_6.first1000.fastq')[1])
for_in, for_out = create_de_brujn_graph('/home/xenx/Downloads/s_6.first1000.fastq', 14)
#for_in, for_out = create_de_brujn_graph('/home/xenx/Downloads/test (1).fastq', 2)
dump_graph(for_out, '/home/xenx/gcbvbfm/out.txt')