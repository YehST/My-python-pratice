str3 = "Python程式設計"
for ch in str3:
    print(ch)
print(str3[3])
str1 = "Python"
print(str1.islower())
str2 = "YunTech"
print(max(str2))
lis1 = [1, [2, 3, 4], [5, 6]]
print("lis1:"+str(lis1))
lis1[2][1] = "Python"
print("lis1:"+str(lis1))
lis2 = [1, 2, 3, 4, 5, 6]
for i in lis2:
    print(i, end="")
lis2.append(7)
print('\n'+"lis2:"+str(lis2))
lis2.extend("1")
print("lis2:"+str(lis2))
lis2.insert(1, 5)
print("lis2:"+str(lis2))
el = lis2.pop()
print(el, lis2)
lis2.remove(5)
print(lis2)
d1 = {1: 'apple', 2: 'banana'}
d2 = {"name": "joe", 1: [2, 4, 6]}
d3 = dict([(1, "tom"), (2, "tim"), (3, "june")])
d4 = dict([("tom", 1), ("brown", 2), ("june", 3)])
print(d1, d2, d3, d4)
for people in d4:
    num = d4[people]
    print(people, num, end=",")


def con(c):
    f = (9.0*c)/5.0+32.0
    return f


print(con(30))
