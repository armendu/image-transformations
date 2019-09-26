#!/usr/bin/env python3
"""
Module Docstring
"""
from src.add_sub_img import AddAndSubImage
from src.gen_histogram_img import GenerateHistogram
from src.low_res_img import LowResImage
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
    thresholdedImage = np.zeros((x, y))

    # Pixels above the threshold are replaced by 0
    for i in range(0, x):
        for j in range(0, y):
            if image[i, j] > threshold:
                thresholdedImage[i, j] = 0
            else:
                thresholdedImage[i, j] = image[i, j]

    return thresholdedImage


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

    # Generate and show Low Resolution image
    logger.info("Loading the low resolution image")
    low_res = LowResImage(img)
    low_res.create_and_show_img()

# ================= Segment the face of Lena ===================
#     while True:
#         threshold = input("Type the threshold(0 to 255)<type exit to break>: ")  # Get the threshold from the client
# 
#         # If client doesn't want to exit apply the threshold to the image
#         if "exit" not in threshold:
#             thresholded_image = applyThreshold(low_resolution_image, int(threshold))  # Applying the threshold
# 
#             # Show the calculated results
#             fig, (axe1, axe2) = plt.subplots(1, 2)
#             fig.suptitle(f"Thresholded image by {int(threshold)}")
#             axe1.imshow(low_resolution_image, cmap='gray')
#             axe2.imshow(thresholded_image, cmap='gray')
#             plt.show(block=True)
#         else:
#             break


if __name__ == "__main__":
    # Start the main function
    main()
