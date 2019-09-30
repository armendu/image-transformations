import numpy as np
import matplotlib.pyplot as plt


class NegativeImage:
    def __init__(self, image):
        self.image = image

    def create_and_show_img(self):
        negative_image = self.get_negative_img()
        self.show_negative_img(negative_image)

    def get_negative_img(self):
        # Get the size of the image
        x, y = self.image.shape

        # Create an matrix of the same size filled with zeros
        negative = np.zeros((x, y))

        # For every pixel of the image subtract 255
        for i in range(0, x):
            for j in range(0, y):
                negative[i, j] = 255 - int(255 * self.image[
                    i, j])

        return negative

    def show_negative_img(self, negative_image):
        # Show the images (new and computed)
        fig, (axe1, axe2) = plt.subplots(1, 2)
        fig.suptitle("Negative image")
        axe1.imshow(self.image, cmap="gray")
        axe2.imshow(negative_image, cmap="gray")
        plt.show()
