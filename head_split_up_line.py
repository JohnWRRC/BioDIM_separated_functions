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

def head_split_up_line(line):
    line = line.split(' ')
    clean_line={}
    clean_line[line[0]]=line[len(line)-1]
    return clean_line