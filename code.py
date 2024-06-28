import numpy as np

box1 = (50, 30, 36)  # x, y, height

pyramid_182 = {
    'top_x': 35,
    'base_x': 100,
    'top_y': 25,
    'base_y': 80,
    'min_size': 5,
    'area_height': 105
}  # is measurement area height include min_size??


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
    if min(xy_box) < src_pyramid['min_size']:
        return False

    xy_angles = get_pyramid_angles(src_pyramid)
    xy_swap = int(xy_box[1] > xy_box[0])  # 0: BoxX <=> PyrX, 1: BoxY <=> PyrX

    # check min_flat box
    if xy_box[2] <= src_pyramid['min_size']:
        if xy_box[xy_swap] >= src_pyramid['base_x'] or xy_box[1 - xy_swap] >= src_pyramid['base_y']:
            return False

    # check height against pyramid wall
    new_base_x = src_pyramid['base_x'] / 2 - xy_box[xy_swap] / 2
    new_base_y = src_pyramid['base_y'] / 2 - xy_box[1 - xy_swap] / 2

    tan_x = np.tan(xy_angles[xy_swap])
    tan_y = np.tan(xy_angles[1 - xy_swap])

    if tan_x != 0 and tan_y != 0:
        new_opp_x = new_base_x * tan_x
        new_opp_y = new_base_y * tan_y

        if new_opp_x <= (xy_box[2] - src_pyramid['min_size']) or new_opp_y <= (xy_box[2] - src_pyramid['min_size']):
            return False
    else:
        # Handle the case where tan is zero (vertical wall)
        if new_base_x <= 0 or new_base_y <= 0:
            return False

    return True

# print("Test Box = " + str(test_box(pyramid_182, box1)))
