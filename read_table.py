import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math
#from rpy2 import robjects

def read_table(file_in):
    input_file = open(file_in, 'r')
    lines = input_file.readlines()
    lines = lines[1:]
    input_file.close()
    
    matrix = []
    for line in lines:
        matrix.append(map(float, line.strip().split(" ")))
    return matrix
