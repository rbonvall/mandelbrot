#!/usr/bin/python

from __future__ import division
from Tkinter import Tk, Label
import Image
from ImageTk import PhotoImage
from random import randrange
range = xrange


def pixel(c, max_iterations=256):
    z = 0+0j
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) >= 2:
            break
    return i


def main():
    root = Tk()
    l = Label(root)
    l.pack()

    W, H = 300, 300
    im = Image.new('P', (W, H), 0)
    im.putpalette([randrange(256) for n in range(3 * 256)])
    p = im.load()

    for x in range(W):
        for y in range(H):
            z = 2 * complex(x/W - 0.5, y/W - 0.5)
            c = pixel(z)
            p[x, y] = c
        if x % 10 == 0:
            print "Columna %d" % x
    l.pim = PhotoImage(im)
    l.config(image=l.pim)

    root.mainloop()

if __name__ == '__main__':
    main()
