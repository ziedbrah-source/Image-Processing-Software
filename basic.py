# This file contains basic operations on PGM files
# read, write, generating histogram, cumulative histogram
# Calculating the mean and the standard deviation
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
import tkinter as tk
import PIL.ImageTk
from collections import Counter
import uuid


# this function takes a pgm file and return a 2 dimensions numpy array
def readPGM(name):
    pgmf = open(name, 'rb')
    lines = pgmf.readlines()
    i = 1
    while True:
        if lines[i].decode()[0] == "#":
            del lines[i]
        else:
            break
    (width, height) = [int(i) for i in lines[1].split()]
    (maxGreyLevel) = [int(i)
                      for i in lines[2] .split()]  # idk why it returns an array
    i = 0
    for line in lines[3:]:
        line = line.decode()
        row = []
        numbers = [int(i) for i in line.split()]
        if i == 0:
            arr = np.copy(numbers)
        else:
            arr = np.append(arr, np.array(numbers))
        i += 1

    arr.resize((height, width))
    return (height, width, maxGreyLevel[0], arr)

# write a pgm file from a 2d numpy array


def writePGM(arr, width, height, maxGreyLevel):
    filename = "./images/"+str(uuid.uuid4())+".pgm"
    pgmf = open(filename, 'w')
    pgmf.write("P2\n")
    pgmf.write(str(width)+" ")
    pgmf.write(str(height)+"\n")
    pgmf.write(str(maxGreyLevel)+"\n")
    for line in arr:
        ch = np.array2string(line)
        ch = ch[1:len(ch)-1]
        pgmf.write(ch)
        pgmf.write("\n")


# return the mean (moyenne) and the standard deviation (écart type)
def meanSTD(arr):
    return (arr.mean(), np.std(arr))

# return a dictionary representing the histogram


def histogram(arr, maxGreyLevel):
    hist = Counter(arr.flatten())
    cumulativeHist = np.zeros(255+1, dtype=int)
    # print(hist)
    # print(sorted(hist.items()))
    for k in hist:
        cumulativeHist[k] = hist[k]
    i = 1
    while i < maxGreyLevel+1:
        cumulativeHist[i] += cumulativeHist[i-1]
        i += 1
    return (hist, cumulativeHist)


def plotHistogram(hist):
    plt.clf()
    plt.bar(hist.keys(), hist.values())
    plt.show(block=False)


def plotCumulativeHist(cumulativeHist, maxGreyLevel):
    plt.clf()
    plt.bar(np.arange(maxGreyLevel+1), cumulativeHist)
    plt.show(block=False)


def plotImage(arr):
    plt.clf()
    plt.imshow(Image.fromarray(arr))
    plt.show(block=False)
