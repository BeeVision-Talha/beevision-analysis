def can_fit_in_beevision_182(length_cm, width_cm, height_cm, debug=False):
    dimensions = [length_cm, width_cm, height_cm]
    max_dimension = max(dimensions)
    max_index = dimensions.index(max_dimension)

    # return false if any dimensions are less than 5
    if min(dimensions) < 5:
        return False

    if dimensions[max_index] >= 5:
        dimensions[max_index] -= 5
    if debug:
        print(f"Adjusted dimensions: {dimensions}")

    top_length = 35
    top_width = 25
    bottom_length = 80
    bottom_width = 100
    pyramid_height = 100

    return can_fit_in_truncated_pyramid(top_length, top_width, bottom_length, bottom_width, pyramid_height, dimensions, debug)


def can_fit_in_truncated_pyramid(top_length, top_width, bottom_length, bottom_width, pyramid_height, dimensions, debug):
    # Function to compute the dimensions at a given height within the pyramid
    def dimensions_at_height(z):
        if z < 0 or z > pyramid_height:
            return None
        interp_length = bottom_length + \
            (top_length - bottom_length) * (z / pyramid_height)
        interp_width = bottom_width + \
            (top_width - bottom_width) * (z / pyramid_height)
        return interp_length, interp_width

    # Check if the height of the box can fit within the truncated pyramid height
    if max(dimensions) > pyramid_height:
        if debug:
            print(
                f"Height exceeds pyramid height: {max(dimensions)} > {pyramid_height}")
        return False

    # Check all orientations of the box
    for orientation in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        length_cm, width_cm, height_cm = dimensions[orientation[0]
                                                    ], dimensions[orientation[1]], dimensions[orientation[2]]
        if debug:
            print(
                f"Checking orientation: length={length_cm}, width={width_cm}, height={height_cm}")

        fits = True
        for z in range(0, pyramid_height - height_cm + 1):
            interp_length, interp_width = dimensions_at_height(z)
            if length_cm <= interp_length and width_cm <= interp_width:
                if debug:
                    print(
                        f"Fits at height {z}: {length_cm} <= {interp_length}, {width_cm} <= {interp_width}")
            else:
                if debug:
                    print(
                        f"Does not fit at height {z}: {length_cm} > {interp_length} or {width_cm} > {interp_width}")
                fits = False
                break

        if fits:
            return True

    return False


def run_test(function, args, expected, debug=False):
    try:
        result = function(*args, debug)
        assert result == expected
        print(f"{function.__name__}{args} passed")
    except AssertionError:
        print(f"{function.__name__}{args} failed")


test_cases = [
    (can_fit_in_beevision_182, (25, 35, 105), True),
    (can_fit_in_beevision_182, (89, 67, 49), True),
    (can_fit_in_beevision_182, (25, 35, 105), True),
    (can_fit_in_beevision_182, (25, 105, 35), True),
    (can_fit_in_beevision_182, (5, 5, 5), True),
    (can_fit_in_beevision_182, (25, 35, 107), False),
    (can_fit_in_beevision_182, (90, 70, 50), True),
    (can_fit_in_beevision_182, (27, 105, 35), False),
    (can_fit_in_beevision_182, (5, 4, 5), False),
    (can_fit_in_beevision_182, (104, 24, 34), True),
    (can_fit_in_beevision_182, (104, 26, 36), False)
]

for function, args, expected in test_cases:
    run_test(function, args, expected, debug=False)
