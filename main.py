import sys
from minesweeper import Minesweeper
from minesweeper import GameState
from calc import Calc

def main(l):

    print(l)

    width,height,nbombs = int(l[1]),int(l[2]),int(l[3])

    print('  ', end='')
    for i in range(0, width) :
        print("   {:d}".format(i), end='')
    print('\n','  +', '---+'*width, sep='')
    for i in range(0,height) :
        print(' {:d}|'.format(i), end='')
        for j in range(0, width) :
            print('   |', end='')
        print('\n','  +', '---+'*width, sep='')

game = Minesweeper(width, height, nbombs)

while game.get_state() == GameState.unfinished :
    s = input().split()
    x, y = int(s[0]), int(s[1])
    action = s[2]
    cel = game.get_cell(x,y)

    if action == 'R' :
        game.reveal_all_cells_from(x, y)
    elif action == 'S' :
        cel.set_hypothetic()
    elif action == 'U' :
        cel.unset_hypothetic()

    print('  ', end='')
    for i in range(0, width) :
        print("   {:d}".format(i), end='')
    print('\n','  +', '---+'*width, sep='')

    for i in range(0,height) :
        print(' {:d}|'.format(i), end='')
        for j in range(0, width) :
            c=game.get_cell(j,i)
            if c.is_revealed() :
                if c.is_bomb() :
                    v = 'B'
                elif c.is_hypothetic() :
                    v = '?'
                else :
                    v = str(c.number_of_bombs_in_neighborhood())
            elif c.is_hypothetic() :
                    v = '?'
            else :
                v = ' '
            print('  {:s}|'.format(v), end='')
        print('\n','  +', '---+'*width, sep='')

if __name__ == "__main__":
    main(sys.argv)
