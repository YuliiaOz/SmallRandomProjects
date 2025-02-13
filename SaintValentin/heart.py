import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def heart_shape(t, scale=1, offset_x=0, offset_y=0):
    x = 16 * np.sin(t) ** 3 * scale + offset_x
    y = (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)) * scale + offset_y
    return x, y

def update(frame):
    scale = 1 + 0.05 * np.sin(frame / 5)
    x, y = heart_shape(t, scale)
    line.set_data(x, y)
    return line,

def animate_opening(frame):
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.axis('off')
    
    split_factor = frame / 30
    left_x, left_y = heart_shape(t, scale=1, offset_x=-split_factor * 8)
    right_x, right_y = heart_shape(t, scale=1, offset_x=split_factor * 8)
    
    ax.plot(left_x, left_y, 'r', linewidth=3)
    ax.plot(right_x, right_y, 'r', linewidth=3)
    
    if frame == 29:
        ax.text(0, 0, "Bonne Saint Valentin!", fontsize=16, color='red', ha='center', fontweight='bold')
        scatter_hearts()
    
    return []

def on_click(event):
    global ani_opening
    ani.event_source.stop()
    ani_opening = animation.FuncAnimation(fig, animate_opening, frames=30, interval=50, blit=False, repeat=False)
    plt.draw()

def scatter_hearts():
    for _ in range(20):
        x = random.uniform(-15, 15)
        y = random.uniform(-10, 10)
        heart_x, heart_y = heart_shape(np.linspace(0, 2 * np.pi, 100), scale=0.2, offset_x=x, offset_y=y)
        ax.plot(heart_x, heart_y, 'r', linewidth=1)

t = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.axis('off')

x, y = heart_shape(t)
line, = ax.plot(x, y, 'r', linewidth=3)

i = fig.canvas.mpl_connect('button_press_event', on_click)
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()