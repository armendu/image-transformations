from random import randint
import numpy as np
import matplotlib.pyplot as plt


class AddAndSubImage:
    def __init__(self, image):
        self.image = image

    def create_and_show_img(self):
        # Generate random number from 0 to 255
        random_value = randint(0, 256)

        # Transform pixels
        img_transformed_pixels = transform_pixels(self.image, random_value)

        # Clip image to have minimum 0 and maximum 255
        clipped_image = clip_img(img_transformed_pixels, 0, 255)

        fig, (axe1, axe2) = plt.subplots(1, 2)
        fig.suptitle(f"Subtraction and Clipping of image by {random_value}")
        axe1.imshow(self.image, cmap="gray")
        axe2.imshow(clipped_image, cmap="gray")
        plt.show()


def transform_pixels(image, value, is_addition=False):
    x, y = image.shape
    transformed_image = np.zeros((x, y))

    # Depending on is_addition parameter add/subtract value from every pixel in the image
    for i in range(0, x):
        for j in range(0, y):
            transformed_image[i, j] = int(255 * image[i, j]) + value if is_addition else int(255 * image[i, j]) - value

    return transformed_image


def clip_img(image, min_value, max_value):
    # Clip every pixel in the image to be between min_value and max_value
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            if image[i, j] < min_value:
                image[i, j] += max_value
            elif image[i, j] > max_value:
                image[i, j] -= max_value

    return image
