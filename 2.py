def f(string):
    all_words = string.split()
    max_count = 0
    words = list(set(all_words))
    for word in words:
         if all_words.count(word) > max_count:
             max_count = all_words.count(word)
             max_word = word
    return max_word
