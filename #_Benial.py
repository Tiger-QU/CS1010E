# Crystal clarity
from turtle import *
reset()
speed(2000)
def upside_arrowhead(level, l):
        
    if level==1:
        lt(60)
        fd(l/2)
        rt(60)
        fd(l/2)
        rt(60)
        fd(l/2)
    else:
        if level%2==0:
            lt(60)
            reverse_arrowhead(level-1, l/2)
            rt(60)
            rt(60)
            upside_arrowhead(level-1, l/2)
            reverse_arrowhead(level-1, l/2)
        
        else:
            lt(60)    
            reverse_arrowhead(level-1, l/2)
            rt(60)
            upside_arrowhead(level-1, l/2)
            rt(60)
            reverse_arrowhead(level-1, l/2)


def reverse_arrowhead(level, l):
        
    if level==1:
        rt(60)
        fd(l/2)
        lt(60)
        fd(l/2)
        lt(60)
        fd(l/2)
    else:
        if level%2==0:
            rt(60)
            upside_arrowhead(level-1, l/2)
            lt(60)
            lt(60)
            reverse_arrowhead(level-1, l/2)

            upside_arrowhead(level-1, l/2)
        
        else:
            rt(60)    
            upside_arrowhead(level-1, l/2)
            lt(60)
            reverse_arrowhead(level-1, l/2)
            lt(60)
            upside_arrowhead(level-1, l/2)

upside_arrowhead(5,266)