#!/c/Python25 python
#import sys, os, numpy #sys, os, PIL, numpy, Image, ImageEnhance
import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math
#from rpy2 import robjects
from datetime import tzinfo, timedelta, datetime

def choose_dispersaldirection():
    direction_MIN=random.uniform(-1,0.75)
    direction_MAX=direction_MIN+0.5
    return [direction_MIN,direction_MAX]
