# --------------------------------Imports------------------------------------#
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import random
import math

def Unipolar(image) :
    x = image.shape[0]
    y = image.shape[1]

    for i in range(x):
        for j in range(y):
            if random.random() <= 0.15 :
                image[i,j]= 0

    # ----------- Image Display ----------------- #
    img = Image.fromarray(image)
    img.show()


def Bipolar(image) :
    x = image.shape[0]
    y = image.shape[1]

    for i in range(x):
        for j in range(y):
            if random.random() <= 0.10 :
                image[i,j]= random.randrange(0,255,255) #Stops at 255 and stepsize=254 to get only 0 or 255

    # ----------- Image Display ----------------- #
    img = Image.fromarray(image)
    img.show()

#----------------------------Histogram-----------------------------------------#
def Histogram(Original,Filtered):
    plt.figure(figsize=(8, 10))
    ax = plt.subplot(311)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xticks(range(0, 256, 30),fontsize=10)
    plt.yticks( fontsize=10)
    plt.xlabel("Intensity", fontsize=10)
    plt.ylabel("Count", fontsize=10)
    ax.set_title('Original Image', fontsize=12)
    plt.hist(Original.ravel(),color="#3F5D7D", bins=100)
    ax = plt.subplot(312)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xticks(range(0, 256, 30),fontsize=10)
    plt.yticks( fontsize=10)
    plt.xlabel("Intensity", fontsize=10)
    plt.ylabel("Count", fontsize=10)
    ax.set_title('Filtered Image', fontsize=12)
    plt.hist(Filtered.ravel(),color="#3F5D7D", bins=100)
    ax = plt.subplot(313)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xticks(range(0, 256, 30),fontsize=10)
    plt.yticks( fontsize=10)
    plt.xlabel("Intensity", fontsize=10)
    plt.ylabel("Count", fontsize=10)
    ax.set_title('Noise', fontsize=12)
    plt.hist((Original-Filtered).ravel(),color="#3F5D7D", bins=100)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    img_o1 = np.array(Image.open("images/image_01.png"))
    img_o2 = np.array(Image.open("images/image_02.png"))

    #----------------- Unipolar 15% of the time is 0 -------------------#
    Unipolar(img_o1)
    #Histogram(img_o1,img_r)
    input("Press Enter to continue...")
    #------------- Bipolar 10% of the time is 255 or 0 -----------------#
    Bipolar(img_o2)
    #Histogram(img_o2,img_r)