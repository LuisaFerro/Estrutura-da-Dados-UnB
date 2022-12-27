x = {1:30,0:30} #o da esquerda é a chave e o da direita é a quantidade de repetições


def permutations_unique(x, curr_list=[]):
    if not x:
        yield curr_list
        return
    last_item = None
    if curr_list:
        last_item = curr_list[-1]
    for item in x:
        if item != last_item:
            for j in range(1, x[item] + 1):
                xchild = dict(x)
                xchild[item] -= j
                if xchild[item] == 0:
                    del xchild[item]
                for y in permutations_unique(xchild, curr_list + [item] * j):
                    yield y

a = permutations_unique(x)
for i in a:
    print(i)
