# from TicTacToe import TicTacToe
#
# game = TicTacToe()
# game.mark(0,0);     game.mark(0,1)
# game.mark(2,0);     game.mark(0,2)
# game.mark(1,1);     game.mark(2,1)
# game.mark(1,2);     game.mark(1,0)
# game.mark(2,2)
#
# print(game)
# winner = game.winner()
# if winner is None:
#     print("tie")
# else:
#     print(winner,"wins")

def add_set():
    first = [[2,3,4],[5,6,7],[8,9,0]]
    second = [[1,2,3],[4,5,6],[7,8,9]]
    n = 0
    for index in first:
        for row in index:
            n += 1
    third = []
    fourth = []
    fifth = []
    if len(first) > len(second):
        return False
    elif len(first) < len(second):
        return False
    else:
        for line in first:
            for num in line:
                third.append(num)

    for lot in second:
        for ball in lot:
            fourth.append(ball)

    for i in range(n):
        fifth.append(third[i] + fourth[i])
    print(fifth)

print(add_set())