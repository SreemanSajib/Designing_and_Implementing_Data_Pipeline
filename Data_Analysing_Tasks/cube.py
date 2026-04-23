import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Defined the 8 corners (vertices) of the cube
cube_points = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
])

# Multiplied by 10 to make the cube bigger
cube_points = cube_points * 10

# Lines that will connect the corners
lines = [
    [0, 1], [1, 2], [2, 3], [3, 0], # Base
    [4, 5], [5, 6], [6, 7], [7, 4], # Top
    [0, 4], [1, 5], [2, 6], [3, 7]  # Sides
]

def rotation_x(angle_deg):
    # Math for rotation around the X-axis
    angle_rad = np.radians(angle_deg)
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    return np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]
    ])

def rotation_y(angle_deg):
    # Math for rotation around the Y-axis
    angle_rad = np.radians(angle_deg)
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    return np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]
    ])

def rotation_z(angle_deg):
    # Math for rotation around the Z-axis
    angle_rad = np.radians(angle_deg)
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    return np.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1]
    ])

def draw_cube(val):
    # Clear the previous cube
    ax.cla()
    
    # Set limits (to keep it fitted on the screen)
    ax.set_xlim([-30, 30])
    ax.set_ylim([-30, 30])
    ax.set_zlim([-30, 30])
    
    # Get current angles from sliders
    angle_x = slider_x.val
    angle_y = slider_y.val
    angle_z = slider_z.val
    
    # Calculate rotation matrices
    mat_x = rotation_x(angle_x)
    mat_y = rotation_y(angle_y)
    mat_z = rotation_z(angle_z)
    
    # Combine all three rotations
    combined_matrix = mat_z @ mat_y @ mat_x
    
    # Rotate each point
    rotated_points = cube_points @ combined_matrix.T
    
    # Draw lines using the new points
    for p1_idx, p2_idx in lines:
        x_coords = [rotated_points[p1_idx, 0], rotated_points[p2_idx, 0]]
        y_coords = [rotated_points[p1_idx, 1], rotated_points[p2_idx, 1]]
        z_coords = [rotated_points[p1_idx, 2], rotated_points[p2_idx, 2]]
        ax.plot3D(x_coords, y_coords, z_coords, color='blue')
        
    fig.canvas.draw_idle()

# Main application window setup
fig = plt.figure(figsize=(7, 8))
fig.canvas.manager.set_window_title('Cube Rotator')

# 3D plot area
ax = fig.add_axes([0.1, 0.35, 0.8, 0.6], projection='3d')

# Space for creating sliders
ax_x = fig.add_axes([0.25, 0.20, 0.5, 0.03])
ax_y = fig.add_axes([0.25, 0.13, 0.5, 0.03])
ax_z = fig.add_axes([0.25, 0.06, 0.5, 0.03])

# Initialize sliders
slider_x = Slider(ax_x, 'X°:', 0, 360, valinit=74.1)
slider_y = Slider(ax_y, 'Y°:', 0, 360, valinit=15.9)
slider_z = Slider(ax_z, 'Z°:', 0, 360, valinit=105.9)

# Call draw_cube function whenever slider moves
slider_x.on_changed(draw_cube)
slider_y.on_changed(draw_cube)
slider_z.on_changed(draw_cube)

# Called once for the initial drawing
draw_cube(0)

plt.show()