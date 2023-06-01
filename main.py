import utils
from utils import *
import numpy as np


def warpPerspective(img, transform_matrix, output_width, output_height):
    """
    TODO : find warp perspective of image_matrix and return it
    :return a (width x height) warped image
    """

    warpedImage = np.zeros((output_width, output_height, 3))
    for x in range(0, len(img)):
        for y in range(0, len(img[x])):
            [a, b, c] = np.dot(np.array(transform_matrix), np.array([x, y, 1]))
            a = a / c
            b = b / c
            if 0 <= a < output_width and 0 <= b < output_height:
                warpedImage[int(a)][int(b)] = img[x][y]

    return warpedImage


def grayScaledFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    transform_matrix = [[0.299, 0.587, 0.114]]

    return utils.Filter(img, np.array(transform_matrix))


def crazyFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    transform_matrix = [[0,0,1],
                        [0,0.5,0],
                        [0.5,0.5,0]]

    crazyImage =  utils.Filter(img,np.array(transform_matrix))

    crazyImageInverse = utils.Filter(crazyImage , np.array(np.linalg.inv(transform_matrix)))

    return crazyImage , crazyImageInverse



def scaleImg(img, scale_width, scale_height):
    """
    TODO : Complete this part based on the description in the manual!
    """

    scaledImage = np.zeros((scale_width * len(img), scale_height * len(img[0]), 3))
    for x in range(0, len(scaledImage)):
        for y in range(0, len(scaledImage[x])):
            scaledImage[x][y] = img[int(x / scale_width)][int(y / scale_height)]

    return scaledImage

def permuteFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    transform_matrix = [[0, 0, 1],
                        [0, 1, 0],
                        [1, 0, 0]]

    return utils.Filter(img, np.array(transform_matrix))

if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    showImage(image_matrix, title="Input Image")

    # TODO : Find coordinates of four corners of your inner Image ( X,Y format)
    #  Order of coordinates: Upper Left, Upper Right, Down Left, Down Right
    pts1 = np.float32([[238, 11], [596, 180], [248, 987], [626, 908]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    m = getPerspectiveTransform(pts1, pts2)

    warpedImage = warpPerspective(image_matrix, m, width, height)
    showWarpPerspective(warpedImage)

    grayScalePic = grayScaledFilter(warpedImage)
    showImage(grayScalePic, title="Gray Scaled")

    crazyImage, invertedCrazyImage = crazyFilter(warpedImage)
    showImage(crazyImage, title="Crazy Filter")
    showImage(invertedCrazyImage, title="Inverted Crazy Filter")

    scaledImage = scaleImg(warpedImage, 3, 4)
    showImage(scaledImage, title="Scaled Image")

    permuteImage = permuteFilter(warpedImage)
    showImage(permuteImage, title="Permuted Image")
