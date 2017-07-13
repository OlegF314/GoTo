def find_message(string):
    returning = ''
    for i in string:
        if i.isalpha() and i.isupper():
            returning += i
    return returning
find_message(input())