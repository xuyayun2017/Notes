# coding=utf-8
'''
   https://blog.csdn.net/u011077672/article/details/77753300

   pip install pyshp    python中处理 shapefile 的包
'''

import numpy as np
from mpl_toolkits.basemap import Basemap
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
import shapefile as sf
from matplotlib.mlab import griddata
import json
from shapely.geometry import Polygon as ShapelyPolygon
from shapely.geometry import Point as ShapelyPoint