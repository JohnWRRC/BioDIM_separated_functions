def estimate_distedgePix(indiv_xy_position,landscape_habdist):
    """
    COMPLETE!
    This function takes the information of distance (in pixels) from the current
    location of an individual to the nearest patch edge
    """    

    row=int(indiv_xy_position[0])
    col=int(indiv_xy_position[1])
    #if row<=0:
    #    row=0
    #if row>=511:
    #    row=511
    #if col<=0:
    #    col=0
    #if col>=511:
    #    col=511
        
    distedgePix = landscape_habdist[row][col]
    return distedgePix