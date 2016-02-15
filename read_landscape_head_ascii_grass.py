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

def read_landscape_head_ascii_grass(input_land):
    input_file = open(input_land, 'r')
    line = input_file.readline()
    nlines = 0
    head = {}
    while nlines<5:
        line=input_file.readline()
        clean_line = head_split_up_line.head_split_up_line(line)
        head.update(clean_line)
        nlines += 1
    input_file.close()
    
    input_file = open(input_land, 'r')
    lines = input_file.readlines()
    lines = lines[6:]
    input_file.close()

    matrix = []
    for line in lines:
        matrix.append(map(float, line.strip().split(" ")))
    return head, matrix
