import visualizer
import argparse

debug = False

if __name__=="__main__":
    if debug:
        product_type = 'beevision182'
        test_cases = [
            (35, 25, 105),
            (50, 45, 40),
            (80, 60, 2),
            (60, 50, 20),
            (50, 40, 40),
            (5, 5, 2),
            (45, 44, 49),
            (35, 25, 15),
            (5, 5, 5),
            (35, 25, 50),
            (70, 50, 30),
            (35, 27, 25),
            (5, 4, 5),
            (100, 100, 100),
            (35, 25, 104),
            (67, 49, 89),
            (90, 68, 50),
        ]

        for box in test_cases:
            visualizer.plot_pyramid_and_box(product_type.lower(), box)

    else:
        # Parse arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('--productType', type=str, required=True, help='Type of the product')
        parser.add_argument('--unit', type=str, required=True, help='Unit')
        parser.add_argument('--objWidth', type=float, required=True, help='Width of the object')
        parser.add_argument('--objLength', type=float, required=True, help='Length of the object')
        parser.add_argument('--objHeight', type=float, required=True, help='Height of the object')
        args = parser.parse_args()
        print('Product Type: {}'.format(args.productType))
        print('Unit: {}'.format(args.unit))
        print('Object Width: {}'.format(args.objWidth))
        print('Object Length: {}'.format(args.objLength))
        print('Object Height: {}'.format(args.objHeight))

        if args.unit == 'cm':
            m_obj_length_mm = args.objLength * 10
            m_obj_width_mm = args.objWidth * 10
            m_obj_height_mm = args.objHeight * 10
        elif args.unit == 'inch':
            m_obj_length_mm = args.objLength * 25.4
            m_obj_width_mm = args.objWidth * 25.4
            m_obj_height_mm = args.objHeight * 25.4
        elif args.unit == 'mm':
            m_obj_length_mm = args.objLength
            m_obj_width_mm = args.objWidth
            m_obj_height_mm = args.objHeight
        else:
            print('main: Undefined unit selection. Options: "mm", "cm", "inch"')
            exit()

        visualizer.plot_pyramid_and_box(args.productType.lower(),(args.objLength, args.objWidth, args.objHeight))

#main.py --productType beevision182 --unit cm --objLength 20 --objWidth 20 --objHeight 20