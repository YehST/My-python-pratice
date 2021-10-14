A = ["我好酷\n", "000", "123123"]
table = [A, A, A]
print(table)

for i in table:
    n = 0
    for j in i:
        j = j.replace("\n", "")
        i[n] = j
        n += 1
print(table)
