dict = {}

with open('input.txt', 'r', encoding='utf-8') as file:
    line = file.readline().strip()
    while line != '':
        name, count = line.split()
        count = int(count)
        if name not in dict:
            dict[name] = 0
        dict[name] += count
        line = file.readline().strip()

for key in sorted(dict):
    print(key, dict[key])            
