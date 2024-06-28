import matplotlib.patches
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import code

max_limit_beevision182 = (80, 60, 105)
min_limit_beevision182 = (5, 5, 5)

max_limit_beevision182s = (80, 60, 40)
min_limit_beevision182s = (5, 5, 2)

# Define the pyramid dimensions
pyramid_182 = {
    'top_x': 35,
    'base_x': 140,
    'top_y': 25,
    'base_y': 107.1,
    'max_length': max_limit_beevision182[0],
    'max_width': max_limit_beevision182[1],
    'min_height': min_limit_beevision182[2],
    'area_height': 105
}

pyramid_182s = {
    'top_x': 50,
    'base_x': 81.6,
    'top_y': 40,
    'base_y': 61.0,
    'max_length': max_limit_beevision182s[0],
    'max_width': max_limit_beevision182s[1],
    'min_height': min_limit_beevision182s[2],
    'area_height': 40
}

# Box dimensions
# box = (35, 25, 105)
scale_beevision182 = (100, 80, 5)
scale_beevision182s = (80, 60, 5)

# Function to create the vertices of the pyramid
def create_pyramid_vertices(pyramid):
    half_base_x = pyramid['base_x'] / 2
    half_base_y = pyramid['base_y'] / 2
    half_top_x = pyramid['top_x'] / 2
    half_top_y = pyramid['top_y'] / 2

    # Vertices of the base rectangle
    base_vertices = np.array([
        [-half_base_x, -half_base_y, 0],
        [half_base_x, -half_base_y, 0],
        [half_base_x, half_base_y, 0],
        [-half_base_x, half_base_y, 0]
    ])

    # Vertices of the top rectangle
    top_vertices = np.array([
        [-half_top_x, -half_top_y, pyramid['area_height']],
        [half_top_x, -half_top_y, pyramid['area_height']],
        [half_top_x, half_top_y, pyramid['area_height']],
        [-half_top_x, half_top_y, pyramid['area_height']]
    ])

    # Combine base and top vertices
    vertices = np.concatenate((base_vertices, top_vertices), axis=0)
    return vertices

# Function to create the vertices of the box


def create_box_vertices(box):
    x, y, z = box
    half_x = x / 2
    half_y = y / 2

    # Vertices of the box
    vertices = np.array([
        [-half_x, -half_y, 0],
        [half_x, -half_y, 0],
        [half_x, half_y, 0],
        [-half_x, half_y, 0],
        [-half_x, -half_y, z],
        [half_x, -half_y, z],
        [half_x, half_y, z],
        [-half_x, half_y, z]
    ])
    return vertices

def create_scale_vertices(scale):
    x, y, z = scale
    half_x = x / 2
    half_y = y / 2

    # Vertices of the box
    vertices = np.array([
        [-half_x, -half_y, -z],
        [half_x, -half_y, -z],
        [half_x, half_y, -z],
        [-half_x, half_y, -z],
        [-half_x, -half_y, 0],
        [half_x, -half_y, 0],
        [half_x, half_y, 0],
        [-half_x, half_y, 0]
    ])
    return vertices

# Function to plot the pyramid and the box


