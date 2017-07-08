def f(array):
    max_len = 1
    prev = -1
    curr_len = 1
    for number in array:
        if number == prev:
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)
            prev = number
            curr_len = 1
    return  max_len

print(f([1, 3, 3, 2, 4, 4, 4, 6, 5, 2, 2, 2, 2, 2, 2, 2, 2, 0]))