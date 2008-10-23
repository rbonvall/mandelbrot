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

def z_converter(img_width, img_height, center=0+0j, side=4.0):
    def z(x, y):
        return center + side * complex(x/img_width - 0.5, y/img_height - 0.5)
    return z

def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-W', '--width',  type='int', default=300)
    parser.add_option('-H', '--height', type='int', default=300)
    parser.add_option('-c', '--center', type='complex', default=0+0j)
    parser.add_option('-s', '--side',   type='float', default=4)
    (options, args) = parser.parse_args()

    root = Tk()
    l = Label(root)
    l.pack()

    W, H = options.width, options.height
    center, side = options.center, options.side

    im = Image.new('P', (W, H), 0)
    im.putpalette([randrange(256) for n in range(3 * 256)])
    p = im.load()
    
    z = z_converter(W, H, center, side)
    l.pim = PhotoImage(im)
    l.config(image=l.pim)

    def paint_column(x):
        if x % 10 == 0: print "Column %d" % x
        for y in range(H):
            p[x, y] = pixel(z(x, y))
        l.pim = PhotoImage(im)
        l.config(image=l.pim)

        if x + 1 < W:
            root.after(1, paint_column, x + 1)

    def start(event):
        root.after(1, paint_column, 0)

    root.bind('<FocusIn>', start)
    root.mainloop()

if __name__ == '__main__':
    main()
