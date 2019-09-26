from random import randint
import numpy as np
import matplotlib.pyplot as plt


class AddAndSubImage:
    def __init__(self, image):
        self.image = image

    def create_and_show_img(self):
        random_value = randint(0, 256)  # generate a random value between 0, 256 (doesn't get the higher limit)
        img_transformed_pixels = transform_pixels(self.image,
                                                  random_value)  # by default add, random_value to everypixel in the image
        clipped_image = clip_img(img_transformed_pixels, 0, 255)  # clip image to have minimum 0 and maximum 255

        fig, (axe1, axe2) = plt.subplots(1, 2)
        fig.suptitle(f"Add/Substraction and Clipped image by {random_value}")
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


def clip_img(image, minVal, maxVal):
    # Clip every pixel in the image to be between minVal and maxVal

    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            if image[i, j] < minVal:  # If the current pixel is less than minVal 
                image[i, j] += maxVal  # Add the minVal
            elif image[i, j] > maxVal:  # else if the current pixel is greater than maxVal
                image[i, j] -= maxVal  # Subtract the maxVal

    return image
