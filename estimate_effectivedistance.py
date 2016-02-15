import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math
#from rpy2 import robjects
from datetime import tzinfo, timedelta, datetime

def estimate_effectivedistance(input_xy_initpos, input_xy, input_xy_quadrant,landscape_matrix):
    effect_dist=[]
    
    for indiv in range(len(input_xy_initpos)):
        row_initpos=input_xy_initpos[indiv][0]
        col_initpos=input_xy_initpos[indiv][1]
        row_adjfact=input_xy_quadrant[indiv][0]
        col_adjfact=input_xy_quadrant[indiv][1]
        row_current=input_xy[indiv][0]
        col_current=input_xy[indiv][1]        
        
        row_finalpos=row_current-row_adjfact*len(landscape_matrix)
        col_finalpos=col_current+col_adjfact*len(landscape_matrix)

        dist=math.sqrt((row_initpos-row_finalpos)*(row_initpos-row_finalpos)+(col_initpos-col_finalpos)*(col_initpos-col_finalpos))

        effect_dist.append(dist)
    return effect_dist