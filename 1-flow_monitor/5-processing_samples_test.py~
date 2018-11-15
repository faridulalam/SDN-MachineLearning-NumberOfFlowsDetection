"""This script is used to automatically take the values of
 OnwWayDelay (OWD) and InterArrivalTime (IAT) from a file and
 create instance for machine learner"""

# highlight peaks selected.
#
import numpy
import numpy as np
import peakutils
from peakutils.plot import plot as pplot
import matplotlib.pyplot as plt
from matplotlib import pyplot
import sys
import os
import subprocess
import random
from random import shuffle
from scipy.signal import argrelextrema

d = []
d_rm = []
t = []
g = []

"""Open the owd-new file and append S1 time, OWD and graph time axis values"""

#	Column 1 -- timestamps at switch 1, Column 2 -- OWD
#	Column 3 -- graph time which is a additive time [e.g. x=x+IAT(i)] IAT at switch 1

print "Append and Preprocess TimeStamps, OWD, GraphTime_S1..."

with open("owd-new.txt") as f:
    for l in f:
        l = l.split()
        t.append(float(l[0]))	# timestamps at switch 1
        if float(l[1]) >= 0.14:  # if more than expected value
            d.append(00.128000)
            d_rm.append(l[1])
        elif float(l[1]) <= 0.029:
            d.append(00.030000)  # if less then configured delay
            d_rm.append(l[1])
        else:
            d.append(float(l[1]))	# OWD
        g.append(float(l[2]))	# IAT at switch 1


print "Total no of TimeStamps, OWD, GraphTime_S1 values -- ", len(t), len(d), len(g)
print "Total no of Preprocessed OWD values -- ", len(d_rm)

""" Convert into np arrays"""

delay = np.array(d)     # Convert into np arrays
t = np.array(t)
graph = np.array(g)

iat = []
iat_rm = []
tt = []

#### Open the s4_iat-new file and append S4 time and IAT values ####

#	Column 1 -- timestamps at switch 4, Column 2 -- IAT at swtich 4
#	Column 3 -- timestamps at switch 1, Column 4 -- IAT at swtich 1

print "Append and Preprocess TimeStamps, IAT..."


with open("s4_iat-new.txt") as f:
    for l in f:
        l = l.split()
        tt.append(float(l[0]))	# timestamps at switch 4
        if float(l[1])>=0.0152:
            iat.append(00.0020)
            iat_rm.append(float(l[1]))
        elif float(l[1]) < 0.000:
            iat.append(0.0000)
            iat_rm.append(float(l[1]))
        else:
            iat.append(float(l[1]))	# IAT at swtich 4

iat_np = np.array(iat)

print "Total no of TimeStamps and IAT values -- ", len(tt), len(iat)
print "Total no of Preprocessed IAT values -- ", len(iat_rm)

Maximum_peak = max(d)
Minimum_delay = min(d)
print "OWD (max) -- ", Maximum_peak
print "OWD (min) -- ", Minimum_delay

#### Find the peak values, (tweak to find the approx peak value) ####

#### Peakutils provides utilities related to the detection of peaks on 1D data
# Includes functions to estimate baselines, finding the indexes of peaks in
# the data and performing Gaussian fitting or centroid computation to further
# increase the resolution of the peak detection.

#indexes = peakutils.indexes(delay, thres=0.08, min_dist=1000)
# ii=indexes
#print "Total peaks found: \n", len(indexes)
#print "Peaks found at (indexed values): \n",indexes

#time=t[indexes]			# corresponding time of each peak
#values=delay[indexes]	# corresponding delay (OWD) value
#graphs=graph[indexes]	# corresponding graph value

#print "\n time:",t[indexes],"\n values", delay[indexes]

#### to check no of peaks by eyes ###
#plt.plot(g,d,'ro')
#plt.show()

#### Selecting the different minimum level of OWD ####

print "Splitting whole OWD values into 21 Area...."


win_index0=[]
win_index1=[]
win_index2=[]
win_index3=[]
win_index4=[]
win_index5=[]
win_index6=[]
win_index7=[]
win_index8=[]
win_index9=[]
win_index10=[]
win_index11=[]
win_index12=[]
win_index13=[]
win_index14=[]
win_index15=[]
win_index16=[]
win_index17=[]
win_index18=[]
win_index19=[]
win_index20=[]
win_index21=[]

# The enumerate function returns a tuple containing the count (line no), and then the actual
# value from the iterable.

no_smpl_per_area = len(d) / 21
no_smpl_per_area_rem = len(d) % 21

print "No of OWD values per Area -- ", no_smpl_per_area
print "No of additional OWD values in last Area -- ", no_smpl_per_area_rem

index_Delay1=[]
index_Delay2=[]
index_Delay3=[]
index_Delay4=[]
index_Delay5=[]
index_Delay6=[]
index_Delay7=[]
index_Delay8=[]
index_Delay9=[]
index_Delay10=[]
index_Delay11=[]
index_Delay12=[]
index_Delay13=[]
index_Delay14=[]
index_Delay15=[]
index_Delay16=[]
index_Delay17=[]
index_Delay18=[]
index_Delay19=[]
index_Delay20=[]
index_Delay21=[]


for i in range(len(d)):
    if i < no_smpl_per_area:
        index_Delay1.append(i)
    if i >= no_smpl_per_area and i < 2*no_smpl_per_area:
        index_Delay2.append(i)
    if i >= 2*no_smpl_per_area and i < 3*no_smpl_per_area:
        index_Delay3.append(i)
    if i >= 3*no_smpl_per_area and i < 4*no_smpl_per_area:
        index_Delay4.append(i)
    if i >= 4*no_smpl_per_area and i < 5*no_smpl_per_area:
        index_Delay5.append(i)
    if i >= 5*no_smpl_per_area and i < 6*no_smpl_per_area:
        index_Delay6.append(i)
    if i >= 6*no_smpl_per_area and i < 7*no_smpl_per_area:
        index_Delay7.append(i)
    if i >= 7*no_smpl_per_area and i < 8*no_smpl_per_area:
        index_Delay8.append(i)
    if i >= 8*no_smpl_per_area and i < 9*no_smpl_per_area:
        index_Delay9.append(i)
    if i >= 9*no_smpl_per_area and i < 10*no_smpl_per_area:
        index_Delay10.append(i)
    if i >= 10*no_smpl_per_area and i < 11*no_smpl_per_area:
        index_Delay11.append(i)
    if i >= 11*no_smpl_per_area and i < 12*no_smpl_per_area:
        index_Delay12.append(i)
    if i >= 12*no_smpl_per_area and i < 13*no_smpl_per_area:
        index_Delay13.append(i)
    if i >= 13*no_smpl_per_area and i < 14*no_smpl_per_area:
        index_Delay14.append(i)
    if i >= 14*no_smpl_per_area and i < 15*no_smpl_per_area:
        index_Delay15.append(i)
    if i >= 15*no_smpl_per_area and i < 16*no_smpl_per_area:
        index_Delay16.append(i)
    if i >= 16*no_smpl_per_area and i < 17*no_smpl_per_area:
        index_Delay17.append(i)
    if i >= 17*no_smpl_per_area and i < 18*no_smpl_per_area:
        index_Delay18.append(i)
    if i >= 18*no_smpl_per_area and i < 19*no_smpl_per_area:
        index_Delay19.append(i)
    if i >= 19*no_smpl_per_area and i < 20*no_smpl_per_area:
        index_Delay20.append(i)
    if i >= 20*no_smpl_per_area:
        index_Delay21.append(i)


print "Area1 -- ", len(index_Delay1)
print "Area2 -- ", len(index_Delay2)
print "Area3 -- ", len(index_Delay3)
print "Area4 -- ", len(index_Delay4)
print "Area5 -- ", len(index_Delay5)
print "Area6 -- ", len(index_Delay6)
print "Area7 -- ", len(index_Delay7)
print "Area8 -- ", len(index_Delay8)
print "Area9 -- ", len(index_Delay9)
print "Area10 -- ", len(index_Delay10)
print "Area11 -- ", len(index_Delay11)
print "Area12 -- ", len(index_Delay12)
print "Area13 -- ", len(index_Delay13)
print "Area14 -- ", len(index_Delay14)
print "Area15 -- ", len(index_Delay15)
print "Area16 -- ", len(index_Delay16)
print "Area17 -- ", len(index_Delay17)
print "Area18 -- ", len(index_Delay18)
print "Area19 -- ", len(index_Delay19)
print "Area20 -- ", len(index_Delay20)
print "Area21 -- ", len(index_Delay21)

