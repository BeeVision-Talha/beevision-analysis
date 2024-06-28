This code is designed to determine if a parcel will fit within the BeeVision models 182 and 182S Parcel Dimensioner devices.

The approach is to calculate a truncated pyramid which models the parcel dimensioners measurement area, and then evaluate if a parcel will fit within that shape in any orientation.

It can be executed as demonstrated below:

#main.py --productType beevision182 --unit cm --objLength 20 --objWidth 20 --objHeight 20

If debug mode is desired, please navigate to main.py and configure the product_type 
and test_cases variables accordingly.