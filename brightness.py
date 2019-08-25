"""
Reducing and increasing brightness on pictures

"""


#--------------------------Image Display------------------------------------#
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

#------------------------------Image-----------------------------------#
def apply_brightness(img, brightness):
    img_o = np.array(Image.open(img))
    x=img_o.shape[0]
    y=img_o.shape[1]
    starting_weights=[]
    weights=[]

    for i in range(256):
        weights.append(0)
        starting_weights.append(0)
    #---------------------Brightness Value Change-------------------------------#
    for i in range(x):
        for j in range(y):
            brightening_value=img_o[i,j]
            new_value=img_o[i,j]+brightness
            if new_value>255:
                brightening_value=255
                new_value=255
            elif new_value<0:
                brightening_value=0
                new_value=0

            starting_weights[brightening_value]+=1
            weights[new_value]+=1
            img_o[i,j]=new_value
    #--------------------------Image Display------------------------------------#
    img = Image.fromarray(img_o)
    img.show()
    #--------------------------Histogram Display--------------------------------#
    plt.figure(1)
    plt.subplot(211)
    plt.bar(range(256), starting_weights)
    plt.xlabel('brightness')
    plt.ylabel('weight')
    plt.title("Before brightness Change")
    plt.subplot(212)
    plt.bar(range(256),weights)
    plt.xlabel('brightness')
    plt.ylabel('weight')
    plt.title("After brightness Change")
    plt.tight_layout()
    plt.show()
    #---------------------------------------------------------------------------#

if __name__ == "__main__":
    #Clarear img 1
    apply_brightness("clarear_1.png",50)
    input("Press Enter to continue...")
    #Clarear img 2
    apply_brightness("clarear_2.png",40)
    input("Press Enter to continue...")
    #Clarear img 3
    apply_brightness("clarear_3.png",60)
    input("Press Enter to continue...")

    #Escurecer img 1
    apply_brightness("escurecer_1.png",-120)
    input("Press Enter to continue...")
    #Escurecer img 2
    apply_brightness("escurecer_2.png",-100)
    input("Press Enter to continue...")
    #Escurecer img 3
    apply_brightness("escurecer_3.png",-80)