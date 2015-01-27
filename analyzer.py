# **********************Author Info**************************
# *@author    Christopher Findeisen                         *
# *@contact    <cfindeisen7@gmail.com>                      *
# *@date     Mon Jan 26 18:13:38 2015                       *
# ***********************************************************
from graphics import *
import time
f = open('generated_input.txt', 'r')


win = GraphWin('Coordinate Plane', 1000, 1000) # give title and dimensions
given_point_order = []
for line in f:
    print line
    numbers = line.split();
    x = int(numbers[0])
    y = int(numbers[1])
    #pt = Point( x, y )
    #pt.draw(win)
    given_point_order += [x,y]

f.close()
f = open('generated_output.txt', 'r')
prev_x = -1
prev_y = -1

# Scale Graph
padding = 10
xs = given_point_order[::2]
ys = given_point_order[1::2]
minX = min(xs)
minY = min(ys)
xScale = (1000.0 - 2.0*padding) / (max(xs) - minX)
yScale = (1000.0 - 2.0*padding) / (max(ys) - minY)
xTrans = -minX * xScale + padding
yTrans = -minY * yScale + padding
# End Scale Info
# Remove Scaling:
# xScale = 1
# yScale = 1
# xTrans = 0
# yTrans = 0

for line in f:
    numbers = line.split();
    pt_no = int(numbers[0]) * 2
    x = given_point_order[pt_no]
    y = given_point_order[pt_no+1]
    Point(x*xScale + xTrans, y*yScale + yTrans).draw(win)
    if prev_x >= 0:
        connection = Line(Point(prev_x*xScale + xTrans, prev_y*yScale + yTrans), Point(x*xScale + xTrans, y*yScale + yTrans))
        connection.draw(win)
        #if you want to see the graph traverse more slowly, uncomment this!
        # time.sleep(1)
    prev_x = x
    prev_y = y

win.getMouse() # Pause to view result
win.close()
