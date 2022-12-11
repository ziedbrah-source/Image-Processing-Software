from seuillage import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


imagePath = "images/3.pgm"
arr = None
(height, width, maxGreyLevel, arr) = readPGM(imagePath)
# print(arr)


(hist, cumulativeHist) = histogram(arr, maxGreyLevel)
(mean, std) = meanSTD(arr)
mean = format(mean, '.2f')
std = format(std, '.2f')
meanSTR = str(mean)
stdSTR = str(std)


def updateImageInfos():
    strings = imagePath.split('/')
    imageName = strings[len(strings)-1]
    btn_path.configure(text=imageName)
    heightBtn.configure(text=str(height))
    widthBtn.configure(text=str(width))
    maxGrayBtn.configure(text=str(maxGreyLevel))
    global mean
    global std
    global meanSTR
    global stdSTR
    global hist
    global cumulativeHist
    (hist, cumulativeHist) = histogram(arr, maxGreyLevel)

    (mean, std) = meanSTD(arr)

    mean = format(mean, '.2f')
    std = format(std, '.2f')
    meanSTR = str(mean)
    stdSTR = str(std)
    meanValue.configure(text=meanSTR)
    stdValue.configure(text=stdSTR)


def updateImg(newPath):
    global imagePath
    imagePath = newPath
    global width
    global height
    global maxGreyLevel
    global arr
    (height, width, maxGreyLevel, arr) = readPGM(imagePath)
    updateImageInfos()
    plotImage(arr)


def equalize():
    # global arr
    # global maxGr
    global arr
    arr = egalisation(arr, maxGreyLevel, cumulativeHist, height, width)
    plotImage(arr)
    updateImageInfos()


def linearContrast():
    x1 = int(xA.get(1.0, "end-1c"))
    y1 = int(yA.get(1.0, "end-1c"))
    x2 = int(xB.get(1.0, "end-1c"))
    y2 = int(yB.get(1.0, "end-1c"))
    print((x1, y1), (x2, y2))
    global arr
    arr = linearContrastTransform(
        arr, height, width, x1, y1, x2, y2, maxGreyLevel)
    updateImageInfos()


def addNoiseAndShow():
    global arr
    arr = addingNoise(arr, height, width)
    plotImage(arr)
    updateImageInfos()


def applyAverageFilter():
    n = int(filterSizeValue.get(1.0, "end-1c"))
    print("n= ", n)
    global arr
    arr = averageFilter(arr, height, width, n)
    plotImage(arr)
    updateImageInfos()


def applyMedianFilter():

    n = int(filterSizeValue.get(1.0, "end-1c"))
    print("n= ", n)

    global arr
    arr = medianFilter(arr, height, width, n)
    plotImage(arr)

    updateImageInfos()


def applyHighPassFilter():
    global arr
    arr = highPassFilter(arr, height, width)
    plotImage(arr)
    updateImageInfos()


def applyOTSU():
    global arr
    arr = otsu(width, height, maxGreyLevel, arr)
    plotImage(arr)
    updateImageInfos()


def doErosionAndShow():
    global arr
    arr = doErosion(arr, height, width)
    plotImage(arr)
    updateImageInfos()


def doDilatationAndShow():
    global arr
    arr = doDilatation(arr, height, width)
    plotImage(arr)
    updateImageInfos()


def invertColorsAfterOTSU():
    global arr
    print(arr)
    #arr = ~arr
    for i in range(height):
        for j in range(width):
            if arr[i][j] == 255:
                arr[i][j] = 0
            else:
                arr[i][j] = 255
    plotImage(arr)
    updateImageInfos()


def printHist():
    print(hist)


def test():
    pass


def openImage():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Java Files", "*.pgm"), ("PGM Files", "*.*")]
    )
    if not filepath:
        return
    updateImg(filepath)


plotImage(arr)
window = tk.Tk()

window.geometry("900x900+0+0")

