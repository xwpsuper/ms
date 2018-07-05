# import itertools

# L = [i for i in range(1, 34)]

# print(L)

# a = list(itertools.combinations(L, 6))
# print(len(a), type(a))
# print(a[:10])

# b = list(set(a))
# print(len(b))

import itertools
import random

def qp5(list1):
    LL = []
    if len(list1) >= 5:
        for i in range(len(list1)):
            if (i+1)%5 == 0:
                l = list1[:5]
                l.sort()
                LL.append(l)
                for i in l:
                    if i in list1:
                        list1.remove(i)
            else:
                pass
    return LL
L = list(range(1, 36))
random.shuffle(L)
LL = qp5(L)
with open('yybf.txt', 'a') as f:
    f.write(str(LL) + '\n')