sum_Delay = len(index_Delay1) + len(index_Delay2) + len(index_Delay3) + len(index_Delay4) + len(index_Delay5) + len(index_Delay6) + len(index_Delay7) + len(index_Delay8) + len(index_Delay9) + len(index_Delay10) + len(index_Delay11) + len(index_Delay12) + len(index_Delay13) + len(index_Delay14) + len(index_Delay15) + len(index_Delay16) + len(index_Delay17) + len(index_Delay18) + len(index_Delay19) + len(index_Delay20) + len(index_Delay21)
print "Total No of OWD values from all considered area -- ", sum_Delay


#### Randomly select different number of samples from different levels ####

# random.sample(source, no of samples to consider)

sample_to_be_consider = 40	# its multiplication factor of 20 So, 20*200=4000
sample_ML = sample_to_be_consider * 21
window_size = 500	# no of values in each window
win_index=[]	# for all samples

print "No of OWD sample for Machine Learning -- ", sample_ML
print "No of OWD values per Window for a single sample -- ", window_size

### Area1 ###
if len(index_Delay1) < sample_to_be_consider:
    for i in range(len(index_Delay1)):
        if index_Delay1[i] > 3 * window_size  and (index_Delay1[i] + window_size) < len(d) :
            win_index1 = random.sample((index_Delay1), len(index_Delay1))
else:
    for i in range(len(index_Delay1)):
        if index_Delay1[i] > 3 * window_size and (index_Delay1[i] + window_size) < len(d):
            win_index1 = random.sample((index_Delay1), sample_to_be_consider)

### Area2 ###
if len(index_Delay2) < sample_to_be_consider:
    for i in range(len(index_Delay2)):
        if index_Delay2[i] > 3 * window_size  and (index_Delay2[i] + window_size) < len(d) :
            win_index2 = random.sample((index_Delay2), len(index_Delay2))
else:
    for i in range(len(index_Delay2)):
        if index_Delay2[i] > 3 * window_size and (index_Delay2[i] + window_size) < len(d):
            win_index2 = random.sample((index_Delay2), sample_to_be_consider)

### Area3 ###
if len(index_Delay3) < sample_to_be_consider:
    for i in range(len(index_Delay3)):
        if index_Delay3[i] > 3 * window_size  and (index_Delay3[i] + window_size) < len(d) :
            win_index3 = random.sample((index_Delay3), len(index_Delay3))
else:
    for i in range(len(index_Delay3)):
        if index_Delay3[i] > 3 * window_size and (index_Delay3[i] + window_size) < len(d):
            win_index3 = random.sample((index_Delay3), sample_to_be_consider)

### Area4 ###
if len(index_Delay4) < sample_to_be_consider:
    for i in range(len(index_Delay4)):
        if index_Delay4[i] > 3 * window_size  and (index_Delay4[i] + window_size) < len(d) :
            win_index4 = random.sample((index_Delay4), len(index_Delay4))
else:
    for i in range(len(index_Delay4)):
        if index_Delay4[i] > 3 * window_size and (index_Delay4[i] + window_size) < len(d):
            win_index4 = random.sample((index_Delay4), sample_to_be_consider)

### Area5 ###
if len(index_Delay5) < sample_to_be_consider:
    for i in range(len(index_Delay5)):
        if index_Delay5[i] > 3 * window_size  and (index_Delay5[i] + window_size) < len(d) :
            win_index5 = random.sample((index_Delay5), len(index_Delay5))
else:
    for i in range(len(index_Delay5)):
        if index_Delay5[i] > 3 * window_size and (index_Delay5[i] + window_size) < len(d):
            win_index5 = random.sample((index_Delay5), sample_to_be_consider)

### Area6 ###
if len(index_Delay6) < sample_to_be_consider:
    for i in range(len(index_Delay6)):
        if index_Delay6[i] > 3 * window_size  and (index_Delay6[i] + window_size) < len(d) :
            win_index6 = random.sample((index_Delay6), len(index_Delay6))
else:
    for i in range(len(index_Delay6)):
        if index_Delay6[i] > 3 * window_size and (index_Delay6[i] + window_size) < len(d):
            win_index6 = random.sample((index_Delay6), sample_to_be_consider)

### Area7 ###
if len(index_Delay7) < sample_to_be_consider:
    for i in range(len(index_Delay7)):
        if index_Delay7[i] > 3 * window_size  and (index_Delay7[i] + window_size) < len(d) :
            win_index7 = random.sample((index_Delay7), len(index_Delay7))
else:
    for i in range(len(index_Delay7)):
        if index_Delay7[i] > 3 * window_size and (index_Delay7[i] + window_size) < len(d):
            win_index7 = random.sample((index_Delay7), sample_to_be_consider)

### Area8 ###
if len(index_Delay8) < sample_to_be_consider:
    for i in range(len(index_Delay8)):
        if index_Delay8[i] > 3 * window_size  and (index_Delay8[i] + window_size) < len(d) :
            win_index8 = random.sample((index_Delay8), len(index_Delay8))
else:
    for i in range(len(index_Delay8)):
        if index_Delay8[i] > 3 * window_size and (index_Delay8[i] + window_size) < len(d):
            win_index8 = random.sample((index_Delay8), sample_to_be_consider)

### Area9 ###
if len(index_Delay9) < sample_to_be_consider:
    for i in range(len(index_Delay9)):
        if index_Delay9[i] > 3 * window_size  and (index_Delay9[i] + window_size) < len(d) :
            win_index9 = random.sample((index_Delay9), len(index_Delay9))
else:
    for i in range(len(index_Delay9)):
        if index_Delay9[i] > 3 * window_size and (index_Delay9[i] + window_size) < len(d):
            win_index9 = random.sample((index_Delay9), sample_to_be_consider)

### Area10 ###
if len(index_Delay10) < sample_to_be_consider:
    for i in range(len(index_Delay10)):
        if index_Delay10[i] > 3 * window_size  and (index_Delay10[i] + window_size) < len(d) :
            win_index10 = random.sample((index_Delay10), len(index_Delay10))
else:
    for i in range(len(index_Delay10)):
        if index_Delay10[i] > 3 * window_size and (index_Delay10[i] + window_size) < len(d):
            win_index10 = random.sample((index_Delay10), sample_to_be_consider)

### Area11 ###
if len(index_Delay11) < sample_to_be_consider:
    for i in range(len(index_Delay11)):
        if index_Delay11[i] > 3 * window_size  and (index_Delay11[i] + window_size) < len(d) :
            win_index11 = random.sample((index_Delay11), len(index_Delay11))
else:
    for i in range(len(index_Delay11)):
        if index_Delay11[i] > 3 * window_size and (index_Delay11[i] + window_size) < len(d):
            win_index11 = random.sample((index_Delay11), sample_to_be_consider)

### Area12 ###
if len(index_Delay12) < sample_to_be_consider:
    for i in range(len(index_Delay12)):
        if index_Delay12[i] > 3 * window_size  and (index_Delay12[i] + window_size) < len(d) :
            win_index12 = random.sample((index_Delay12), len(index_Delay12))
else:
    for i in range(len(index_Delay12)):
        if index_Delay12[i] > 3 * window_size and (index_Delay12[i] + window_size) < len(d):
            win_index12 = random.sample((index_Delay12), sample_to_be_consider)

### Area13 ###
if len(index_Delay13) < sample_to_be_consider:
    for i in range(len(index_Delay13)):
        if index_Delay13[i] > 3 * window_size  and (index_Delay13[i] + window_size) < len(d) :
            win_index13 = random.sample((index_Delay13), len(index_Delay13))
else:
    for i in range(len(index_Delay13)):
        if index_Delay13[i] > 3 * window_size and (index_Delay13[i] + window_size) < len(d):
            win_index13 = random.sample((index_Delay13), sample_to_be_consider)

### Area14 ###
if len(index_Delay14) < sample_to_be_consider:
    for i in range(len(index_Delay14)):
        if index_Delay14[i] > 3 * window_size  and (index_Delay14[i] + window_size) < len(d) :
            win_index14 = random.sample((index_Delay14), len(index_Delay14))
