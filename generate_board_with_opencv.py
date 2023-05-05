#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import argparse
from math import ceil

import cv2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pattern-size',
                        type=int,
                        nargs=2,
                        help='Size of the calibration pattern (width, height) in terms of squares',
                        required=True)
    args = parser.parse_args()

    # Create a Charuco board definition.
    PW = args.pattern_size[0]  # width of calibration pattern
    PH = args.pattern_size[1]  # height of calibration pattern
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_1000)
    square_length = 25  # mm
    marker_length = 15  # mm
    board = cv2.aruco.CharucoBoard((PW, PH), square_length, marker_length, dictionary)

    pixels_per_cm = 100
    pixels_per_square = int(ceil(square_length / 10.0 * pixels_per_cm))
    img_board = board.generateImage((PW * pixels_per_square, PH * pixels_per_square), marginSize=0, borderBits=1)

    file = "board_generated_by_opencv.png"
    cv2.imwrite(file, img_board)
    print("Board was saved to %s." % file)


if __name__ == '__main__':
    main()