window.title("Image processing software")
window.configure(bg="#3498db")
window.rowconfigure(0, minsize=200, weight=1)
window.columnconfigure(1, minsize=100, weight=1)

# --------------Image infos ---------------------------

imageInfos = tk.Frame(window, relief=tk.RAISED, bd=2)

firstSection1 = tk.Label(
    imageInfos, text="Image infos:", font=("Arial", 18))
pathLabel = tk.Label(imageInfos, text="Path:", font=("Arial", 12))
btn_path = tk.Button(imageInfos, text=imagePath, width=20,
                     font=("Arial", 12), relief=tk.SUNKEN, command=test)
heightLabel = tk.Label(imageInfos, text="Height:", font=("Arial", 12))
heightBtn = tk.Button(imageInfos, text=str(height), relief=tk.SUNKEN,  width=20,
                      font=("Arial", 12), command=test)
widthLabel = tk.Label(imageInfos, text="Width", font=("Arial", 12))
widthBtn = tk.Button(imageInfos, text=str(width), relief=tk.SUNKEN, width=20,
                     font=("Arial", 12), command=test)
maxGrayLabel = tk.Label(imageInfos, text="Max gray level:", font=("Arial", 12))
maxGrayBtn = tk.Button(imageInfos, text="255", relief=tk.SUNKEN, width=20,
                       font=("Arial", 12), command=test)

firstSection1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
pathLabel.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_path.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
heightLabel.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
heightBtn.grid(row=1, column=3, sticky="ew", padx=5, pady=5)
maxGrayLabel.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
maxGrayBtn.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
widthLabel.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
widthBtn.grid(row=2, column=3, sticky="ew", padx=5, pady=5)


# -------------------------------------------------------------
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
secondSection = tk.Label(
    fr_buttons, text="Basic Operations:", font=("Arial", 18))
btn_original = tk.Button(fr_buttons, text="Original image", width=18,
                         font=("Arial", 12), command=lambda: updateImg(imagePath))
btn_Img = tk.Button(fr_buttons, text="Show current image", width=18,
                    font=("Arial", 12), command=lambda: plotImage(arr))
btn_openPGM = tk.Button(fr_buttons, text="Open new image", width=18,
                        font=("Arial", 12), command=openImage)
btn_savePGM = tk.Button(fr_buttons, text="Save current PGM", width=18,
                        font=("Arial", 12), command=lambda: writePGM(arr, width, height, maxGreyLevel))
mean = tk.Label(fr_buttons, text="Mean:", font=("Arial", 12))
meanValue = tk.Button(fr_buttons, text=meanSTR,
                      font=("Arial", 12), width=18, relief=tk.SUNKEN, command=test)
std = tk.Label(fr_buttons, text="Standard deviation:", font=("Arial", 12))
stdValue = tk.Button(fr_buttons, text=stdSTR,
                     font=("Arial", 12), width=18, relief=tk.SUNKEN, command=test)
histoButton = tk.Button(fr_buttons, text="Histogram",
                        font=("Arial", 12), width=18,  command=lambda: plotHistogram(hist))
cumulHistogButton = tk.Button(fr_buttons, text="Cumulative Histogram",
                              font=("Arial", 12), width=18,  command=lambda: plotCumulativeHist(cumulativeHist, 255))
secondSection.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_original.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_Img.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
btn_openPGM.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
btn_savePGM.grid(row=1, column=3, sticky="ew", padx=5, pady=5)
mean.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
meanValue.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
std.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
histoButton.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
cumulHistogButton.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

