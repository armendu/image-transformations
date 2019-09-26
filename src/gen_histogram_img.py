from src.common_trans_img import CommonTransformations

import numpy as np
import matplotlib.pyplot as plt


class GenerateHistogram(CommonTransformations):
    def __init__(self, image):
        self.image = image

    def create_and_show_img(self):
        # ============= Tear image into 16x16 blocks and compute histogram =====
        block_size = 16  # blocks to tear the image
        teared_up_image = super(GenerateHistogram, self).break_image(self.image,
                                                                     block_size)  # Tear image into block_size x block_size non overlapping blocks
        teared_up_image_with_histograms = np.zeros((block_size, block_size),
                                                   dtype=object)  # Create an empty(with zeros) matrix of size block_size x block_size

        # For every pixel of the teared_up_image_with histograms compute the histogram of the corresponding pixel at teared_up_image
        for i in range(0, block_size):
            for j in range(0, block_size):
                teared_up_image_with_histograms[i, j] = im_hist(teared_up_image[i, j].flatten(), 256)

        fig, ax = plt.subplots(nrows=block_size, ncols=block_size)
        fig.suptitle(f"Tear image into {block_size}x{block_size} blocks and compute histogram")

        i = 0
        for row in ax:
            j = 0
            for col in row:
                col.axis('off')
                col.plot(teared_up_image_with_histograms[i][j])
                j = j + 1
            i = i + 1

        plt.show(block=True)


def im_hist(image, bins):
    histogram = np.zeros(bins)  # Array of size of bins(usually 256)

    for i in image:
        index = int(i * 255)  # Since image has values between 0 and 1, translate to 0 to 255
        histogram[index] += 1  # Count the pixels

    return histogram
