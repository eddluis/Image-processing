# --------------------------------Imports------------------------------------#
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
# ----------------------------------------------------------------------------#

#------------------------------Filtro de mediana 3x3 ---------------------------#
def median3by3(image):
    nine_neighbors = []
    mediana = 0

    x = image.shape[0]
    y = image.shape[1]

    filtered_image = np.zeros((x,y))

    for i in range(x):
        for j in range(y):
            if i>1 and j+1<y :
                try:
                    nine_neighbors.append( image[i-1][j-1] )
                    nine_neighbors.append( image[i-1][j] )
                    nine_neighbors.append( image[i-1][j+1] )

                    nine_neighbors.append( image[i][j-1] )
                    nine_neighbors.append( image[i][j] )
                    nine_neighbors.append( image[i][j+1] )

                    nine_neighbors.append( image[i+1][j-1] )
                    nine_neighbors.append( image[i+1][j] )
                    nine_neighbors.append( image[i+1][j+1] )

                except:
                    print("boundary violation") #in case the indexes are outside the picture
                finally:
                     nine_neighbors.sort()
                     mediana = nine_neighbors[4]
                     filtered_image[i][j] = mediana
                     nine_neighbors.clear()

    return filtered_image

#----------------------------Histogram-----------------------------------------#
def Histogram(Original,Altered):
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
    ax.set_title('Altered Image', fontsize=12)
    plt.hist(Altered.ravel(),color="#3F5D7D", bins=100)
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
    plt.hist((Altered-Original).ravel(),color="#3F5D7D", bins=100)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    img_o = np.array(Image.open("images/image_04.png"))

    x = img_o.shape[0]
    y = img_o.shape[1]
    img_r=np.zeros((x, y))

    #First pass
    img_r = median3by3(img_o)
    #Second pass
    img_r2 = median3by3(img_r)

    # --------------------------Image Display------------------------------------#
    img_as_array_second_pass = Image.fromarray(img_r2)
    img_as_array_second_pass.show()
    # ---------------------------Histogram-------------------------------------#
    input("Press Enter to continue...")
    Histogram(img_o, img_r2)