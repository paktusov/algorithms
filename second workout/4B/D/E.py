dict = {}
dict_count = {}

with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())
    for i in range(1, n+1):
        flag =  int(file.readline().strip())
        if flag == 0:
            them = file.readline().strip()
            dict[i] = them
#            if them not in dict_count:
            dict_count[them] = 1
#            dict_count[them] += 1    
            message = file.readline().strip()
        else:
            dict[i] = dict[flag]
            dict_count[dict[flag]] += 1 
            message = file.readline().strip()

print(max(dict_count.items(), key = lambda x: x[1])[0])            


    
