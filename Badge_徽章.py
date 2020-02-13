# Crystal clarity
from turtle import *
reset()
speed(1000)
def tiger(level, l):
    if level%2!=0:
        lt(60)
    if level==1:
        fd(l/2)
        rt(60)
        fd(l/2)
        rt(60)
        fd(l/2)
    else:
        lion(level-1, l/2)
        rt(60)
        lion(level-1, l/2)
        rt(60)
        lion(level-1, l/2)


def lion(level, l):
    if level%2!=0:
        rt(60)
    if level==1:
        fd(l/2)
        lt(60)
        fd(l/2)
        lt(60)
        fd(l/2)
    else:
        tiger(level-1, l/2)
        lt(60)
        tiger(level-1, l/2)
        lt(60)
        tiger(level-1, l/2)

tiger(8,500)
