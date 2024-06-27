This code is incomplete. Some tests are not passing.

can_fit_in_beevision_182(104, 26, 36) failed
can_fit_in_beevision_182(27, 105, 35) failed

This code attemps to determine if a parcel will fit within the BeeVision model 182 Parcel Dimensioner.
The approach is to calculate a truncated pyramid which models the parcel dimensioners measurement area, and then evaluate if a parcel will fit within that shape in any orientation.
