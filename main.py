#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from minesweeper import Minesweeper
from minesweeper import GameState
from cell import Cell
import sys

width = int(sys.argv[1])
height = int(sys.argv[2])
nbombs = int(sys.argv[3])

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

if game.get_state() == GameState.win :
    print("win")
elif game.get_state() == GameState.los :
    print("lose")
