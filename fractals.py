# Super Awesome Fractal!
# Ben Storlie
# 20 September 2012
#

import turtle
import sys
sys.setrecursionlimit(60000)



turtle.speed(0)
turtle.hideturtle()

# size=10 is good for higher levels.
# size=2 is good for super high levels.
# 20 or 30 could work for the lower ones.
# n=4 to n=6 is a good start.  After that you have to wait a really long
# time for the whole thing to get drawn.  n=11 is pretty much the maximum.

def fractal(n,size,fillcolor='white'):
    turtle.begin_fill()
    turtle.fillcolor(fillcolor)
    startL=[1,1,1]    #This gives just a regular triangle.
                      #[0,0] will give a zigzag, like a frieze pattern.
    lens=lengths(startL,n)  #lengths of each edge
    turs=Bturns(lens)       #turns left or right

    for i in iter(range(0,len(lens))):

        turtle.forward(size*(lens[i]+1))
        if turs[i]==1:
            turtle.right(120)
        else:
            turtle.left(120)
    turtle.end_fill()

# The following two functions, 'lengths' and 'binary', give the order of
# short/long line segments in the nth iteration of the fractal. 1 means
# long and 0 means short.
# The starting L should be [1,1,1], since that's just a regular triangle.
# Every 1 turns into 1,0,0. And every 0 turns into 1,0. So,
# 111 -> 100 100 100
# -> 100 10 10 100 10 10 100 10 10

def lengths(L,n):

    if n==1:
        return L
    else:
        return binary(lengths(L,n-1))

def binary(L):

    if L==[]:
        return []
    elif L[0]==1:
        return [1,0,0]+binary(L[1:])
    elif L[0]==0:
        return [1,0]+binary(L[1:])


# B(inary)turns records the left and right turns of the curve. 1 means right,
# 0 means left. A long (1) length turns the same direction as it just did,
# making a 'C' shape. A short (0) length turns the opposite direction,
# making a 'Z' shape.

def Bturns(L):

    turnList=list(range(0,len(L)))
    turnList[0]=1
    for i in iter(range(1,len(L))):
        if L[i]==1:
            turnList[i]=turnList[i-1]
        elif L[i]==0:
            turnList[i]=1-turnList[i-1]

    return turnList
        

