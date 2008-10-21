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
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-W', '--width',  type='int', default=300)
    parser.add_option('-H', '--height', type='int', default=300)
    parser.add_option('-f', '--z-min',  type='complex', default=-2-2j)
    parser.add_option('-t', '--z-max',  type='complex', default=+2+2j)
    (options, args) = parser.parse_args()

    root = Tk()
    l = Label(root)
    l.pack()

    W, H = options.width, options.height
    z_min, z_max = options.z_min, options.z_max

    im = Image.new('P', (W, H), 0)
    im.putpalette([randrange(256) for n in range(3 * 256)])
    p = im.load()
    
    z = z_converter(W, H, z_min, z_max)
    l.pim = PhotoImage(im)
    l.config(image=l.pim)

    def draw(event):
        for x in range(W):
            for y in range(H):
                p[x, y] = pixel(z(x, y))
        l.pim = PhotoImage(im.copy())
        l.config(image=l.pim)
    root.bind('<FocusIn>', draw)

    root.mainloop()

if __name__ == '__main__':
    main()
