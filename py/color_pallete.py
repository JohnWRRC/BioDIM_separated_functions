import random

def color_pallete():
    """
    COMPLETE!
    """    
    pal = [(0,0,0) for i in range(256)]  # all black
    
    random.seed(1)
    for i in range(1,255):
        color_R=random.sample(range(1,255),1)
        color_G=random.sample(range(1,255),1)
        color_B=random.sample(range(1,255),1)
        #pal[i]=((255-i),int(i/2),i)
        pal[i]=(color_R[0],color_G[0],color_B[0])
    
    pal=random.sample(pal, 255)

#    if Form1.background_filename[0]=="random_landscape_habmat.png":
#        pal[1] = (68,194,0)     # HABITAT
#        pal[2] = (255,190,190)  # MATRIZ
#    if Form1.background_filename[0]=="random_landscape_hqmqlq.png":
    if 1==1:
        pal[1] = (68,194,0)     # HABITAT
        pal[2] = (255,235,190)  # MQ/MATRIZ
        pal[3] = (255,190,190)  # MATRIZ

    pal = sum(pal, ())  # flatten it
    random.seed()
    return pal