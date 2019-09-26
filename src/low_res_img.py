from src.common_trans_img import CommonTransformations

import numpy as np
import matplotlib.pyplot as plt


class LowResImage(CommonTransformations):
    def __init__(self, image):
        self.image = image

    def create_and_show_img(self):
        # ============= Tear image into 16x16 blocks and compute histogram =====
        block_size = 16  # blocks to tear the image
        teared_up_image = super(LowResImage, self).break_image(self.image,
                                                               block_size)  # Tear image into block_size x block_size non overlapping blocks
        # For each of the blocks, compute mean value
        low_resolution_image = low_resolution(teared_up_image)

        fig, (axe1, axe2) = plt.subplots(1, 2)
        fig.suptitle("Low resolution image")
        axe1.imshow(self.image, cmap='gray')
        axe2.imshow(low_resolution_image, cmap='gray')
        plt.show(block=True)


def low_resolution(image):
    x, y = image.shape
    low_resolution_image = np.zeros((x, y))

    for i in range(0, x):
        for j in range(0, y):
            low_resolution_image[i, j] = int(
                255 * image[i, j].mean())  # Since image has 0 to 1 values we need to do the multiplication

    return low_resolution_image
