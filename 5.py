def g(string):
    all_words = string
    max_count = 0
    max_word = ''
    words = list(set(all_words))
    for word in words:
#         print(all_words, words, word, max_count, max_word)
         if all_words.count(word) > max_count:
             max_count = all_words.count(word)
             max_word = word
    return max_word
def f(array):
    returning = ''
    for i in range(len(array)):
        array[i] = list(array[i])
    array1 = [[None for i in range(len(array))] for j in range(len(array[0]))]
    for i in range(len(array)):
        for j in range(len(array1)):
            array1[j][i] = array[i][j]
    for string in array1:
        returning += g(string)
    return returning

#print(f(['AAACCTTG',
#         'AACCCTTG',
#         'ACACCTTG',
#         'AAACCGGA']))