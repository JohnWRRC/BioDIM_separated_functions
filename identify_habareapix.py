
def identify_habareapix(indiv_xy_position, habareapix_map):
    """
    COMPLETE!
    This function identifies the habitat area of a patch in which an individual is (is it correct?)
    """ 
    row=int(indiv_xy_position[0])
    col=int(indiv_xy_position[1])
    habareapix=habareapix_map[row][col]
    return habareapix
