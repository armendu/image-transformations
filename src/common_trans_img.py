import numpy as np


class CommonTransformations:
    def break_image(self, image, blocks=16):
        blocked_image = np.zeros((blocks, blocks), dtype=object)

        x_split_by_percentage = image.shape[0] // blocks  # Get the size of x axis
        y_split_by_percentage = image.shape[1] // blocks  # Get the size of y axis

        # Looping to the image from 0 to maxVal of x axis minus the split value, the counter increases by split value
        for i in range(0, image.shape[0] - x_split_by_percentage + 1, x_split_by_percentage):
            for j in range(0, image.shape[1] - y_split_by_percentage + 1, y_split_by_percentage):
                blocked_image[i // x_split_by_percentage, j // y_split_by_percentage] = image[i: i + blocks,
                                                                                        j: j + blocks]
        return blocked_image
