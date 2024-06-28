def run_test(function, pyramid_dimensions, args, expected, debug=False):
    try:
        result = function(pyramid_dimensions, args)
        assert result == expected
        print(f"{function.__name__}{args} passed")
    except AssertionError:
        print(f"{function.__name__}{args} failed")
    except Exception as e:
        print(f"{function.__name__}{args} raised an exception: {e}")


pyramid_182 = {
    'top_x': 35,
    'base_x': 100,
    'top_y': 25,
    'base_y': 80,
    'min_size': 5,
    'area_height': 100
}  # is measurement area height include min_height??


test_cases = [
    (test_box, (36, 30, 50), True),
    (test_box, (100, 100, 100), False),
    (test_box, (35, 25, 104), True),
    (test_box, (67, 49, 89), True),
    (test_box, (68, 50, 90), True),
    (test_box, (44, 44, 49), True),
    (test_box, (35, 25, 105), True),
    (test_box, (5, 5, 5), True),
    (test_box, (35, 25, 107), False),
    (test_box, (70, 50, 90), True),
    (test_box, (35, 27, 105), False),
    (test_box, (5, 4, 5), False),
    (test_box, (34, 24, 104), True),
    (test_box, (36, 26, 104), False)
]

for function, args, expected in test_cases:
    run_test(function, pyramid_182, args, expected, debug=False)
