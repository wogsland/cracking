# Array & Strings

# 1.3

"""
O(n) because we have to check every letter
"""


def replace_space(test):
    letters = ''
    for i, x in enumerate(test):
        if ' ' == x:
            letters = letters + '%20'
        else:
            letters = letters + x
    return letters


print replace_space('This is a test.')
