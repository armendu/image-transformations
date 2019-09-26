import numpy as np
import matplotlib.pyplot as plt


class MirrorImage:
    def __init__(self, image):
        self.image = image

    def create_and_show_img(self):
        # Flips image from left to right
        img_mirror = np.fliplr(self.image)

        fig, (axe1, axe2) = plt.subplots(1, 2)
        fig.suptitle("Flipped image left to right")
        axe1.imshow(self.image, cmap="gray")
        axe2.imshow(img_mirror, cmap="gray")
        plt.show()
