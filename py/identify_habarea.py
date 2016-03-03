
def identify_habarea(indiv_xy_position, habarea_map, userbase = False):
    """
    This function identifies the habitat area of a patch in which an individual is.
    If userbase = False (simulation on the DataBase maps), the area is in number of pixels;
    if userbase = True (simulation on the user (real) maps), the area is in number of hectares.
    Input:
    - indiv_xy_position: cell that corresponde to [x,y](row,col) positions of an individual
    - habarea_map: matrix/map of Area of each patch 
      (if userbase = False, AREAPix in pixels; if userbase = True, AreaHA in hectares)
    - userbase: False = simulated database maps are used
                True = user (real) maps are used
    Output:
    - patchid: Area of the fragment
      (if userbase = False, in pixels; if userbase = True, in hectares)
    """  
    
    row=int(indiv_xy_position[0])
    col=int(indiv_xy_position[1])
    habarea=habarea_map[row][col]
    return habarea
