
n = int(input())
str = list(map(int, input().split()))
dict = {}
for i in range(len(str)):
    if str[i] in dict:
        dict[str[i]] += 1
    else:
        dict[str[i]] = 1

t = sorted(dict.items(), key=lambda x: (x[1], x[0]))
t.sort(key=lambda x: x[1], reverse=True)

for i in range(len(t)):
    print(t[i][0], t[i][1])