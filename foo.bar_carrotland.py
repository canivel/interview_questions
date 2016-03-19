__author__ = 'canivel'
'''
The rabbits are free at last, free from that horrible zombie science experiment. They need a happy, safe home, where they can recover.

You have a dream, a dream of carrots, lots of carrots, planted in neat rows and columns! But first, you need some land. And the only person who's selling land is Farmer Frida. Unfortunately, not only does she have only one plot of land, she also doesn't know how big it is - only that it is a triangle. However, she can tell you the location of the three vertices, which lie on the 2-D plane and have integer coordinates.

Of course, you want to plant as many carrots as you can. But you also want to follow these guidelines: The carrots may only be planted at points with integer coordinates on the 2-D plane. They must lie within the plot of land and not on the boundaries. For example, if the vertices were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).

Write a function answer(vertices), which, when given a list of three vertices, returns the maximum number of carrots you can plant.

The vertices list will contain exactly three elements, and each element will be a list of two integers representing the x and y coordinates of a vertex. All coordinates will have absolute value no greater than 1000000000. The three vertices will not be collinear.
'''

import math

def calculateFraction(a,b):
    a, b = abs(a),abs(b)
    while b:
        a, b = b, a%b
    return a

def answer(vertices):
    x1, y1, x2, y2, x3, y3 = vertices[0][0], vertices[0][1], vertices[1][0],vertices[1][1], vertices[2][0], vertices[2][1]
    lattice = 0
    lattice += calculateFraction(x1-x2, y1-y2)
    lattice += calculateFraction(x3-x2, y3-y2)
    lattice += calculateFraction(x1-x3, y1-y3)
    area = (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2.0
    return int(math.fabs(area)-lattice/2.0+1)

print (answer([[-1, -1], [1, 0], [0, 1]]))
print (answer([[2, 3], [6, 9], [10, 160]]))
print (answer([[91207, 89566], [-88690, -83026], [67100, 47194]]))
print (answer([[0,0],[1,1],[-1,2]]))
print (answer([[1,0],[-3,1],[12,-1]]))