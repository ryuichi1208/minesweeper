#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import random
from enum import Enum
from cell import Cell

class GameState(Enum):
    win = 1
    los = 2
    unf = 3

def neighborhood(x, y, width, height):
    neighbors = []
    for i in range(x-1, x+2) :
        for j in range(y-1, y+2) :
            if 0<=i<width and 0<=j<height  and not (i,j)==(x,y):
                neighbors = neighbors + [ (i,j) ]
    return neighbors


def make_grid(width, height, nbombs):
    assert 0 < width, 'width must be a positive integer'
    assert 0 < height, 'height must be a positive integer'
    assert 0 <= nbombs <= width * height, "nbombs must don't exceed width*height"
    coords = [(x, y) for y in range(height) for x in range(width)]
    random.shuffle(coords)
    grid = [[Cell() for y in range(height)] for x in range(width)]
    for i in range(nbombs):
        x,y=coords[i]
        grid[x][y].set_bomb()
        for neighbor in neighborhood(x, y, width, height):
            x1, y1 = neighbor
            grid[x1][y1].incr_number_of_bombs_in_neighborhood()
    return grid

class Minesweeper():

    def __init__(self, width=30, height=20, nbombs=99):
        self.w = width
        self.h = height
        self.nb = nbombs
        self.grid = make_grid(width, height, nbombs)

    def get_height(self):
        return self.h


    def get_width(self):
        return self.w

    def get_nbombs(self):
        return self.nb


    def get_cell(self, x, y):
        return self.grid[x][y]

    def get_state(self):
        n = 0
        state = 0
        width = self.w
        height = self.h
        nb_cases = width*height

        for i in range(0,width) :
            for j in range(0,height) :
                cel = self.get_cell(i,j)
                if cel.is_bomb() and cel.is_revealed():
                    state = 2
                    break
                elif (cel.is_revealed() and not cel.is_bomb()) or (not cel.is_revealed() and cel.is_bomb()):
                    n = n+1
            if state == 2:
                break

        if n == nb_cases:
            return GameState.winning
        elif state == 2:
            return GameState.losing
        else:
            return GameState.unfinished

    def reveal_all_cells_from(self, x, y):
        width = self.w
        height = self.h
        cel = self.get_cell(x,y)
        if cel.number_of_bombs_in_neighborhood() != 0:
            cel.reveal()
        elif cel.is_bomb():
            cel.reveal()
        else:
            listeVoisins = neighborhood(x, y, width, height)
            for i in range(0,len(listeVoisins)) :
                cel2=self.get_cell(listeVoisins[i][0],listeVoisins[i][1])
                if cel2.is_revealed()==False:
                    cel2.reveal()
                    self.reveal_all_cells_from(listeVoisins[i][0], listeVoisins[i][1])

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True) 