else:
    for i in range(len(index_Delay14)):
        if index_Delay14[i] > 3 * window_size and (index_Delay14[i] + window_size) < len(d):
            win_index14 = random.sample((index_Delay14), sample_to_be_consider)

### Area15 ###
if len(index_Delay15) < sample_to_be_consider:
    for i in range(len(index_Delay15)):
        if index_Delay15[i] > 3 * window_size  and (index_Delay15[i] + window_size) < len(d) :
            win_index15 = random.sample((index_Delay15), len(index_Delay15))
else:
    for i in range(len(index_Delay15)):
        if index_Delay15[i] > 3 * window_size and (index_Delay15[i] + window_size) < len(d):
            win_index15 = random.sample((index_Delay15), sample_to_be_consider)

### Area16 ###
if len(index_Delay16) < sample_to_be_consider:
    for i in range(len(index_Delay16)):
        if index_Delay16[i] > 3 * window_size  and (index_Delay16[i] + window_size) < len(d) :
            win_index16 = random.sample((index_Delay16), len(index_Delay16))
else:
    for i in range(len(index_Delay16)):
        if index_Delay16[i] > 3 * window_size and (index_Delay16[i] + window_size) < len(d):
            win_index16 = random.sample((index_Delay16), sample_to_be_consider)

### Area17 ###
if len(index_Delay17) < sample_to_be_consider:
    for i in range(len(index_Delay17)):
        if index_Delay17[i] > 3 * window_size  and (index_Delay17[i] + window_size) < len(d) :
            win_index17 = random.sample((index_Delay17), len(index_Delay17))
else:
    for i in range(len(index_Delay17)):
        if index_Delay17[i] > 3 * window_size and (index_Delay17[i] + window_size) < len(d):
            win_index17 = random.sample((index_Delay17), sample_to_be_consider)

### Area18 ###
if len(index_Delay18) < sample_to_be_consider:
    for i in range(len(index_Delay18)):
        if index_Delay18[i] > 3 * window_size  and (index_Delay18[i] + window_size) < len(d) :
            win_index18 = random.sample((index_Delay18), len(index_Delay18))
else:
    for i in range(len(index_Delay18)):
        if index_Delay18[i] > 3 * window_size and (index_Delay18[i] + window_size) < len(d):
            win_index18 = random.sample((index_Delay18), sample_to_be_consider)

### Area19 ###
if len(index_Delay19) < sample_to_be_consider:
    for i in range(len(index_Delay19)):
        if index_Delay19[i] > 3 * window_size  and (index_Delay19[i] + window_size) < len(d) :
            win_index19 = random.sample((index_Delay19), len(index_Delay19))
else:
    for i in range(len(index_Delay19)):
        if index_Delay19[i] > 3 * window_size and (index_Delay19[i] + window_size) < len(d):
            win_index19 = random.sample((index_Delay19), sample_to_be_consider)

### Area20 ###
if len(index_Delay20) < sample_to_be_consider:
    for i in range(len(index_Delay20)):
        if index_Delay20[i] > 3 * window_size and (index_Delay20[i] + window_size) < len(d):
            win_index20 = random.sample((index_Delay20), len(index_Delay20))
else:
    for i in range(len(index_Delay20)):
        if index_Delay20[i] > 3 * window_size and (index_Delay20[i] + window_size) < len(d):
            win_index20 = random.sample((index_Delay20), sample_to_be_consider)


### Area21 ###
if len(index_Delay21)!=0:
    if len(index_Delay21) < sample_to_be_consider:
        for i in range(len(index_Delay21)):
            if index_Delay21[i] > 3 * window_size  and (index_Delay21[i] + window_size) < len(d) :
                win_index21 = random.sample((index_Delay21), len(index_Delay21))
    else:
        for i in range(len(index_Delay21)):
            if index_Delay21[i] > 3 * window_size and (index_Delay21[i] + window_size) < len(d):
                win_index21 = random.sample((index_Delay21), sample_to_be_consider)



print "No of random OWD Samples from each area -- "
print  "Area0_sample -- ", len(win_index0)
print  "Area1_sample -- ", len(win_index1)
print  "Area2_sample -- ", len(win_index2)
print  "Area3_sample -- ", len(win_index3)
print  "Area4_sample -- ", len(win_index4)
print  "Area5_sample -- ", len(win_index5)
print  "Area6_sample -- ", len(win_index6)
print  "Area7_sample -- ", len(win_index7)
print  "Area8_sample -- ", len(win_index8)
print  "Area9_sample -- ", len(win_index9)
print  "Area10_sample -- ", len(win_index10)
print  "Area11_sample -- ", len(win_index11)
print  "Area12_sample -- ", len(win_index12)
print  "Area13_sample -- ", len(win_index13)
print  "Area14_sample -- ", len(win_index14)
print  "Area15_sample -- ", len(win_index15)
print  "Area16_sample -- ", len(win_index16)
print  "Area17_sample -- ", len(win_index17)
print  "Area18_sample -- ", len(win_index18)
print  "Area19_sample -- ", len(win_index19)
print  "Area20_sample -- ", len(win_index20)
print  "Area21_sample -- ", len(win_index21)


sum_Delay_samples = len(win_index0) + len(win_index1) + len(win_index2) + len(win_index3) + len(win_index4) + len(win_index5) + len(win_index6) + len(win_index7) + len(win_index8) + len(win_index9) + len(win_index10) + len(win_index11) + len(win_index12) + len(win_index13) + len(win_index14) + len(win_index15) + len(win_index16) + len(win_index17) + len(win_index18) + len(win_index19) + len(win_index20) + len(win_index21)
print "Total No of OWD Random samples from all different area -- ", sum_Delay_samples

win_index3_add=[]
win_index5_add=[]
win_index7_add=[]
win_index9_add=[]

win_index6_add=[]

#### Check and negotiate with desire no of samples ###
if sum_Delay_samples < (20*sample_to_be_consider):
    sample_to_be_add = (20*sample_to_be_consider) - sum_Delay_samples
    print "No of OWD samples to be add -- ", sample_to_be_add
    sample_to_be_add_new = (sample_to_be_add / 4) + sample_to_be_consider
    sample_to_be_add_remainder = sample_to_be_add % 4
    print "No of additional OWD samples to be add -- ",sample_to_be_add_remainder
    #win_index3_add = random.sample((index_Delay3), sample_to_be_add_new)
    #win_index5_add = random.sample((index_Delay5), sample_to_be_add_new)
    #win_index6_add = random.sample((index_Delay6), (sample_to_be_consider+ sample_to_be_add_remainder))
    #win_index7_add = random.sample((index_Delay7), sample_to_be_add_new)
    #win_index9_add = random.sample((index_Delay9), sample_to_be_add_new)

    ### Area3 ###
    if len(index_Delay3) < sample_to_be_add_new:
        for i in range(len(index_Delay3)):
            if index_Delay3[i] > 3 * window_size and (index_Delay3[i] + window_size) < len(d):
                win_index3_add = random.sample((index_Delay3), len(index_Delay3))
    else:
        for i in range(len(index_Delay3)):
            if index_Delay3[i] > 3 * window_size and (index_Delay3[i] + window_size) < len(d):
                win_index3_add = random.sample((index_Delay3), sample_to_be_add_new)

    ### Area5 ###
    if len(index_Delay5) < sample_to_be_add_new:
        for i in range(len(index_Delay5)):
            if index_Delay5[i] > 3 * window_size and (index_Delay5[i] + window_size) < len(d):
                win_index5_add = random.sample((index_Delay5), len(index_Delay5))
    else:
        for i in range(len(index_Delay5)):
            if index_Delay5[i] > 3 * window_size and (index_Delay5[i] + window_size) < len(d):
                win_index5_add = random.sample((index_Delay5), sample_to_be_add_new)

    ### Area6 ###
    if len(index_Delay6) < sample_to_be_consider:
        for i in range(len(index_Delay6)):
            if index_Delay6[i] > 3 * window_size and (index_Delay6[i] + window_size) < len(d):
                win_index6_add = random.sample((index_Delay6), len(index_Delay6))
    else:
        for i in range(len(index_Delay6)):
            if index_Delay6[i] > 3 * window_size and (index_Delay6[i] + window_size) < len(d):
                win_index6_add = random.sample((index_Delay6), (sample_to_be_consider+ sample_to_be_add_remainder))

    ### Area7 ###
    if len(index_Delay7) < sample_to_be_consider:
        for i in range(len(index_Delay7)):
            if index_Delay7[i] > 3 * window_size and (index_Delay7[i] + window_size) < len(d):
                win_index7_add = random.sample((index_Delay7), len(index_Delay7))
    else:
        for i in range(len(index_Delay7)):
            if index_Delay7[i] > 3 * window_size and (index_Delay7[i] + window_size) < len(d):
                win_index7_add = random.sample((index_Delay7), sample_to_be_add_new)

    ### Area9 ###
    if len(index_Delay9) < sample_to_be_consider:
        for i in range(len(index_Delay9)):
            if index_Delay9[i] > 3 * window_size and (index_Delay9[i] + window_size) < len(d):
                win_index9_add = random.sample((index_Delay9), len(index_Delay9))
    else:
        for i in range(len(index_Delay9)):
            if index_Delay9[i] > 3 * window_size and (index_Delay9[i] + window_size) < len(d):
                win_index9_add = random.sample((index_Delay9), sample_to_be_add_new)


