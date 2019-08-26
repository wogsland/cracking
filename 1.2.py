# Array & Strings

# 1.2

"""
create hash table from letters from one
see if the other has all the same

O(n+m)
n - length of 1st word
m - length of 2nd word
"""


def is_perm(test1, test2):
    letters = {}
    for x in test1:
        if x in letters.keys():
            letters[x] = letters[x] + 1
        else:
            letters[x] = 1
    for x in test2:
        if x in letters.keys():
            letters[x] = letters[x] - 1
            if 0 == letters[x]:
                del letters[x]
        else:
            return False
    return True


if is_perm('poop', 'oopp'):
    print 'poop <=> oopp'
else:
    print 'poop <!=> oopp'
if is_perm('zrwextcryvtubyiun', 'zrwextcryyceqqee'):
    print 'zrwextcryvtubyiun <=> zrwextcryyceqqee'
else:
    print 'zrwextcryvtubyiun <!=> zrwextcryyceqqee'
