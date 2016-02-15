import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math
#from rpy2 import robjects
from datetime import tzinfo, timedelta, datetime

def estimate_distedgePix(indiv_xy_position,landscape_habdist):

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