def plot_pyramid_and_box(product_type, box):
    pyramid = (0,0,0)
    scale = (0,0,0)

    if product_type == 'beevision182':
        pyramid = pyramid_182
        scale = scale_beevision182
    elif product_type == 'beevision182s':
        pyramid = pyramid_182s
        scale = scale_beevision182s
    else:
        print('plot_pyramid_and_box: Product not found.(Supported products: beevision182, beevision182s)')
        return

    is_obj_fit = code.test_box(pyramid, box)

    pyramid_vertices = create_pyramid_vertices(pyramid)
    box_vertices = create_box_vertices(box)
    scale_vertices = create_scale_vertices(scale)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    fig.canvas.manager.set_window_title(product_type.upper() + ' ANALYSIS')

    # Define the faces of the pyramid
    pyramid_faces = [
        [pyramid_vertices[0], pyramid_vertices[1],
            pyramid_vertices[5], pyramid_vertices[4]],
        [pyramid_vertices[1], pyramid_vertices[2],
            pyramid_vertices[6], pyramid_vertices[5]],
        [pyramid_vertices[2], pyramid_vertices[3],
            pyramid_vertices[7], pyramid_vertices[6]],
        [pyramid_vertices[3], pyramid_vertices[0],
            pyramid_vertices[4], pyramid_vertices[7]],
        [pyramid_vertices[4], pyramid_vertices[5],
            pyramid_vertices[6], pyramid_vertices[7]],
        [pyramid_vertices[0], pyramid_vertices[1],
            pyramid_vertices[2], pyramid_vertices[3]]
    ]

    # Define the faces of the box
    box_faces = [
        [box_vertices[0], box_vertices[1], box_vertices[5], box_vertices[4]],
        [box_vertices[1], box_vertices[2], box_vertices[6], box_vertices[5]],
        [box_vertices[2], box_vertices[3], box_vertices[7], box_vertices[6]],
        [box_vertices[3], box_vertices[0], box_vertices[4], box_vertices[7]],
        [box_vertices[4], box_vertices[5], box_vertices[6], box_vertices[7]],
        [box_vertices[0], box_vertices[1], box_vertices[2], box_vertices[3]]
    ]

    scale_faces = [
        [scale_vertices[0], scale_vertices[1], scale_vertices[5], scale_vertices[4]],
        [scale_vertices[1], scale_vertices[2], scale_vertices[6], scale_vertices[5]],
        [scale_vertices[2], scale_vertices[3], scale_vertices[7], scale_vertices[6]],
        [scale_vertices[3], scale_vertices[0], scale_vertices[4], scale_vertices[7]],
        [scale_vertices[4], scale_vertices[5], scale_vertices[6], scale_vertices[7]],
        [scale_vertices[0], scale_vertices[1], scale_vertices[2], scale_vertices[3]]
    ]

    # Create 3D polygon collections
    pyramid_poly3d = Poly3DCollection(
        pyramid_faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.25)
    box_poly3d = Poly3DCollection(
        box_faces, facecolors='magenta', linewidths=1, edgecolors='b', alpha=0.25)
    scale_poly3d = Poly3DCollection(
        scale_faces, facecolors='black', linewidths=1, edgecolors='black', alpha=0.25)

    ax.add_collection3d(pyramid_poly3d)
    ax.add_collection3d(box_poly3d)
    ax.add_collection3d(scale_poly3d)

    ax.text(0.5, 0.5, -5, "Scale", color='black', fontsize=8, ha='center')
    ax.text(0.5, 0.5, box[2]/2, "Object", color='black', fontsize=8, ha='center')

    fig.text(0.01, 0.95, 'Object length:', va='center', rotation='horizontal', fontsize=10, color='black')
    fig.text(0.01, 0.90, 'Object width:', va='center', rotation='horizontal', fontsize=10, color='black')
    fig.text(0.01, 0.85, 'Object height:', va='center', rotation='horizontal', fontsize=10, color='black')

    dim_swap = int(box[1] > box[0])

    fig.text(0.18, 0.95, str(box[dim_swap]), va='center', rotation='horizontal', fontsize=10, color='black')
    fig.text(0.18, 0.90, str(box[1-dim_swap]), va='center', rotation='horizontal', fontsize=10, color='black')
    fig.text(0.18, 0.85, str(box[2]), va='center', rotation='horizontal', fontsize=10, color='black')

    fig.text(0.01, 0.80, 'Object status:', va='center', rotation='horizontal', fontsize=10, color='black')
    if is_obj_fit:
        fig.text(0.18, 0.80, 'PASSED', va='center', rotation='horizontal', fontsize=10, color='green')
    else:
        fig.text(0.18, 0.80, 'FAILED', va='center', rotation='horizontal', fontsize=10, color='red')

    # Calculate dynamic ticks for x and y axes
    x_ticks = np.linspace(-pyramid['base_x'] / 2, pyramid['base_x'] / 2, num=5)
    y_ticks = np.linspace(-pyramid['base_y'] / 2, pyramid['base_y'] / 2, num=5)
    x_labels = np.linspace(0, pyramid['base_x'], num=5, dtype=int)
    y_labels = np.linspace(0, pyramid['base_y'], num=5, dtype=int)

    # Set the limits, ticks, and labels
    ax.set_xlim([-pyramid['base_x']/2, pyramid['base_x']/2])
    ax.set_ylim([-pyramid['base_y']/2, pyramid['base_y']/2])
    ax.set_zlim([0, max(pyramid['area_height'], box[2])])
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)
    ax.set_xlabel('X (cm)')
    ax.set_ylabel('Y (cm)')
    ax.set_zlabel('Z (cm)')

    plt.show()


# Plot the pyramid and the box
#plot_pyramid_and_box('beevision182', box, scale)
#plot_pyramid_and_box('beevision182s', box, scale)
