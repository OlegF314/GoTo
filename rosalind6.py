s, t = input(), input()
distance = 0
for i in range(len(s)):
    if s[i] != t[i]:
        distance += 1
print(distance)