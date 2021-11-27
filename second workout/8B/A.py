def add(tree, x):
    if not tree:
        tree.extend([x, None, None])
        print('DONE')
        return
    key = tree[0]
    if x == key:
        print('ALREADY')
    elif x < key:
        left = tree[1]
        if left == None:
            tree[1] = [x, None, None]
            print('DONE')
        else:
            add(left, x)  
    elif x > key:
        right = tree[2]
        if right == None:
            tree[2] = [x, None, None]
            print('DONE')
        else:
            add(right, x)


def find(tree, x):
    if not tree:
        return False
    key = tree[0]
    if x == key:
        return True
    elif x < key:
        left = tree[1]
        if left == None:
            return False
        else:
            return find(left, x)  
    elif x > key:
        right = tree[2]
        if right == None:
            return False
        else:
            return find(right, x)


def printtree(tree, count=0):
#    if not tree:
#        return
    if tree[1]:
        printtree(tree[1], count + 1)
    print(f"{''.join('.' * count)}{tree[0]}")
    if tree[2]:
        printtree(tree[2], count + 1)    

tree = []

with open('input.txt', 'r', encoding='utf-8') as file:
    string = file.readline().strip()
    while string != '':
        line = [i for i in string.split()]
        if line[0] == 'ADD':
            add(tree, int(line[1]))

        elif line[0] == 'SEARCH':
            if find(tree, int(line[1])):
                print('YES')
            else:
                print('NO')  

        elif line[0] == 'PRINTTREE':
            printtree(tree)           
        string = file.readline().strip()

        


