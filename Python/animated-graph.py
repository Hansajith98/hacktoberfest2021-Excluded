import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

x = np.arange(0, 10*np.pi, 0.01)
y = -(np.sin(-5*x))/np.pi 

y1 = -(np.sin((-5)*x))/np.pi + -(np.sin((-10)*x))/(2*np.pi)
y2 = -(np.sin((-5)*x))/np.pi + -(np.sin((-10)*x))/(2*np.pi) + -(np.sin((-15)*x))/(3*np.pi)

fig = plt.figure()
ax = plt.subplot(1, 1, 1)

data_skip = 50


def init_func():
    ax.clear()
    plt.xlabel('pi')
    plt.ylabel('sin(pi)')
    plt.xlim((x[0], x[-1]))
    plt.ylim((-1, 1))



def update_plot(i):
    ax.plot(x[i:i+data_skip], y[i:i+data_skip], color='k')
    ax.scatter(x[i], y[i], marker='o', color='r')





anim = FuncAnimation(fig,
                     update_plot,
                     frames=np.arange(0, len(x), data_skip),
                     init_func=init_func,
                     interval=20)

#anim.save('sine.gif', dpi=150, fps = 30, writer='ffmpeg')
plt.show()