#!/usr/bin/env python3
import math


def get_camera_width():
    return math.pi / 2.0


def get_tree_coords():
    return [
        (100, 0),
        (0, 100),
        (50, -50)
        #(0, -100),
        #(-100, 0),
        #(101, 0)
    ]


def calculate_angle(x, y):
    return math.atan2(y, x)


def main():
    camera_angle = get_camera_width()
    tree_angles = sorted(calculate_angle(*coord)
                         for coord in get_tree_coords())
    max_num_trees = 0
    next_tree_i = 0
    prev_trees = 1
    for tree_i, tree_angle in enumerate(tree_angles):
        num_trees = prev_trees - 1
        while (tree_angle <= tree_angles[next_tree_i] <= tree_angle +
               camera_angle or tree_angle <= tree_angles[next_tree_i] +
               2 *
               math.pi <= tree_angle +
               camera_angle) and num_trees != len(tree_angles):
            num_trees += 1
            next_tree_i = (next_tree_i + 1) % len(tree_angles)
        max_num_trees = max(max_num_trees, num_trees)
        prev_trees = num_trees
    print(max_num_trees)


if __name__ == '__main__':
    main()