stdValue.grid(row=2, column=3, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
# btn_compile.grid(row=2, column=0, sticky="ew", padx=5)

# ------------Manipulating contrast--------------------------------------

# -------------------------------------------------------------
manipConstrast = tk.Frame(window, relief=tk.RAISED, bd=2, pady=10)
thirdSection = tk.Label(
    manipConstrast, text="Manipulating contrast", font=("Arial", 18))
invertButton = tk.Button(manipConstrast, text="Invert Colors after OTSU :)",
                         font=("Arial", 12), width=20, command=invertColorsAfterOTSU)
equalizationLabel = tk.Label(
    manipConstrast, text="Histogram equalization", font=("Arial", 12))
equalizationBtn = tk.Button(manipConstrast, text="Equalize",
                            font=("Arial", 12), width=20, command=equalize)
linearTransformLabel = tk.Label(
    manipConstrast, text="Linear contrast transformation", font=("Arial", 12))
labelA = tk.Label(manipConstrast, text="A(x,y)", font=("Arial", 12))
xA = tk.Text(manipConstrast, height=1, width=1)
yA = tk.Text(manipConstrast, height=1, width=20)
labelB = tk.Label(manipConstrast, text="B(x,y)", font=("Arial", 12))
xB = tk.Text(manipConstrast, height=1, width=1)
yB = tk.Text(manipConstrast, height=1, width=20)
contrastButton = tk.Button(manipConstrast, text="Apply linear contrast",
                           font=("Arial", 12), width=20, command=linearContrast)

thirdSection.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
invertButton.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
equalizationLabel.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
equalizationBtn.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
linearTransformLabel.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
contrastButton.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
labelA.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
xA.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
yA.grid(row=4, column=2, sticky="ew", padx=5, pady=5)
labelB.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
xB.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
yB.grid(row=5, column=2, sticky="ew", padx=5, pady=5)

# ---------------------filters------------------------------------
manipFilters = tk.Frame(window, relief=tk.RAISED, bd=2, pady=10)
thirdSection = tk.Label(
    manipFilters, text="Filters", font=("Arial", 18))

noiseBtn = tk.Button(manipFilters, text="Pepper and salt noise",
                     font=("Arial", 12), width=20, command=addNoiseAndShow)

filterSizeLabel = tk.Label(
    manipFilters, text="Filter size", font=("Arial", 12))
filterSizeValue = tk.Text(manipFilters, height=1, width=5)
averageFilterBtn = tk.Button(manipFilters, text="Average filter",
                             font=("Arial", 12), width=20, command=applyAverageFilter)
medianFilterBtn = tk.Button(manipFilters, text="Median filter",
                            font=("Arial", 12), width=20, command=applyMedianFilter)
highPassFilterBtn = tk.Button(manipFilters, text="High boost",
                              font=("Arial", 12), width=20, command=applyHighPassFilter)


thirdSection.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
noiseBtn.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
filterSizeLabel.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
filterSizeValue.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
averageFilterBtn.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
medianFilterBtn.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
highPassFilterBtn.grid(row=2, column=2, sticky="ew", padx=5, pady=5)

# -------------------Seuillage-------------------------------
manipSeuillage = tk.Frame(window, relief=tk.RAISED, bd=3, pady=10)
fourthSection = tk.Label(
    manipSeuillage, text="Segmentation Part", font=("Arial", 18))

OTSUBtn = tk.Button(manipSeuillage, text="Apply OTSU Algorithm",
                    font=("Arial", 12), width=20, command=applyOTSU)
fourthSection.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
OTSUBtn.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
# Erosion,
# Dilatation,
# Ouverture,
# Fermeture
ErosionBtn = tk.Button(manipSeuillage, text="Apply Erosion Algorithm",
                       font=("Arial", 12), width=20, command=doErosionAndShow)
ErosionBtn.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
DilatationBtn = tk.Button(manipSeuillage, text="Apply Dilatation Algorithm",
                          font=("Arial", 12), width=20, command=doDilatationAndShow)
DilatationBtn.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

imageInfos.grid(row=0, column=0, sticky="ew", padx=10)
fr_buttons.grid(row=1, column=0, sticky="ew", padx=10)
manipConstrast.grid(row=2, column=0, sticky="ew", padx=10)
manipFilters.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
manipSeuillage.grid(row=0, column=1, sticky="ew", padx=10)

window.update()
window.mainloop()
