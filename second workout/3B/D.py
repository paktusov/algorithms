n = int(input())
numbers = {i for i in range(1, n+1)}
yes = set()
no= set()

temp = input()
while temp != 'HELP':
    temp = {int(i) for i in temp.split()}
    key = input()
    if key == 'YES':
        if yes:
            yes = yes & temp
        else:
            yes = temp    
    elif key == 'NO':
        if len(temp) > 1:
            numbers = numbers - temp  
        else:
            numbers.discard(*temp)         
    temp = input()
if yes:
    print(*sorted(numbers & yes))  
else:
    print(*sorted(numbers))              