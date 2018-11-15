#!/usr/bin/python


from itertools import islice
from collections import Counter
import datetime
from datetime import timedelta
import operator
import numpy as np
import re 
from peakutils.plot import plot as pplot
import matplotlib.pyplot as plt

from matplotlib import pyplot
import random
import numpy
import numpy as np
from pylab import figure, axes, pie, title, show
import os, os.path
import matplotlib.pyplot as plt; plt.rcdefaults()
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.font_manager import FontProperties
import os




########## Train ########


os.system('java -cp /home/faridul/Desktop/weka-3-8-2/weka.jar weka.core.Instances append tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_1.arff tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_2.arff > tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_1_2.arff')	

os.system('java -cp /home/faridul/Desktop/weka-3-8-2/weka.jar weka.core.Instances append tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_1_2.arff tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_3.arff > tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_1_2_3.arff')	

os.system('java -cp /home/faridul/Desktop/weka-3-8-2/weka.jar weka.core.Instances append tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_1_2_3.arff tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_4.arff > tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_1_2_3_4.arff')	

os.system('java -cp /home/faridul/Desktop/weka-3-8-2/weka.jar weka.core.Instances append tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_1_2_3_4.arff tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_5.arff > tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_1_2_3_4_5.arff')

os.system('java -cp /home/faridul/Desktop/weka-3-8-2/weka.jar weka.core.Instances append tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_1_2_3_4_5.arff tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_6.arff > tree_I+II+III+IV+V+VI+VII+VIII+IX+X+XI+XII+XIII+XIV+XV_1_2_3_4_5_6.arff')







