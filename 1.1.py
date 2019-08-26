# Array & Strings

# 1.1

"""
create hash table from letters
if a letter is hit twice, fail
O(n)
"""


def unique_letters(test):
    letters = {}
    for x in test:
        if x in letters.keys():
            return False
        else:
            letters[x] = x
    return True


if unique_letters('poop'):
    print 'poop has all unique letters'
else:
    print 'poop does not have all unique letters'

if unique_letters('qwertyuiopasdfghjklzxcvbnm'):
    print 'qwertyuiopasdfghjklzxcvbnm has all unique letters'
else:
    print 'qwertyuiopasdfghjklzxcvbnm does not have all unique letters'
