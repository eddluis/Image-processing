
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
