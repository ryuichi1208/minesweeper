#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

class Cell():
    def __init__(self):
        self.bomb = False
        self.hypothetic = False
        self.nb_bombs_neighborhood = 0
        self.revealed = False

    def is_revealed(self):
        return self.revealed

    def reveal(self):
        self.revealed = True

    def is_bomb(self):
        return self.bomb

    def set_bomb(self):
        self.bomb = True

    def is_hypothetic(self):
        return self.hypothetic

    def set_hypothetic(self):
        self.hypothetic = True

    def unset_hypothetic(self):
        self.hypothetic = False

    def number_of_bombs_in_neighborhood(self):
        return self.nb_bombs_neighborhood

    def incr_number_of_bombs_in_neighborhood(self):
        self.nb_bombs_neighborhood += 1

    def __str__(self):
        if self.hypothetic==True:
            return "?"
        elif self.bomb==True:
            return "B"
        elif self.hypothetic ==False and self.bomb==False and self.revealed==False:
            return " "
        else:
            return str(self.nb_bombs_neighborhood)

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