if sum_Delay_samples >= (20*sample_to_be_consider):
	win_index3_add = win_index3
	win_index5_add = win_index5
	win_index6_add = win_index6
	win_index7_add = win_index7
	win_index9_add = win_index9

#print  "Area3_sample_new -- ", len(win_index3_add)
#print  "Area5_sample_new -- ", len(win_index5_add)
#print  "Area6_sample_new -- ", len(win_index6_add)
#print  "Area7_sample_new -- ", len(win_index7_add)
#print  "Area9_sample_new -- ", len(win_index9_add)

sum_Delay_samples = len(win_index0) + len(win_index1) + len(win_index2) + len(win_index3_add) + len(win_index4) + len(win_index5_add) + len(win_index6_add) + len(win_index7_add) + len(win_index8) + len(win_index9_add) + len(win_index10) + len(win_index11) + len(win_index12) + len(win_index13) + len(win_index14) + len(win_index15) + len(win_index16) + len(win_index17) + len(win_index18) + len(win_index19) + len(win_index20) + len(win_index21)
print "Total No of OWD Random samples (after) from all different area -- ", sum_Delay_samples




####### put all OWD samples together into win_index ######

print "Put all OWD samples into a single list..."

#for i in range(len(win_index0)):
#    win_index.append(win_index0[i])

for i in range(len(win_index1)):
    win_index.append(win_index1[i])

for i in range(len(win_index2)):
    win_index.append(win_index2[i])

for i in range(len(win_index3_add)):	# next phase addition
    win_index.append(win_index3_add[i])

for i in range(len(win_index4)):
    win_index.append(win_index4[i])

for i in range(len(win_index5_add)):	# next phase addition
    win_index.append(win_index5_add[i])

for i in range(len(win_index6_add)):	# next phase addition
    win_index.append(win_index6_add[i])

for i in range(len(win_index7_add)):	# next phase addition
    win_index.append(win_index7_add[i])

for i in range(len(win_index8)):
    win_index.append(win_index8[i])

for i in range(len(win_index9_add)):	# next phase addition
    win_index.append(win_index9_add[i])

for i in range(len(win_index10)):
    win_index.append(win_index10[i])

for i in range(len(win_index11)):
    win_index.append(win_index11[i])

for i in range(len(win_index12)):
    win_index.append(win_index12[i])

for i in range(len(win_index13)):
    win_index.append(win_index13[i])

for i in range(len(win_index14)):
    win_index.append(win_index14[i])

for i in range(len(win_index15)):
    win_index.append(win_index15[i])

for i in range(len(win_index16)):
    win_index.append(win_index16[i])

for i in range(len(win_index17)):
    win_index.append(win_index17[i])

for i in range(len(win_index18)):
    win_index.append(win_index18[i])

for i in range(len(win_index19)):
    win_index.append(win_index19[i])

for i in range(len(win_index20)):
    win_index.append(win_index20[i])

for i in range(len(win_index21)):
    win_index.append(win_index21[i])


print "Total No of OWD Random samples (after) put all together -- ", len(win_index)

########

print "--- Getting samples for OWD ---"

time=t[win_index]	# taking corrosponding time (timestamps at switch 1) of win_index
values=delay[win_index]	# taking corrosponding delay (OWD) of win_index

owd11=[]
owd12=[]
owd13=[]

open("owd-results_test","w").close()
#open("owd-noloss-results_Offline","w").close()
#open("iat-noloss-results_Offline","w").close()


for i in range(len(win_index)):  # select 3 different window here, window_size = 500
    indDelay1 = win_index[i] - (3 * window_size)  # taking previous delay value of win_index - 1000
    indDelay2 = win_index[i] - (2 * window_size)  # taking previous delay value of win_index - 500
    indDelay3 = win_index[i] - window_size# taking delay value of win_index

    for nn in range(window_size):  # window_size = 500
        owd11.append(d[indDelay1 + nn])  # taking additional 500 delay values from each
        owd12.append(d[indDelay2 + nn])  # indLoss points and put it to owd11/12/13
        owd13.append(d[indDelay3 + nn])  # now each owd has window of 500 values
        #print "nn loop -- ", len(owd11), len(owd12), len(owd13), nn, len(win_index), win_index[i]

    #print "OWD -- ", i
    #print "D -- ", len(d)
    #print indDelay1, indDelay2, indDelay3
    #print len(owd11), len(owd12), len(owd13)
    ### Number of packet in a window###

    ### for owd11 ###
    mean11 = numpy.mean(owd11)
    min11 = min(owd11)
    max11 = max(owd11)
    std11 = numpy.std(owd11)
    #print "number of packets included = {}".format(len(owd11))  # printing window length
    #print 'mean11 = {}'.format(numpy.mean(owd11))  # getting mean of 500 delay values
    #print 'min11 = {}'.format(min(owd11))  # getting min
    #print 'max11 = {}'.format(max(owd11))  # getting max
    #print 'std11 = {}'.format(numpy.std(owd11))  # getting standard deviation

    ### for owd12 ###
    mean12 = numpy.mean(owd12)
    min12 = min(owd12)
    max12 = max(owd12)
    std12 = numpy.std(owd12)

	#print "number of packets included = {}".format(len(owd12))
    #print 'mean12 = {}'.format(numpy.mean(owd12))
    #print 'min12 = {}'.format(min(owd12))
    #print 'max12 = {}'.format(max(owd12))
    #print 'std12 = {}'.format(numpy.std(owd12))

    ### for owd13 ###
    mean13 = numpy.mean(owd13)
    min13 = min(owd13)
    max13 = max(owd13)
    std13 = numpy.std(owd13)

    #print "number of packets included = {}".format(len(owd13))
    #print 'mean13 = {}'.format(numpy.mean(owd13))
    #print 'min13 = {}'.format(min(owd13))
    #print 'max13 = {}'.format(max(owd13))
    #print 'std13 = {}'.format(numpy.std(owd13))

    ### next take the Window3/Window1 ###
    a1 = numpy.mean(owd13) / numpy.mean(owd11)
    a2 = numpy.mean(owd13) / numpy.min(owd11)
    a3 = numpy.mean(owd13) / numpy.max(owd11)

    a4 = numpy.min(owd13) / numpy.mean(owd11)
    a5 = numpy.min(owd13) / numpy.min(owd11)
    a6 = numpy.min(owd13) / numpy.max(owd11)

    a7 = numpy.max(owd13) / numpy.mean(owd11)
    a8 = numpy.max(owd13) / numpy.min(owd11)
    a9 = numpy.max(owd13) / numpy.max(owd11)

    ### next take the Window3/Window2 ###
    a10 = numpy.mean(owd13) / numpy.mean(owd12)
    a11 = numpy.mean(owd13) / numpy.min(owd12)
    a12 = numpy.mean(owd13) / numpy.max(owd12)

    a13 = numpy.min(owd13) / numpy.mean(owd12)
    a14 = numpy.min(owd13) / numpy.min(owd12)
    a15 = numpy.min(owd13) / numpy.max(owd12)

    a16 = numpy.max(owd13) / numpy.mean(owd12)
    a17 = numpy.max(owd13) / numpy.min(owd12)
    a18 = numpy.max(owd13) / numpy.max(owd12)

    ### min/max window 3 ###
    a19 = numpy.min(owd13) / numpy.max(owd13)

    ### standard dev values ###
    a20 = numpy.std(owd13) / numpy.std(owd11)
    a21 = numpy.std(owd13) / numpy.std(owd12)
    a22 = numpy.std(owd11) / numpy.std(owd12)

    ### next window1 / window2 ###
    a23 = numpy.mean(owd11) / numpy.mean(owd12)
    a24 = numpy.mean(owd11) / numpy.min(owd12)
    a25 = numpy.mean(owd11) / numpy.max(owd12)

    a26 = numpy.min(owd11) / numpy.mean(owd12)
    a27 = numpy.min(owd11) / numpy.min(owd12)
    a28 = numpy.min(owd11) / numpy.max(owd12)

    a29 = numpy.max(owd11) / numpy.mean(owd12)
    a30 = numpy.max(owd11) / numpy.min(owd12)
    a31 = numpy.max(owd11) / numpy.max(owd12)

    owd11 = []
    owd12 = []
    owd13 = []

    with open("owd-results_test", "a") as f:
        f.write(str(a1) + "," + str(a2) + "," + str(a3) + "," + str(a4) + "," + str(a5) + "," + str(a6) + "," + str(
            a7) + "," + str(a8) + "," +
                str(a9) + "," + str(a10) + "," + str(a11) + "," + str(a12) + "," + str(a13) + "," + str(
            a14) + "," + str(a15) + "," + str(a16) + "," +
                str(a17) + "," + str(a18) + "," + str(a19) + "," + str(a20) + "," + str(a21) + "," + str(
            a22) + "," + str(a23) + "," + str(a24) + "," +
                str(a25) + "," + str(a26) + "," + str(a27) + "," + str(a28) + "," + str(a29) + "," + str(
            a30) + "," + str(a31) + "," + "I   " + "\n")

