import serial_interface
import matplotlib
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from serial_interface import serialfunc

#layout
plt.style.use('fivethirtyeight')

#number generator function
def gen():
    i = 0
    while True:
        i = i +1
        yield i

#inputs to matplotlib
x_vals = []
y_vals = []
count = gen()

p = serialfunc()


def animate(i):
    x_vals.append(next(count))
    y_vals.append(next(p))

    plt.cla()
    plt.plot(x_vals[-50:],y_vals[-50:])



#what is this function
ani = FuncAnimation(plt.gcf(),animate,interval = 0)

#layout
plt.tight_layout
plt.xlabel("Time Value")
plt.ylabel("Output Value")
plt.show()
