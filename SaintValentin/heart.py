# test 
# test 2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def heart_shape(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

def update(frame):
    scale = 1 + 0.05 * np.sin(frame / 5)
    x, y = heart_shape(t)
    line.set_data(x * scale, y * scale)
    return line,

t = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.axis('off')

x, y = heart_shape(t)
line, = ax.plot(x, y, 'r', linewidth=3)

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()