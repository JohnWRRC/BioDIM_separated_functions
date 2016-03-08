import math

def distance_between_indiv(xy_ind_a,xy_ind_b,spatialresolution):
    """
    This function returns the euclidean distance among two individuals.
    Input:
    - xy_ind_a: coordinates (x,y) of individual a
    - xy_ind_b: coordinates (x,y) of individual b
    Output:
    - distMeters: straight line distance among the individuals
    """    
    a_x=xy_ind_a[0]
    a_y=xy_ind_a[1]
    b_x=xy_ind_b[0]
    b_y=xy_ind_b[1]
    
    distPix=math.sqrt((a_x-b_x)*(a_x-b_x)+(a_y-b_y)*(a_y-b_y))
    distMeters=float(distPix)*float(spatialresolution)
    return distMeters