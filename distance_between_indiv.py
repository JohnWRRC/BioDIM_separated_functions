import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math
#from rpy2 import robjects
from datetime import tzinfo, timedelta, datetime

def distance_between_indiv(xy_ind_a,xy_ind_b,spatialresolution):
    a_x=xy_ind_a[0]
    a_y=xy_ind_a[1]
    b_x=xy_ind_b[0]
    b_y=xy_ind_b[1]
    
    distPix=math.sqrt((a_x-b_x)*(a_x-b_x)+(a_y-b_y)*(a_y-b_y))
    distMeters=float(distPix)*float(spatialresolution)
    return distMeters