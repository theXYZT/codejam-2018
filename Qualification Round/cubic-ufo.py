# Codejam 2018, Qualification Round: Cubic UFO

from math import sqrt, cos, sin, atan2

def get_angle_from_area(area):
    """Using the cube shadow theorem."""
    return 2 * atan2(sqrt(2) - sqrt(3 - area**2), area + 1)

def rotate(x, y, z, theta):
    """Rotate vector (x, y, z) by angle theta along the x-axis."""
    new_y = y * cos(theta) - z * sin(theta)
    new_z = z * cos(theta) + y * sin(theta)
    return [x, new_y, new_z]

def get_face_centers(area):
    """Get face centers for cube corresponding to given area."""
    theta = get_angle_from_area(area)

    face_A = rotate( sqrt(1/8), 0, sqrt(1/8), theta)
    face_B = rotate(-sqrt(1/8), 0, sqrt(1/8), theta)
    face_C = rotate(0, 1/2, 0, theta)

    return [face_A, face_B, face_C]

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    area = float(input())
    centers = get_face_centers(area)
    print('Case #{}:'.format(case))
    for center in centers:
        print('{} {} {}'.format(*center))
