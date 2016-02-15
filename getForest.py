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

def getForest(landscape_matrix):
    forest = []
    for row in range(len(landscape_matrix)):
        for col in range(len(landscape_matrix[0])):
            feature = landscape_matrix[row][col]
            if feature == 1: #HQ
                forest.append([row,col])
            if feature == 2: #MQ
                forest.append([row,col])                
    return forest