################################            IAT               ########################################

iat_s4=[]
iat_s4_rm=[]

with open("s4_iat.txt") as f:
    for l in f:
        l = l.split()
        tt.append(float(l[0]))	# timestamps at switch 4
        if float(l[1])>=0.0362:
            iat_s4.append(00.035000)
			#iat_s4.append(float(l[1]))
            iat_s4_rm.append(float(l[1]))
        elif float(l[1]) < 0.000:
            iat_s4.append(0.0000)
            iat_s4_rm.append(float(l[1]))
        else:
            iat_s4.append(float(l[1]))	# IAT at swtich 4

iat_s4_np = np.array(iat_s4)
no_smpl_per_area_iat = len(iat_s4) / 21
no_smpl_per_area_rem_iat = len(iat_s4) % 21

print "Total no of IAT TimeStamps and IAT_S4 values -- ", len(tt), len(iat_s4)
print "Total no of IAT Preprocessed IAT_S4 values -- ", len(iat_s4_rm)

print "No of IAT values per Area -- ", no_smpl_per_area_iat
print "No of additional IAT values in last Area -- ", no_smpl_per_area_rem_iat


index_iat1=[]
index_iat2=[]
index_iat3=[]
index_iat4=[]
index_iat5=[]
index_iat6=[]
index_iat7=[]
index_iat8=[]
index_iat9=[]
index_iat10=[]
index_iat11=[]
index_iat12=[]
index_iat13=[]
index_iat14=[]
index_iat15=[]
index_iat16=[]
index_iat17=[]
index_iat18=[]
index_iat19=[]
index_iat20=[]
index_iat21=[]


for i in range(len(iat_s4)):
    if i < no_smpl_per_area_iat:
        index_iat1.append(i)
    if i >= no_smpl_per_area_iat and i < 2*no_smpl_per_area_iat:
        index_iat2.append(i)
    if i >= 2*no_smpl_per_area_iat and i < 3*no_smpl_per_area_iat:
        index_iat3.append(i)
    if i >= 3*no_smpl_per_area_iat and i < 4*no_smpl_per_area_iat:
        index_iat4.append(i)
    if i >= 4*no_smpl_per_area_iat and i < 5*no_smpl_per_area_iat:
        index_iat5.append(i)
    if i >= 5*no_smpl_per_area_iat and i < 6*no_smpl_per_area_iat:
        index_iat6.append(i)
    if i >= 6*no_smpl_per_area_iat and i < 7*no_smpl_per_area_iat:
        index_iat7.append(i)
    if i >= 7*no_smpl_per_area_iat and i < 8*no_smpl_per_area_iat:
        index_iat8.append(i)
    if i >= 8*no_smpl_per_area_iat and i < 9*no_smpl_per_area_iat:
        index_iat9.append(i)
    if i >= 9*no_smpl_per_area_iat and i < 10*no_smpl_per_area_iat:
        index_iat10.append(i)
    if i >= 10*no_smpl_per_area_iat and i < 11*no_smpl_per_area_iat:
        index_iat11.append(i)
    if i >= 11*no_smpl_per_area_iat and i < 12*no_smpl_per_area_iat:
        index_iat12.append(i)
    if i >= 12*no_smpl_per_area_iat and i < 13*no_smpl_per_area_iat:
        index_iat13.append(i)
    if i >= 13*no_smpl_per_area_iat and i < 14*no_smpl_per_area_iat:
        index_iat14.append(i)
    if i >= 14*no_smpl_per_area_iat and i < 15*no_smpl_per_area_iat:
        index_iat15.append(i)
    if i >= 15*no_smpl_per_area_iat and i < 16*no_smpl_per_area_iat:
        index_iat16.append(i)
    if i >= 16*no_smpl_per_area_iat and i < 17*no_smpl_per_area_iat:
        index_iat17.append(i)
    if i >= 17*no_smpl_per_area_iat and i < 18*no_smpl_per_area_iat:
        index_iat18.append(i)
    if i >= 18*no_smpl_per_area_iat and i < 19*no_smpl_per_area_iat:
        index_iat19.append(i)
    if i >= 19*no_smpl_per_area_iat and i < 20*no_smpl_per_area_iat:
        index_iat20.append(i)
    if i >= 20*no_smpl_per_area_iat:
        index_iat21.append(i)


print "Area1 -- ", len(index_iat1)
print "Area2 -- ", len(index_iat2)
print "Area3 -- ", len(index_iat3)
print "Area4 -- ", len(index_iat4)
print "Area5 -- ", len(index_iat5)
print "Area6 -- ", len(index_iat6)
print "Area7 -- ", len(index_iat7)
print "Area8 -- ", len(index_iat8)
print "Area9 -- ", len(index_iat9)
print "Area10 -- ", len(index_iat10)
print "Area11 -- ", len(index_iat11)
print "Area12 -- ", len(index_iat12)
print "Area13 -- ", len(index_iat13)
print "Area14 -- ", len(index_iat14)
print "Area15 -- ", len(index_iat15)
print "Area16 -- ", len(index_iat16)
print "Area17 -- ", len(index_iat17)
print "Area18 -- ", len(index_iat18)
print "Area19 -- ", len(index_iat19)
print "Area20 -- ", len(index_iat20)
print "Area21 -- ", len(index_iat21)

sum_Delay_iat = len(index_iat1) + len(index_iat2) + len(index_iat3) + len(index_iat4) + len(index_iat5) + len(index_iat6) + len(index_iat7) + len(index_iat8) + len(index_iat9) + len(index_iat10) + len(index_iat11) + len(index_iat12) + len(index_iat13) + len(index_iat14) + len(index_iat15) + len(index_iat16) + len(index_iat17) + len(index_iat18) + len(index_iat19) + len(index_iat20) + len(index_iat21)
print "Total No of IAT values from all considered area -- ", sum_Delay_iat


sample_to_be_consider_iat = 40	# its multiplication factor of 20 So, 20*200=4000
sample_ML_iat = sample_to_be_consider_iat * 21
window_size_iat = 500	# no of values in each window

print "No of IAT sample for Machine Learning -- ", sample_ML_iat
print "No of IAT values per Window for a single sample -- ", window_size_iat

win_index_iat=[]	# for all samples

