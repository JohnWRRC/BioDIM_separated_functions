import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math
#from rpy2 import robjects
from datetime import tzinfo, timedelta, datetime

def identify_patchid(indiv_xy_position, patchid_map):
    row=int(indiv_xy_position[0])
    col=int(indiv_xy_position[1])
    patchid=patchid_map[row][col]
    return patchid
