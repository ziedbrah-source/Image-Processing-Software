# this file manipulates:
# egalisation
# contrast
from basic import *


# histogram egalisation
def egalisation(arr, maxGreyLevel, cumulativeHist, height, width):
    # cumulative probabilities
    cumulProb = cumulativeHist/cumulativeHist[maxGreyLevel]
  #  print(cumulProb)
    transform = cumulProb*maxGreyLevel
    transform = transform.astype(int)
    resultArr = np.zeros((height, width), dtype=int)

    for i in range(height):
        for j in range(width):
            resultArr[i][j] = transform[arr[i][j]]
    return resultArr

# editing the contrast, this function takes a 2D array


def linearContrastTransform(arr, height, width, x1, y1, x2, y2, maxGreyLevel):
    resultArr = np.zeros((height, width), dtype=int)
    # look up table
    lut = np.zeros((maxGreyLevel+1), dtype=int)

    # our function is a linear function ax+b:
    a = (y2-y1)/(x2-x1)
    b = (y1+y2-a*(x1+x2))/2
    for i in range (maxGreyLevel+1):
        lut[i]=int(a*i+b)
        if lut[i] < 0:
            lut[i]=0
        elif lut[i]>maxGreyLevel:
            lut[i]=maxGreyLevel
    print(lut)
    for i in range(height):
        for j in range(width):
            resultArr[i][j] =lut[arr[i][j]]
    plt.clf()
    image = plt.imshow(Image.fromarray(resultArr))
    plt.show()  # do not forget to add block = false
    return resultArr

#resultArr = egalisation(arr, maxGreyLevel, cumulativeHist, height, width)

#linearContrastTransform(arr, height, width, 50, 0, 255, 255, maxGreyLevel)


def openImage(arr):
    plt.clf()
    image = plt.imshow(Image.fromarray(arr))
    plt.show(block=False)



