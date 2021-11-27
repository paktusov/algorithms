dict = {}

with open('input.txt', 'r', encoding='utf-8') as file:
    line = file.readline().strip()
    while line != '':
        words = [i for i in line.split()]
        for word in words:
            if word not in dict:
                dict[word] = 0
            dict[word] += 1
        line = file.readline().strip()
sor = []
for key, value in dict.items():
    sor.append((value, key))


for item in sorted(sor, key =  lambda x: (-x[0], x[1])):
    print(item[1])
#print(*sorted(sor, key =  lambda x: (-x[0], x[1])), sep = '\n')    
        