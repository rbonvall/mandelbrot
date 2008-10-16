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

def z_converter(img_width, img_height, z_min=-2-2j, z_max=2+2j):
    z_diff = z_max - z_min
    scale_re = z_diff.real / img_width
    scale_im = z_diff.imag / img_height
    def z(x, y):
        return z_min + complex(x * scale_re, y * scale_im)
    return z

def main():
    root = Tk()
    l = Label(root)
    l.pack()

    W, H = 300, 300
    im = Image.new('P', (W, H), 0)
    im.putpalette([randrange(256) for n in range(3 * 256)])
    p = im.load()
    
    vertex = 1e-3 + 1e-3j
    z = z_converter(W, H, -vertex, +vertex)
    for x in range(W):
        for y in range(H):
            p[x, y] = pixel(z(x, y))
        if x % 10 == 0:
            print "Columna %d" % x
    l.pim = PhotoImage(im)
    l.config(image=l.pim)

    root.mainloop()

if __name__ == '__main__':
    main()
