import cairo
import math
import os
import random

# options
image_size = (2000, 2000)
line_strength = 1
CENTER = image_size[0]/2, image_size[1]/2
DOTS = 11
knit = 400
jump = 6

# container
dotslist = []

# basic setup
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, image_size[0], image_size[1])
ctx = cairo.Context(surface)

# draw background
ctx.rectangle(0, 0, image_size[0], image_size[1])
ctx.set_source_rgba(1, 1, 1, 1)
ctx.fill()

# dot class
class Dot:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number

# draw function
def drawline(start, end):
    ctx.set_source_rgba(random.randrange(0, 1), random.randrange(0, 1), random.randrange(0, 1), line_strength)
    ctx.set_line_width(4)
    ctx.move_to(start[0], start[1])
    ctx.line_to(end[0], end[1])
    ctx.stroke()

def drawcir(x, y):
    ctx.set_source_rgba(0, 0, 0, 1)
    ctx.arc(x, y, 5, 0, 2*math.pi)
    ctx.fill()

def drawloom():
    radius = image_size[0]/2*0.9
    dotdis = math.pi * 2 / DOTS

    for i in range(DOTS):
        x = CENTER[0] + math.cos(dotdis*i) * radius
        y = CENTER[1] + math.sin(dotdis*i) * radius
        dotslist.append(Dot(x, y, i+1))
        drawcir(x, y)

def drawshape():

    currentdot = dotslist[0]
    for i in range(knit):
        nextdot = dotslist[(currentdot.number + jump)%DOTS]
        drawline((currentdot.x, currentdot.y), (nextdot.x, nextdot.y))
        currentdot = nextdot


def main():
    drawloom()
    drawshape()

    i = 1
    while True:
        if os.path.exists(f'output{i}.png'):
            i += 1
            continue
        surface.write_to_png(f'output{i}.png')
        break



if __name__ == '__main__':
    main()