win_index_iat1=[]
win_index_iat2=[]
win_index_iat3=[]
win_index_iat4=[]
win_index_iat5=[]
win_index_iat6=[]
win_index_iat7=[]
win_index_iat8=[]
win_index_iat9=[]
win_index_iat10=[]
win_index_iat11=[]
win_index_iat12=[]
win_index_iat13=[]
win_index_iat14=[]
win_index_iat15=[]
win_index_iat16=[]
win_index_iat17=[]
win_index_iat18=[]
win_index_iat19=[]
win_index_iat20=[]
win_index_iat21=[]



### Area1 ###
if len(index_iat1) < sample_to_be_consider_iat:
    for i in range(len(index_iat1)):
        if index_iat1[i] > 3 * window_size_iat and (index_iat1[i] + window_size_iat) < len(iat_s4):
            win_index_iat1 = random.sample((index_iat1), len(index_iat1))
else:
    for i in range(len(index_iat1)):
        if index_iat1[i] > 3 * window_size_iat and (index_iat1[i] + window_size_iat) < len(iat_s4):
            win_index_iat1 = random.sample((index_iat1), sample_to_be_consider_iat)

### Area2 ###
if len(index_iat2) < sample_to_be_consider_iat:
    for i in range(len(index_iat2)):
        if index_iat2[i] > 3 * window_size_iat and (index_iat2[i] + window_size_iat) < len(iat_s4):
            win_index_iat2 = random.sample((index_iat2), len(index_iat2))
else:
    for i in range(len(index_iat2)):
        if index_iat2[i] > 3 * window_size_iat and (index_iat2[i] + window_size_iat) < len(iat_s4):
            win_index_iat2 = random.sample((index_iat2), sample_to_be_consider_iat)

### Area3 ###
if len(index_iat3) < sample_to_be_consider_iat:
    for i in range(len(index_iat3)):
        if index_iat3[i] > 3 * window_size_iat and (index_iat3[i] + window_size_iat) < len(iat_s4):
            win_index_iat3 = random.sample((index_iat3), len(index_iat3))
else:
    for i in range(len(index_iat3)):
        if index_iat3[i] > 3 * window_size_iat and (index_iat3[i] + window_size_iat) < len(iat_s4):
            win_index_iat3 = random.sample((index_iat3), sample_to_be_consider_iat)

### Area4 ###
if len(index_iat4) < sample_to_be_consider_iat:
    for i in range(len(index_iat4)):
        if index_iat4[i] > 3 * window_size_iat and (index_iat4[i] + window_size_iat) < len(iat_s4):
            win_index_iat4 = random.sample((index_iat4), len(index_iat4))
else:
    for i in range(len(index_iat4)):
        if index_iat4[i] > 3 * window_size_iat and (index_iat4[i] + window_size_iat) < len(iat_s4):
            win_index_iat4 = random.sample((index_iat4), sample_to_be_consider_iat)

### Area5 ###
if len(index_iat5) < sample_to_be_consider_iat:
    for i in range(len(index_iat5)):
        if index_iat5[i] > 3 * window_size_iat and (index_iat5[i] + window_size_iat) < len(iat_s4):
            win_index_iat5 = random.sample((index_iat5), len(index_iat5))
else:
    for i in range(len(index_iat5)):
        if index_iat5[i] > 3 * window_size_iat and (index_iat5[i] + window_size_iat) < len(iat_s4):
            win_index_iat5 = random.sample((index_iat5), sample_to_be_consider_iat)

### Area6 ###
if len(index_iat6) < sample_to_be_consider_iat:
    for i in range(len(index_iat6)):
        if index_iat6[i] > 3 * window_size_iat and (index_iat6[i] + window_size_iat) < len(iat_s4):
            win_index_iat6 = random.sample((index_iat6), len(index_iat6))
else:
    for i in range(len(index_iat6)):
        if index_iat6[i] > 3 * window_size_iat and (index_iat6[i] + window_size_iat) < len(iat_s4):
            win_index_iat6 = random.sample((index_iat6), sample_to_be_consider_iat)

### Area7 ###
if len(index_iat7) < sample_to_be_consider_iat:
    for i in range(len(index_iat7)):
        if index_iat7[i] > 3 * window_size_iat and (index_iat7[i] + window_size_iat) < len(iat_s4):
            win_index_iat7 = random.sample((index_iat7), len(index_iat7))
else:
    for i in range(len(index_iat7)):
        if index_iat7[i] > 3 * window_size_iat and (index_iat7[i] + window_size_iat) < len(iat_s4):
            win_index_iat7 = random.sample((index_iat7), sample_to_be_consider_iat)

### Area8 ###
if len(index_iat8) < sample_to_be_consider_iat:
    for i in range(len(index_iat8)):
        if index_iat8[i] > 3 * window_size_iat and (index_iat8[i] + window_size_iat) < len(iat_s4):
            win_index_iat8 = random.sample((index_iat8), len(index_iat8))
else:
    for i in range(len(index_iat8)):
        if index_iat8[i] > 3 * window_size_iat and (index_iat8[i] + window_size_iat) < len(iat_s4):
            win_index_iat8 = random.sample((index_iat8), sample_to_be_consider_iat)

### Area9 ###
if len(index_iat9) < sample_to_be_consider_iat:
    for i in range(len(index_iat9)):
        if index_iat9[i] > 3 * window_size_iat and (index_iat9[i] + window_size_iat) < len(iat_s4):
            win_index_iat9 = random.sample((index_iat9), len(index_iat9))
else:
    for i in range(len(index_iat9)):
        if index_iat9[i] > 3 * window_size_iat and (index_iat9[i] + window_size_iat) < len(iat_s4):
            win_index_iat9 = random.sample((index_iat9), sample_to_be_consider_iat)

### Area10 ###
if len(index_iat10) < sample_to_be_consider_iat:
    for i in range(len(index_iat10)):
        if index_iat10[i] > 3 * window_size_iat and (index_iat10[i] + window_size_iat) < len(iat_s4):
            win_index_iat10 = random.sample((index_iat10), len(index_iat10))
else:
    for i in range(len(index_iat10)):
        if index_iat10[i] > 3 * window_size_iat and (index_iat10[i] + window_size_iat) < len(iat_s4):
            win_index_iat10 = random.sample((index_iat10), sample_to_be_consider_iat)

### Area11 ###
if len(index_iat11) < sample_to_be_consider_iat:
    for i in range(len(index_iat11)):
        if index_iat11[i] > 3 * window_size_iat and (index_iat11[i] + window_size_iat) < len(iat_s4):
            win_index_iat11 = random.sample((index_iat11), len(index_iat11))
else:
    for i in range(len(index_iat11)):
        if index_iat11[i] > 3 * window_size_iat and (index_iat11[i] + window_size_iat) < len(iat_s4):
            win_index_iat11 = random.sample((index_iat11), sample_to_be_consider_iat)

### Area12 ###
if len(index_iat12) < sample_to_be_consider_iat:
    for i in range(len(index_iat12)):
        if index_iat12[i] > 3 * window_size_iat and (index_iat12[i] + window_size_iat) < len(iat_s4):
            win_index_iat12 = random.sample((index_iat12), len(index_iat12))
else:
    for i in range(len(index_iat12)):
        if index_iat12[i] > 3 * window_size_iat and (index_iat12[i] + window_size_iat) < len(iat_s4):
            win_index_iat12 = random.sample((index_iat12), sample_to_be_consider_iat)

### Area13 ###
if len(index_iat13) < sample_to_be_consider_iat:
    for i in range(len(index_iat13)):
        if index_iat13[i] > 3 * window_size_iat and (index_iat13[i] + window_size_iat) < len(iat_s4):
            win_index_iat13 = random.sample((index_iat13), len(index_iat13))
else:
    for i in range(len(index_iat13)):
        if index_iat13[i] > 3 * window_size_iat and (index_iat13[i] + window_size_iat) < len(iat_s4):
            win_index_iat13 = random.sample((index_iat13), sample_to_be_consider_iat)

### Area14 ###
if len(index_iat14) < sample_to_be_consider_iat:
    for i in range(len(index_iat14)):
        if index_iat14[i] > 3 * window_size_iat and (index_iat14[i] + window_size_iat) < len(iat_s4):
            win_index_iat14 = random.sample((index_iat14), len(index_iat14))
