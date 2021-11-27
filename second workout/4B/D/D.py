dict = {}
sum = 0
with open('input.txt', 'r', encoding='utf-8') as file:
    line = file.readline().strip()
    while line != '':
        temp_line = [i for i in line.split()]
        name = ' '.join(temp_line[:-1])
        count = int(temp_line[-1])
        sum += count
        dict[name] = count
        line = file.readline().strip()

first_voice = sum/450
dict_result = {}
count = 0
dict_temp = {}

for key in dict:
    if key not in dict_result:
        dict_result[key] = int(dict[key] // first_voice)
        fract_part = (dict[key]/ first_voice) % 1
        count += dict_result[key]
        dict_temp[(fract_part, dict[key])] = key

#print(dict_temp)        



while count != 450:
    for key in sorted(dict_temp, reverse=True):
        dict_result[dict_temp[key]] += 1
        count += 1
        if count == 450:
            break
    
    
#    fract_part = 0
#    for key, value in sorted(dict.items(), key = lambda x: x[1], reverse=True):
#        print((dict[key]/ first_voice) % 1)
#        if (dict[key]/ first_voice) % 1 > fract_part:
#            fract_part = dict[key]/ first_voice % 1
#            voice_key = key
    
#    print(voice_key, fract_part)

#    dict_result[voice_key] += 1
#    count += 1
#    dict.pop(voice_key)


for key, item in dict_result.items():
    print(key, item)
#print(dict_result)            


            




    
