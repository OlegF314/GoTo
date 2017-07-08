flag_nor = 0
l_nor = 0
r_nor = 0
flag_hyp = 0
l_hyp = 0
r_hyp = 0
names = []
genes_plus = []
genes_minus = []

with open("/home/xenx/genome_annotation.gtf") as f:
    for line in f:
        gene_info = line.strip().split('\t')
        names.append(line.strip().split('"')[5])
        if gene_info[6] == '+':
            genes_plus.append([int(gene_info[3]), int(gene_info[4]), gene_info[6], line.strip().split('"')[5], 0, 0])
        if gene_info[6] == '-':
            genes_minus.append([int(gene_info[3]), int(gene_info[4]), (gene_info[6]), line.strip().split('"')[5], 0, 0])


def count_reads(file, ind):
    with open(file) as f:
        current_gen_plus = 0
        current_gen_minus = 0
        for line in f:
            if line[0] == "@":
                continue
            gene_info = line.strip().split('\t')
            flag_nor = int(gene_info[1])
            l_nor = int(gene_info[3])
            r_nor = l_nor + len(gene_info[9])

            if flag_nor & 4:
                continue
            if flag_nor & 16:
                while current_gen_minus < len(genes_minus):
                    # print(left_n, right_n, stminus[t_genm][0], stminus[t_genm][1])
                    if r_nor < genes_minus[current_gen_minus][0]:
                        break
                    elif l_nor < genes_minus[current_gen_minus][1] and r_nor > genes_minus[current_gen_minus][0]:
                        genes_minus[current_gen_minus][ind] += 1
                        # print('plus')
                        break
                    else:
                        current_gen_minus += 1
            else:
                while current_gen_plus < len(genes_plus):
                    if r_nor < genes_plus[current_gen_plus][0]:
                        break
                    elif l_nor < genes_plus[current_gen_plus][1] and r_nor > genes_plus[current_gen_plus][0]:
                        genes_plus[current_gen_plus][ind] += 1
                        break
                    else:
                        current_gen_plus += 1


count_reads("/home/xenx/THYP2_22.sam", 4)
count_reads("/home/xenx/TNOR2_22.sam", 5)

with open("summon_cthulhu.out", 'w') as f:
    for gene in genes_plus:
        print(gene[3], gene[4], gene[5], sep='\t', file=f)
    for gene in genes_minus:
        print(gene[3], gene[4], gene[5], sep='\t', file=f)