else:
    for i in range(len(index_iat14)):
        if index_iat14[i] > 3 * window_size_iat and (index_iat14[i] + window_size_iat) < len(iat_s4):
            win_index_iat14 = random.sample((index_iat14), sample_to_be_consider_iat)

### Area15 ###
if len(index_iat15) < sample_to_be_consider_iat:
    for i in range(len(index_iat15)):
        if index_iat15[i] > 3 * window_size_iat and (index_iat15[i] + window_size_iat) < len(iat_s4):
            win_index_iat15 = random.sample((index_iat15), len(index_iat15))
else:
    for i in range(len(index_iat15)):
        if index_iat15[i] > 3 * window_size_iat and (index_iat15[i] + window_size_iat) < len(iat_s4):
            win_index_iat15 = random.sample((index_iat15), sample_to_be_consider_iat)

### Area16 ###
if len(index_iat16) < sample_to_be_consider_iat:
    for i in range(len(index_iat16)):
        if index_iat16[i] > 3 * window_size_iat and (index_iat16[i] + window_size_iat) < len(iat_s4):
            win_index_iat16 = random.sample((index_iat16), len(index_iat16))
else:
    for i in range(len(index_iat16)):
        if index_iat16[i] > 3 * window_size_iat and (index_iat16[i] + window_size_iat) < len(iat_s4):
            win_index_iat16 = random.sample((index_iat16), sample_to_be_consider_iat)

### Area17 ###
if len(index_iat17) < sample_to_be_consider_iat:
    for i in range(len(index_iat17)):
        if index_iat17[i] > 3 * window_size_iat and (index_iat17[i] + window_size_iat) < len(iat_s4):
            win_index_iat17 = random.sample((index_iat17), len(index_iat17))
else:
    for i in range(len(index_iat17)):
        if index_iat17[i] > 3 * window_size_iat and (index_iat17[i] + window_size_iat) < len(iat_s4):
            win_index_iat17 = random.sample((index_iat17), sample_to_be_consider_iat)

### Area18 ###
if len(index_iat18) < sample_to_be_consider_iat:
    for i in range(len(index_iat18)):
        if index_iat18[i] > 3 * window_size_iat and (index_iat18[i] + window_size_iat) < len(iat_s4):
            win_index_iat18 = random.sample((index_iat18), len(index_iat18))
else:
    for i in range(len(index_iat18)):
        if index_iat18[i] > 3 * window_size_iat and (index_iat18[i] + window_size_iat) < len(iat_s4):
            win_index_iat18 = random.sample((index_iat18), sample_to_be_consider_iat)

### Area19 ###
if len(index_iat19) < sample_to_be_consider_iat:
    for i in range(len(index_iat19)):
        if index_iat19[i] > 3 * window_size_iat and (index_iat19[i] + window_size_iat) < len(iat_s4):
            win_index_iat19 = random.sample((index_iat19), len(index_iat19))
else:
    for i in range(len(index_iat19)):
        if index_iat19[i] > 3 * window_size_iat and (index_iat19[i] + window_size_iat) < len(iat_s4):
            win_index_iat19 = random.sample((index_iat19), sample_to_be_consider_iat)

### Area20 ###
if len(index_iat20) < sample_to_be_consider_iat:
    for i in range(len(index_iat20)):
        if index_iat20[i] > 3 * window_size_iat and (index_iat20[i] + window_size_iat) < len(iat_s4):
            win_index_iat20 = random.sample((index_iat20), len(index_iat20))
else:
    for i in range(len(index_iat20)):
        if index_iat20[i] > 3 * window_size_iat and (index_iat20[i] + window_size_iat) < len(iat_s4):
            win_index_iat20 = random.sample((index_iat20), sample_to_be_consider_iat)

### Area21 ###
if len(index_iat21) < sample_to_be_consider_iat:
    for i in range(len(index_iat21)):
        if index_iat21[i] > 3 * window_size_iat and (index_iat21[i] + window_size_iat) < len(iat_s4):
            win_index_iat21 = random.sample((index_iat21), len(index_iat21))
else:
    for i in range(len(index_iat21)):
        if index_iat21[i] > 3 * window_size_iat and (index_iat21[i] + window_size_iat) < len(iat_s4):
            win_index_iat21 = random.sample((index_iat21), sample_to_be_consider_iat)


sum_iat_samples = len(win_index_iat1) + len(win_index_iat2) + len(win_index_iat3) + len(win_index_iat4) + len(win_index_iat5) + len(win_index_iat6) + len(win_index_iat7) + len(win_index_iat8) + len(win_index_iat9) + len(win_index_iat10) + len(win_index_iat11) + len(win_index_iat12) + len(win_index_iat13) + len(win_index_iat14) + len(win_index_iat15) + len(win_index_iat16) + len(win_index_iat17) + len(win_index_iat18) + len(win_index_iat19) + len(win_index_iat20) + len(win_index_iat21)

print "Total No of Random IAT samples from all different area -- ", sum_iat_samples

for i in range(len(win_index_iat1)):
    win_index_iat.append(win_index_iat1[i])

for i in range(len(win_index_iat2)):
    win_index_iat.append(win_index_iat2[i])

for i in range(len(win_index_iat3)):
    win_index_iat.append(win_index_iat3[i])

for i in range(len(win_index_iat4)):
    win_index_iat.append(win_index_iat4[i])

for i in range(len(win_index_iat5)):
    win_index_iat.append(win_index_iat5[i])

for i in range(len(win_index_iat6)):
    win_index_iat.append(win_index_iat6[i])

for i in range(len(win_index_iat7)):
    win_index_iat.append(win_index_iat7[i])

for i in range(len(win_index_iat8)):
    win_index_iat.append(win_index_iat8[i])

for i in range(len(win_index_iat9)):
    win_index_iat.append(win_index_iat9[i])

for i in range(len(win_index_iat10)):
    win_index_iat.append(win_index_iat10[i])

for i in range(len(win_index_iat11)):
    win_index_iat.append(win_index_iat11[i])

for i in range(len(win_index_iat12)):
    win_index_iat.append(win_index_iat12[i])

for i in range(len(win_index_iat13)):
    win_index_iat.append(win_index_iat13[i])

for i in range(len(win_index_iat14)):
    win_index_iat.append(win_index_iat14[i])

for i in range(len(win_index_iat15)):
    win_index_iat.append(win_index_iat15[i])

for i in range(len(win_index_iat16)):
    win_index_iat.append(win_index_iat16[i])

for i in range(len(win_index_iat17)):
    win_index_iat.append(win_index_iat17[i])

for i in range(len(win_index_iat18)):
    win_index_iat.append(win_index_iat18[i])

for i in range(len(win_index_iat19)):
    win_index_iat.append(win_index_iat19[i])

for i in range(len(win_index_iat20)):
    win_index_iat.append(win_index_iat20[i])

for i in range(len(win_index_iat21)):
    win_index_iat.append(win_index_iat21[i])


print "Total No of Random IAT samples (after) put all together -- ", len(win_index_iat)

#(g,iat_s4,ro)

print "--- Getting samples for IAT ---"


owd11 = []
owd12 = []
owd13 = []


open("iat-results_test","w").close()


