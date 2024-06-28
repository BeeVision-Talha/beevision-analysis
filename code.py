import numpy as np

'''
box1 = (32, 25, 105)  # x, y, height
max_limit_beevision182 = (80, 60, 105)
min_limit_beevision182 = (5, 5, 5)

max_limit_beevision182s = (50, 40, 40)
min_limit_beevision182s = (5, 5, 2)

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
'''

def get_pyramid_angles(src_pyramid):
    # X, Y-dimension truncated sub triangles [adjacent, opposite], [adjacent, opposite]
    adj_x = float(src_pyramid['base_x'] / 2 - src_pyramid['top_x'] / 2)
    opp_x = float(src_pyramid['area_height'])
    adj_y = float(src_pyramid['base_y'] / 2 - src_pyramid['top_y'] / 2)
    opp_y = float(src_pyramid['area_height'])

    ang_x = float(np.arctan(opp_x / adj_x))
    ang_y = float(np.arctan(opp_y / adj_y))

    ang_xy = np.array([ang_x, ang_y], dtype=float)
    return ang_xy

def test_box(src_pyramid, xy_box):

    if len(xy_box) < 3:
        raise ValueError("xy_box must have at least 3 elements")

    # return false if any dimensions are less than 5
    if min(xy_box) < src_pyramid['min_height']:
        return False

    xy_angles = get_pyramid_angles(src_pyramid) # X-axis and Y-axis angles
    xy_swap = int(xy_box[1] > xy_box[0])  # 0: BoxX <=> PyrX, 1: BoxY <=> PyrX

    # check min_flat box
    if xy_box[2] <= src_pyramid['min_height']:
        if xy_box[xy_swap] > src_pyramid['max_length'] or xy_box[1 - xy_swap] > src_pyramid['max_width']:
            return False

    # check height against pyramid wall
    new_base_x = src_pyramid['base_x'] / 2 - xy_box[xy_swap] / 2
    new_base_y = src_pyramid['base_y'] / 2 - xy_box[1 - xy_swap] / 2

    tan_x = np.tan(xy_angles[xy_swap])
    tan_y = np.tan(xy_angles[1 - xy_swap])

    if tan_x != 0 and tan_y != 0:
        new_opp_x = new_base_x * tan_x
        new_opp_y = new_base_y * tan_y

        # Rounding operation(for step=0.5)
        new_opp_x = round(new_opp_x*2)/2
        new_opp_y = round(new_opp_y*2)/2
        if new_opp_x < xy_box[2] or new_opp_y < xy_box[2] or src_pyramid['area_height'] < xy_box[2]:
            return False
    else:
        # Handle the case where tan is zero (vertical wall)
        if new_base_x <= 0 or new_base_y <= 0:
            return False
    return True

#print("Test Box = " + str(test_box(pyramid_182, box1)))
