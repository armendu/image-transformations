import numpy as np
import matplotlib.pyplot as plt


class NegativeImage:
    def __init__(self, image):
        self.image = image

    def create_and_show_img(self):
        negative_image = self.get_negative_img()
        self.show_negative_img(negative_image)

    def get_negative_img(self):
        x, y = self.image.shape  # Size of the image
        negative = np.zeros((x, y))  # Create an matrix of the same size filled with zeros

        # For every pixel of the image subtract 255
        for i in range(0, x):
            for j in range(0, y):
                negative[i, j] = 255 - int(255 * self.image[
                    i, j])  # Since image has values between 0 and 1, this multiplication is done to translate to the range between 0 and 255

        return negative

    def show_negative_img(self, negative_image):
        # Show the images (new and computed)
        fig, (axe1, axe2) = plt.subplots(1, 2)
        fig.suptitle("Negative image")
        axe1.imshow(self.image, cmap="gray")
        axe2.imshow(negative_image, cmap="gray")
        plt.show()
