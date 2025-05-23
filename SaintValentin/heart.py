import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from matplotlib.path import Path

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
    ax.fill(left_x, left_y, color='white')
    ax.fill(right_x, right_y, color='white')
    ax.add_patch(plt.Rectangle((-20, -20), 40, 40, color='red'))
    if frame == 29:
        ax.text(0, 0, "Bonne Saint Valentin!", fontsize=16, color='black', ha='center', fontweight='bold')  # Texte en noir
        scatter_hearts()
    return []

def on_click(event):
    global ani_opening
    ani.event_source.stop()  # Arrêter l'animation principale
    ani_opening = animation.FuncAnimation(fig, animate_opening, frames=30, interval=50, blit=False, repeat=False)
    plt.draw()

def scatter_hearts():
    for _ in range(20):
        x = random.uniform(-15, 15)
        y = random.uniform(-10, 10)
        heart_x, heart_y = heart_shape(np.linspace(0, 2 * np.pi, 100), scale=0.2, offset_x=x, offset_y=y)
        ax.plot(heart_x, heart_y, 'w', linewidth=1)
        dx = random.uniform(-0.5, 0.5)
        dy = random.uniform(0.5, 1.5)
        ax.arrow(x, y, dx, dy, head_width=0.1, head_length=0.2, fc='w', ec='w')

def on_hover(event):
    if is_inside_heart(event):
        ax.clear()
        ax.set_aspect('equal')
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        ax.axis('off')
        ax.add_patch(plt.Rectangle((-20, -20), 40, 40, color='red'))
        x, y = heart_shape(t)
        ax.fill(x, y, color='darkred')  # Survol du cœur avec couleur rouge foncé
        ax.text(0, 0, "Clique", fontsize=12, color='black', ha='center')
        plt.draw()
    else:
        ax.clear()
        ax.set_aspect('equal')
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        ax.axis('off')
        ax.add_patch(plt.Rectangle((-20, -20), 40, 40, color='red'))
        x, y = heart_shape(t)
        ax.fill(x, y, color='white')  # Cœur rempli en blanc
        plt.draw()

def is_inside_heart(event):
    mouse_x, mouse_y = event.xdata, event.ydata
    if mouse_x is not None and mouse_y is not None:
        x, y = heart_shape(t)
        heart_path = Path(list(zip(x, y)))  # Crée un chemin pour le cœur
        return heart_path.contains_point((mouse_x, mouse_y))  # Vérifie si la souris est à l'intérieur du cœur
    return False

t = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.axis('off')
x, y = heart_shape(t)
line, = ax.plot(x, y, 'w', linewidth=3)
ax.add_patch(plt.Rectangle((-20, -20), 40, 40, color='red'))
i = fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('motion_notify_event', on_hover)
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=False)
plt.show()
