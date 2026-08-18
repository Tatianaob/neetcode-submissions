from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    num1, num2, num3 = triplet
    sumTriplet = num1 + num2 + num3 
    return sumTriplet


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    w, h, d = box_dimensions[0] , box_dimensions[1],  box_dimensions[2]
    volumen = w * h * d
    return volumen
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
