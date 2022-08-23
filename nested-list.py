# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
notas = []
records = {}
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())

    records[name] = score
    notas.append(score)
notas.sort()
slg = 0
names = []
for i in notas:
    if i > notas[0]:
        slg = i
        break

for i in records.items():
    if i[1] == slg:
        names.append(i[0])
names.sort()
for e in names:
    print(e)
