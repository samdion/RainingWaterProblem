from typing import List


def get_raining_water(height: List[int]):

    leading: int = 0
    leading_max: int = 0

    trailing: int = len(height) - 1
    trailing_max: int = 0

    water_levels: List[int] = [0] * len(height)

    while leading < trailing:
        if height[leading] <= height[trailing]:
            if height[leading] > leading_max:
                leading_max = height[leading]
            else:
                water_levels[leading] = abs(leading_max - height[leading])

            leading += 1
        else:
            if height[trailing] > trailing_max:
                trailing_max = height[trailing]
            else:
                water_levels[trailing] = abs(leading_max - height[leading])

            trailing -= 1

    return water_levels


if __name__ == '__main__':
    print(get_raining_water([3, 5, 3, 1, 8, 6, 4, 7, 3, 4, 5, 3, 2]))
    print(get_raining_water([0, 1, 2, 3, 2, 1, 0, 4]))
    print(get_raining_water([0, 8, 4, 4, 8]))
