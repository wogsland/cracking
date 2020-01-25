"""
Robot in upper left corner of grid of r rows and c columns. Can only move right
and down but some cells are "off limits". Get robot to bottom right.

My first thought is that this is not necessarily possible, because once the
robot has made a bad choice then they're stuck because it can't go back. And
also the density of off limits cells may make this impossible.
"""


def move_robot(x, y):
    if can_move(x + 1, y):
        return move_robot(x + 1, y)
    elif can_move(x, y - 1):
        return move_robot(x, y - 1)
    elif c = x and -r = y:
        return True
    else:
        return False

# O(r+c) - but this can fail


"""
Assuming instead that the robot can try again after failing, there's instead a
more complex solution.
"""

# O(RC) - will find path if it exists


def move_robot(x, y, path):
    if can_move(x + 1, y):
        path.append([x + 1, y])
        return move_robot(x + 1, y, path)
    if can_move(x, y - 1):
        path.append([x, y - 1])
        return move_robot(x, y - 1, path)
    if c = x and -r = y:
        return path
    return False


move_robot()

clusterf&*k
