import random
from check_landscaperange import check_landscaperange

def disperse_random_walk(landscape_matrix, indiv_xy, movement_dist_sigma_pixel, indiv_totaldistance,Form1_landscape_matrix):
    '''on landscape_matrix 1=HQ / 2=MQ / 3=LQ'''
    modified_indiv_xy=[]
    for i in range(len(indiv_xy)):
        modified_indiv_xy.append(indiv_xy[i])
   
    for xp in range(len(modified_indiv_xy)):
        modified_indiv_xy[xp][0]+=random.normalvariate(mu=0,sigma=movement_dist_sigma_pixel)   # random xpos
        modified_indiv_xy[xp][1]+=random.normalvariate(mu=0,sigma=movement_dist_sigma_pixel)   # random ypos

    modified_indiv_xy,changed_quadrant=check_landscaperange(modified_indiv_xy,Form1_landscape_matrix)
    
    return modified_indiv_xy, indiv_totaldistance,changed_quadrant