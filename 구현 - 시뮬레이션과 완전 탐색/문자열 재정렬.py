# 내가 푼 방법
s = [i for i in input()] #K1A5C2
s.sort()

sum = 0
lett = ""
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "T", "U", "V", "W", "X", "Y", "Z"]

for i in s:
    if i in letters:
        lett += i
    else:
        sum += int(i)

print((lett + str(sum)))

# 해설
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))