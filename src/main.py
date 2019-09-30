#!/usr/bin/env python3
"""
Module Docstring
"""
from src.add_sub_img import AddAndSubImage
from src.gen_histogram_img import GenerateHistogram
from src.mirror_img import MirrorImage
from src.negative_img import NegativeImage

__author__ = "Armend Ukehaxhaj"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger
import numpy as np
import matplotlib.image as mpimg


def applyThreshold(image, threshold):
    x, y = image.shape
    thresholded_image = np.zeros((x, y))

    # Pixels above the threshold are replaced by 0
    for i in range(0, x):
        for j in range(0, y):
            if image[i, j] > threshold:
                thresholded_image[i, j] = 0
            else:
                thresholded_image[i, j] = image[i, j]

    return thresholded_image


def main():
    # Main starting point of the application
    logger.info("Starting Image transformations")

    # Read the image
    logger.info("Loading selected image")
    img = mpimg.imread("../res/lena.png")

    # Generate and show negative image
    logger.info("Processing the negative image")
    neg_img_trans = NegativeImage(img)
    neg_img_trans.create_and_show_img()

    # Generate and show mirrored image
    logger.info("Loading the mirrored image")
    mirrored_img_trans = MirrorImage(img)
    mirrored_img_trans.create_and_show_img()

    # Generate and show added and subtracted image
    logger.info("Loading the added and subtracted image")
    add_sub_trans = AddAndSubImage(img)
    add_sub_trans.create_and_show_img()

    # Generate and show generated histogram of image
    logger.info("Loading the generated histogram")
    gen_histogram = GenerateHistogram(img)
    gen_histogram.create_and_show_img()


if __name__ == "__main__":
    # Start the main function
    main()
