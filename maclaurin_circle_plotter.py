import math
import numpy
from matplotlib import pyplot as plt

def cos_accuracy(point):
    counter = 0
    last_estimate = -1
    estimate = 0
    while counter < 15:
        last_estimate = estimate
        estimate += maclaurin_cos(counter, point)
        counter += 1
    return estimate

def sin_accuracy(point):
    counter = 0
    last_estimate = -1
    estimate = 0
    while counter < 15:
        last_estimate = estimate
        estimate += maclaurin_sin(counter, point)
        counter += 1
    return estimate

def maclaurin_sin(r,x): # Formula for r-th term of sin maclaurin series
    return (((-1)**r)*(((x)**((2*r) + 1))/(math.factorial((2*r) + 1))))

def maclaurin_cos(r,x):
    return (((-1)**r)*(((x)**(2*r))/(math.factorial(2*r))))

def deg2rad(deg):
    return (numpy.pi/180)*deg
def rad2deg(rad):
    return (rad*180)/numpy.pi

ypoints = []
xpoints = []

for angle in range(0, 180): # Loop through every degree in semi-circle (makes calculations more time efficient)
    angle_rad = deg2rad(angle)
    x = cos_accuracy(angle_rad)
    xpoints.append(x)
    
    y = sin_accuracy(angle_rad)
    ypoints.append(y)

    # Plot point on other side
    xOpp = x - (x * -2)
    yOpp = y

    xpoints.append(xOpp)
    ypoints.append(yOpp)

print(ypoints)
print(xpoints)

plt.plot(xpoints, ypoints)
plt.axis("equal")
plt.grid()
plt.show()
