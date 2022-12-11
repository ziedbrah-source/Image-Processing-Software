from filters import *


def otsu(width, height, max_l, image):

    flat_image = image.flatten("C")

    pixel_number = width * height
    mean_weigth = 1.0/pixel_number

    his, bins = np.histogram(flat_image, np.array(range(0, max_l+1)))
    final_thresh = -1
    final_value = -1
    for t in bins[1:-1]:
        Wb = np.sum(his[:t]) * mean_weigth
        Wf = np.sum(his[t:]) * mean_weigth

        mub = np.mean(his[:t])
        muf = np.mean(his[t:])

        value = Wb * Wf * (mub - muf) ** 2

        if value > final_value:
            final_thresh = t
            final_value = value

    print(final_thresh)
    final_image = flat_image.copy()
    final_image[flat_image > final_thresh] = 255
    final_image[flat_image < final_thresh] = 0
    new_image = np.reshape(final_image, (height, width))
    return new_image


def doErosion(arr, height, width):
    erosionArray = np.array([[255, 0, 255], [0, 255, 0], [255, 0, 255]])
    resultArr = resultArr = np.zeros((height, width), dtype=int)
    n = 3
    endLine = height - n//2
    endColumn = width - n//2
    i = n//2
    while i < endLine:
        j = n//2
        while j < endColumn:
            # print((i,j))
            resultArr[i][j] = arr[i][j]
            for l in range(n):
                for k in range(n):
                    if arr[i-n//2+l][j-n//2+k] > erosionArray[l][k]:
                        resultArr[i][j] = 255
            j += 1
        i += 1
    return resultArr


def doDilatation(arr, height, width):
    dilatationArray = np.array([[255, 0, 255], [0, 0, 0], [255, 0, 255]])
    newArr = np.zeros((height, width), dtype=int)
    n = 3
    for i in range(height):
        for j in range(width):
            newArr[i][j] = 255
    print(arr)
    endLine = height - n//2
    endColumn = width - n//2
    i = n//2
    while i < endLine:
        j = n//2
        while j < endColumn:
            if arr[i][j] == 0:
                #print((i, j))
                for l in range(n):
                    for k in range(n):
                        if dilatationArray[l][k] == 0:
                            newArr[i-n//2+l][j-n//2+k] = 0
            j += 1
        i += 1
    print(newArr)
    print(arr)
    return newArr