for i in range(len(win_index_iat)):
    indIAT1 = win_index_iat[i] - (3 * window_size_iat)
    indIAT2 = win_index_iat[i] - (2 * window_size_iat)
    indIAT3 = win_index_iat[i] - window_size_iat

    for nn in range(window_size_iat):
        owd11.append(iat_s4[indIAT1 + nn])
        owd12.append(iat_s4[indIAT2 + nn])
        owd13.append(iat_s4[indIAT3 + nn])

    #print "IAT -- ", i

    ### Number of packet in a window ###
    #print "number of packets included = {}".format(len(owd11))
    ### owd11 avg ###
    #print 'mean11 = {}'.format(numpy.mean(owd11))
    ### owd11 min ###
    #print 'min11 = {}'.format(min(owd11))
    ### owd11 max ###
    #print 'max11 = {}'.format(max(owd11))
    ### owd11 std ###
    #print 'std11 = {}'.format(numpy.std(owd11))

    mean11 = numpy.mean(owd11)
    min11 = min(owd11)
    max11 = max(owd11)
    std11 = numpy.std(owd11)


    ### for owd12 ###
    mean12 = numpy.mean(owd12)
    min12 = min(owd12)
    max12 = max(owd12)
    std12 = numpy.std(owd12)


    #print "number of packets included = {}".format(len(owd12))
    #print 'mean12 = {}'.format(numpy.mean(owd12))
    #print 'min12 = {}'.format(min(owd12))
    #print 'max12 = {}'.format(max(owd12))
    #print 'std12 = {}'.format(numpy.std(owd12))

    ### for owd13 ###
    mean13 = numpy.mean(owd13)
    min13 = min(owd13)
    max13 = max(owd13)
    std13 = numpy.std(owd13)


    #print "number of packets included = {}".format(len(owd13))
    #print 'mean13 = {}'.format(numpy.mean(owd13))
    #print 'min13 = {}'.format(min(owd13))
    #print 'max13 = {}'.format(max(owd13))
    #print 'std13 = {}'.format(numpy.std(owd13))

    ### next take the Window3/Window1 ###
    a1 = numpy.mean(owd13) / numpy.mean(owd11)
    a2 = numpy.mean(owd13) / numpy.min(owd11)
    a3 = numpy.mean(owd13) / numpy.max(owd11)

    a4 = numpy.min(owd13) / numpy.mean(owd11)
    a5 = numpy.min(owd13) / numpy.min(owd11)
    a6 = numpy.min(owd13) / numpy.max(owd11)

    a7 = numpy.max(owd13) / numpy.mean(owd11)
    a8 = numpy.max(owd13) / numpy.min(owd11)
    a9 = numpy.max(owd13) / numpy.max(owd11)

    ### next take the Window3/Window2 ###
    a10 = numpy.mean(owd13) / numpy.mean(owd12)
    a11 = numpy.mean(owd13) / numpy.min(owd12)
    a12 = numpy.mean(owd13) / numpy.max(owd12)

    a13 = numpy.min(owd13) / numpy.mean(owd12)
    a14 = numpy.min(owd13) / numpy.min(owd12)
    a15 = numpy.min(owd13) / numpy.max(owd12)

    a16 = numpy.max(owd13) / numpy.mean(owd12)
    a17 = numpy.max(owd13) / numpy.min(owd12)
    a18 = numpy.max(owd13) / numpy.max(owd12)

    ### min/max window 3 ###
    a19 = numpy.min(owd13) / numpy.max(owd13)

    ### standard dev values ###
    a20 = numpy.std(owd13) / numpy.std(owd11)
    a21 = numpy.std(owd13) / numpy.std(owd12)
    a22 = numpy.std(owd11) / numpy.std(owd12)

    ### next window1 / window2 ###
    a23 = numpy.mean(owd11) / numpy.mean(owd12)
    a24 = numpy.mean(owd11) / numpy.min(owd12)
    a25 = numpy.mean(owd11) / numpy.max(owd12)

    a26 = numpy.min(owd11) / numpy.mean(owd12)
    a27 = numpy.min(owd11) / numpy.min(owd12)
    a28 = numpy.min(owd11) / numpy.max(owd12)

    a29 = numpy.max(owd11) / numpy.mean(owd12)
    a30 = numpy.max(owd11) / numpy.min(owd12)
    a31 = numpy.max(owd11) / numpy.max(owd12)

    owd11 = []
    owd12 = []
    owd13 = []

    with open("iat-results_test", "a") as f:
        f.write(str(a1) + "," + str(a2) + "," + str(a3) + "," + str(a4) + "," + str(a5) + "," + str(a6) + "," + str(
            a7) + "," + str(a8) + "," +
                str(a9) + "," + str(a10) + "," + str(a11) + "," + str(a12) + "," + str(a13) + "," + str(
            a14) + "," + str(a15) + "," + str(a16) + "," +
                str(a17) + "," + str(a18) + "," + str(a19) + "," + str(a20) + "," + str(a21) + "," + str(
            a22) + "," + str(a23) + "," + str(a24) + "," +
                str(a25) + "," + str(a26) + "," + str(a27) + "," + str(a28) + "," + str(a29) + "," + str(
            a30) + "," + str(a31) + "," + "I   " + "\n")



### Removing the 'NAN' & 'INF' words from the file ###

print "Preprocessing IAT samples for ML..."

replacements = {'inf':'0.0','nan':'0.0','-':''}
#replacements = {'inf':'0','nan':'0'}

lines = []
with open('iat-results_test') as infile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        lines.append(line)
#print lines
with open('iat-results_test', 'w') as outfile:
    for line in lines:
        outfile.write(line)

#print len(g), len(d)
#, iat_s4_graph

### Plotting Graph OWD ###

plt.title("1 - Flow, Queue=100, RTT=60ms, BW=20Mbps", fontsize=16)	# set titels, x and y label
plt.xlabel('Time (sec)', fontsize=14)
plt.ylabel('One-way Delay (sec)', fontsize=14)

#plt.plot(graph, delay,linewidth=0.4, label='Measured OWD')	# plot line graph between graph and delay
plt.plot(graph, delay,'bx', ls="", ms=3,label='Measured OWD')
plt.xticks(np.arange(min(graph), max(graph), 20.0))	# set the current tick locations and labels of the x-axis
plt.grid(True)
plt.plot(graph[win_index],delay[win_index],'ro', ls="", ms=3, label='Training Samples - OWD')	# mark congestion points in RED

plt.axvline(x=graph[max(index_Delay1)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay2)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay3)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay4)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay5)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay6)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay7)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay8)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay9)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay10)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay11)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay12)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay13)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay14)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay15)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay16)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay17)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay18)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay19)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay20)],c="g",linewidth=2,zorder=0)
plt.axvline(x=graph[max(index_Delay21)],c="g",linewidth=2,zorder=0)

plt.legend()
plt.savefig('OWD_test.png', figsize=(30,15), dpi = 300)
#plt.savefig('OWD.pdf')
pyplot.show()



### Plotting Graph IAT ###

### Creating S4 graph time ###
x_iat = 0.00
#x = list()
iat_s4_graph=list()

#iat_s1_bf=list()
#iat_s1_b=list()
iat_s4_bb=list()

for i in range(len(iat_s4)):
	iat_s4_bf = str(iat_s4[i])
	iat_s4_b = iat_s4_bf.split(":")
	iat_s4_bb.append(float(iat_s4_b[-1]))
	#print type(iat_s1_bb[i]), iat_s1_bb, type(x)
	if i==0:
		iat_s4_graph.append(0.0)
		#print iat_s1_after, type(iat_s1_after)
	else:
		x_iat=float(iat_s4_bb[i]) + x_iat
		iat_s4_graph.append(float(x_iat))

iat_s4_np = np.array(iat_s4)     # Convert into np arrays
iat_s4_graph_np = np.array(iat_s4_graph)

#print len(iat_s4_graph), len(iat_s4)
#print type(iat_s4_graph_np[1]), type(iat_s4_np[1]), type(graph[1]), type(delay[1])


plt.title("1 - Flow, Queue=100, RTT=60ms, BW=20Mbps", fontsize=16)	# set titels, x and y label
plt.xlabel('Time (sec)', fontsize=14)
plt.ylabel('Inter-Arrival Time (sec)', fontsize=14)

#plt.plot(iat_s4_graph_np, iat_s4_np,linewidth=0.5)	# plot line graph between graph and delay
plt.plot(iat_s4_graph_np, iat_s4_np,'bx', ls="", ms=3,label='IAT')
plt.xticks(np.arange(min(iat_s4_graph_np), max(iat_s4_graph_np), 20.0))	# set the current tick locations and labels of the x-axis
plt.grid(True)
plt.plot(iat_s4_graph_np[win_index_iat],iat_s4_np[win_index_iat],'ro', ls="", ms=3,label='Test Samples - IAT')	# mark congestion points in RED

plt.axvline(x=iat_s4_graph_np[max(index_iat1)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat2)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat3)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat4)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat5)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat6)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat7)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat8)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat9)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat10)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat11)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat12)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat13)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat14)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat15)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat16)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat17)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat18)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat19)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat20)],c="g",linewidth=2,zorder=0)
plt.axvline(x=iat_s4_graph_np[max(index_iat21)],c="g",linewidth=2,zorder=0)

plt.legend()
plt.savefig('iat_test.png', figsize=(30,15), dpi = 300)
#plt.savefig('iat.pdf')
pyplot.show()
