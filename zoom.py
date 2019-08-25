"""
Zoom in and out imagens using the Nearest neighbour interpolation technique
"""
#--------------------------------Imports------------------------------------#
from PIL import Image
import numpy as np

def nearest_neighbor(img, x_new, y_new):
    img_o = np.array(Image.open(img))

    #-------------------------------Array Resize--------------------------------#
    x_old=img_o.shape[0]
    y_old=img_o.shape[1]
    x_scale = x_new/(x_old - 1)
    y_scale = y_new/(y_old - 1)
    img_r=np.zeros((x_new, y_new))

    #------------------------------Nearest Neighbor Alg--------------------------#
    for i in range(x_new):
        for j in range(y_new):
            img_r[i,j] = img_o[(round(i/x_scale)),(round(j/y_scale))]
    #--------------------------Image Display------------------------------------#
    img = Image.fromarray(img_r)
    img.show()
    #---------------------------------------------------------------------------#


if __name__ == "__main__":

    #Primeira imagem zoom-in-1
    nearest_neighbor('zoom_in_1.png',480,360)
    input("Press Enter to continue...")
    #Segunda imagem zoom-in-2
    nearest_neighbor('zoom_in_2.png',1456,2597)
    input("Press Enter to continue...")
    #Terceira imagem zoom-in-3
    nearest_neighbor('zoom_in_3.png',990,720)
    input("Press Enter to continue...")


    #Primeira imagem zoom-out-1
    nearest_neighbor('zoom_out_1.png',120, 271)
    input("Press Enter to continue...")
    #Segunda imagem zoom-out-2
    nearest_neighbor('zoom_out_2.png',500, 314)
    input("Press Enter to continue...")
    #Terceira imagem zoom-out-3
    nearest_neighbor('zoom_out_3.png',500, 174)
