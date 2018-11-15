#!/usr/bin/python

"""
This file filter out TimeStamps and CheckSum...
match CheckSum between switch S1 and S4 and
calculate OneWayDelay (OWD), InterArrivalTime (IAT)
at switch S1 and S4
"""

from itertools import islice
from datetime import timedelta
import datetime

from collections import Counter
import operator
import numpy as np


iat_1=[]
timestamps_1=[]

mins1=[]
sec1=[]
sec1_diff=[]
mins1_diff=[]
chksum1=[]
field_1=[]


iat_2=[]
timestamps_2=[]
mins2=[]
sec2=[]
sec2_diff=[]
mins2_diff=[]
chksum2=[]
field_2=[]
j=0


##### FOR SWITCH S1 ######

print "--- Start filtering S1 ---"

open('FilterS1.txt', 'w').close()

### Filter out only packet_in msg from SWITCH 1 ###

with open('switch1_monitor') as f1:
	for line in f1:
		line = line.rstrip()
		if line.startswith('201') and 'NXT_PACKET_IN' in line:
			line = line.strip()
			# join the next line to OFPT_PACKET_IN
			newline = line + ' '+ ''.join(islice(f1,1))

			# check if this is packet from h1 as source
			if 'tp_src=' in newline:
				with open('FilterS1.txt', 'a') as wfile:
					wfile.write("%s" %newline)

print "Append TimeStamps and CheckSum"
### Append TimeStamps and CheckSum ###

with open('FilterS1.txt', 'r') as tfile1:
	for l in tfile1:
		l = l.rstrip().split(' ')  # split based on white space

		### APPEND DUPLICATE CHECKSUMS
		chksum1.append(l[-1:])	# append CheckSum
		field_1=l[1]	# append TimeStamps
		timestamps_1.append(field_1[:-1])	# append timestamps

	for n in range(len(timestamps_1)):
		timeFormat = '%H:%M:%S.%f'
		if n>0:
			# Calculate the IAT at SWITCH1
			iat_1.append(datetime.datetime.strptime(timestamps_1[n],timeFormat) - datetime.datetime.strptime(timestamps_1[n-1],timeFormat))


print "Total no of packets capture in S1 -- ", len(timestamps_1), len(chksum1)
#print len(iat_1), len(timestamps_1)

timestamps_1_1=list()
timestamps_1_2=list()
iat_1_1=list()
iat_1_2=list()
# writing IAT at switch 1 into a file name s1_iat
open('s1_iat.txt', 'w').close()
with open('s1_iat.txt','w+') as iat_s1:
	for i in range(len(iat_1)):
		timestamps_1_2 = str(timestamps_1[i])
		timestamps_1_1 = timestamps_1_2.split(":")
		iat_1_2 = str(iat_1[i])
		iat_1_1 = iat_1_2.split(":")
		iat_s1.write(" " + str(timestamps_1_1[-1]) + "    " + str(iat_1_1[-1]) + "     " + "     " + "\n")


print "Writing TimeStamps, CheckSum and IAT_S1 for SWITCH1"
# Create and empty Time file
open('S1Data.txt', 'w').close()

with open('S1Data.txt', "w+") as timef:
	for n in range(len(iat_1)):
		# timef.write(str(timestamps_1[n+1]) + " " + str(chksum1[n+1]) +" " + str(iat_1[n])  + "\n")
		timef.write(str(timestamps_1[n + 1]) + " " + str(chksum1[n + 1]) + " " + str(iat_1[n]) + "\n")


################	FOR SWITCH S2	####################

print "--- Start filtering S4 ---"

# Create and empty the result file
open('FilterS4.txt', 'w').close()

with open('switch4_monitor') as f4:
	for line in f4:
		line = line.rstrip()
		if line.startswith('201') and 'NXT_PACKET_IN' in line:
			line = line.strip()
			# join the next line to OFPT_PACKET_IN
			newline = line + ' '+ ''.join(islice(f4,1))

			# check if this is packet from h1 as source port 34727
			if 'tp_src=' in newline:
				with open('FilterS4.txt', 'a') as wfile:
					wfile.write("%s" %newline)


print "Append TimeStamps and CheckSum"
with open('FilterS4.txt', 'r') as tfile4:
	for l in tfile4:
		l = l.rstrip().split(' ')
		#print l[1]

		### APPEND DUPLICATE CHECKSUMS
		chksum2.append(l[-1:])
		field_2=l[1]
		timestamps_2.append(field_2[:-1])


	for n in range(len(timestamps_2)):
		datetimeFormat = '%H:%M:%S.%f'
		#print timestamps_2[n]

		if n > 0:
			# Calculate the IAT at switch4
			iat_2.append(datetime.datetime.strptime(timestamps_2[n], datetimeFormat) - datetime.datetime.strptime(timestamps_2[n - 1], datetimeFormat))

print "Total no of packets capture in S4 -- ", len(timestamps_2), len(chksum2)

timestamps_2_1=list()
timestamps_2_2=list()
iat_2_1=list()
iat_2_2=list()
# writing IAT at switch 4 into a file name s4_iat
open('s4_iat.txt', 'w').close()
with open('s4_iat.txt','w+') as iat_s4:
	for i in range(len(iat_2)):
		timestamps_2_2 = str(timestamps_2[i])
		timestamps_2_1 = timestamps_2_2.split(":")
		iat_2_2 = str(iat_2[i])
		iat_2_1 = iat_2_2.split(":")
		iat_s4.write(" " + str(timestamps_2_1[-1]) + "    " + str(iat_2_1[-1]) + "     " + "     " + "\n")


print "Writing TimeStamps, CheckSum and IAT_S4 for SWITCH4"
open('S4Data.txt', 'w').close()

# Save timestamps, IAT and checksum of switch4 in a file
with open('S4Data.txt', "w+") as timef2:
	for n in range(len(chksum2) - 1):
		timef2.write(str(timestamps_2[n + 1]) + " " + str(chksum2[n + 1]) + " " + str(iat_2[n]) + "\n")

### getting no of packet different between S1 and S4 (loss)
pkt_diff = len(timestamps_1) - len(timestamps_2)
print "No of packets difference in S1 to S4 -- ", pkt_diff

#Calculation of ONE WAY DELAY (between Switch1 - to - Swithc4)

print "Append time at S1 and S4"

time1=list()
time2=list()
delay=list()
delay_2=list()
iat_s1=list()
iat_s4=list()

# Open the switch1 time file, and append the time
with open('S1Data.txt','r') as tf1:
	for l in tf1:
		l=l.split(" ")
		time1.append(l[0])

time_new=[]
with open('S4Data.txt','r') as tf2:
	for m in tf2:
		m=m.split(" ")
		time2.append(m[0])

print "--- Calculating OWD ---"

open('delay_time_csum.txt', 'w').close()

# define loop range
if len(time1) >= len(time2):
	loop_range = len(time2)
else:
	loop_range = len(time1)


with open('delay_time_csum.txt', 'w+') as df_2:

	datetimeFormat = '%H:%M:%S.%f'
	for y in range(loop_range):
		#print "for y", y
		if (chksum1[y+1] == chksum2[y+1]):
			#print "time1  time2 -- ",time1[y], time2[y], "chksum1 == chksum2", chksum1[y+1], "=",chksum2[y+1]
			delay.append(datetime.datetime.strptime(time2[y], datetimeFormat) - datetime.datetime.strptime(time1[y],datetimeFormat))
			iat_s1.append(datetime.datetime.strptime(time1[y+1], datetimeFormat) - datetime.datetime.strptime(time1[y],datetimeFormat))
			#iat_s4.append(datetime.datetime.strptime(time2[y+1], datetimeFormat) - datetime.datetime.strptime(time2[y],datetimeFormat))
			df_2.write(str((datetime.datetime.strptime(time2[y], datetimeFormat) - datetime.datetime.strptime(time1[y],datetimeFormat))))
			#df_2.write(str((datetime.datetime.strptime(time1[y+1], datetimeFormat) - datetime.datetime.strptime(time1[y],datetimeFormat))))
			#df_2.write(str((datetime.datetime.strptime(time2[y+1], datetimeFormat) - datetime.datetime.strptime(time2[y],datetimeFormat))))
			#df_2.write(" " + str(time1[y]) + " " + str(time2[y]) + " " + str(chksum1[y+1]) + " " + str(chksum2[y+1]) + "  " + str(iat_s1[y]) + "   " + "   " + "   " + str(iat_s4[y]) + "  " + "\n")
			df_2.write(" " + str(time1[y]) + " " + str(time2[y]) + " " + str(chksum1[y+1]) + " " + str(chksum2[y+1]) + "\n")
		else:
			#print "else"
			if (y-1000) >= 0:
				start = y-1000
			elif (y-800) >= 0:
				start = y-800
			elif (y-600) >= 0:
				start = y-600
			elif (y-400) >= 0:
				start = y-400
			elif (y - 200) >= 0:
				start = y - 200
			else:
				start = 0

			if (y+650) <= len(time2):
				end = y+650
			elif (y+500) <= len(time2):
				end = y+500
			elif (y+300) <= len(time2):
				end = y+300
			else:
				end = loop_range

			#print "else", y

			for z in range(start, end):
				#print "y-", y, "z-", z, "chksum1=", chksum1[y], "chksum2=", chksum1[z]
				if (chksum1[y+1] == chksum2[z+1]):
					if (time2[z] > time1[y]):
						delay.append(datetime.datetime.strptime(time2[z], datetimeFormat) - datetime.datetime.strptime(time1[y],datetimeFormat))
						iat_s1.append(datetime.datetime.strptime(time1[y + 1], datetimeFormat) - datetime.datetime.strptime(time1[y], datetimeFormat))
						#iat_s4.append(datetime.datetime.strptime(time2[y + 1], datetimeFormat) - datetime.datetime.strptime(time2[y], datetimeFormat))
						df_2.write(str((datetime.datetime.strptime(time2[z], datetimeFormat) - datetime.datetime.strptime(time1[y], datetimeFormat))))
						df_2.write(" " + str(time1[y]) + " " + str(time2[z]) + " " + str(chksum1[y + 1]) + " " + str(chksum2[z + 1]) + "\n")
						#print "y-", y, "z-", z, "chksum1[y+1] = chksum2[z+1]", chksum1[y+1], "=", chksum2[z+1]

					break


# append delay only (after checksum matching)

delay_bf=list()
delay_b=list()
delay_after=list()

time1_bf=list()
time1_b=list()
time1_after=list()

time4_bf=list()
time4_b=list()
time4_after=list()

time1_after_iat1=list()
time4_after_iat4=list()

print "Append Delay, TimeStamps S1 & S4 (from) delay_time_csum.txt"

with open('delay_time_csum.txt','r') as dtc1:
	for l in dtc1:

		l_sep = l.split(" ")
		# print l[3]
		# print len(l)
		#print l

		delay_bf = str(l_sep[0])
		delay_b=delay_bf.split(":")
		delay_after.append(delay_b[-1])

		time1_bf = str(l_sep[1])
		time1_b=time1_bf.split(":")
		time1_after.append(float(time1_b[-1]))

		time4_bf = str(l_sep[2])
		time4_b = time4_bf.split(":")
		time4_after.append(float(time4_b[-1]))
		#print type(time1_after[0]), type(time4_after[0])

### calculating graph scale by using iat at switch 1
print "Calculating graph time"
#print delay_after

x = 0.00
#x = list()
iat_s1_graph=list()

#iat_s1_bf=list()
#iat_s1_b=list()
iat_s1_bb=list()

for i in range(len(iat_s1)):
	iat_s1_bf = str(iat_s1[i])
	iat_s1_b = iat_s1_bf.split(":")
	iat_s1_bb.append(float(iat_s1_b[-1]))
	#print type(iat_s1_bb[i]), iat_s1_bb, type(x)
	if i==0:
		iat_s1_graph.append(0.0)
		#print iat_s1_after, type(iat_s1_after)
	else:
		x=float(iat_s1_bb[i]) + x
		iat_s1_graph.append(float(x))

print "No of values in owd-new.txt -- ", len(delay_after)
#print len(time1_after), type(time1_after)
#print len(time4_after), type(time4_after)
#print len(iat_s1_after), type(iat_s1_graph)

print "Writing --> owd-new.txt"
open('owd-new.txt', 'w').close()

with open('owd-new.txt','w+') as owdnew:
	for i in range(len(delay_after)):
		owdnew.write("  " +str(time1_after[i]) + "     " + str(delay_after[i]) + "     " + str(iat_s1_graph[i]) + "\n")


print "Writing --> s4_iat-new.txt"

open('s4_iat-new.txt', 'w').close()

delay_after_1 = len(delay_after) - 1
print "No of values in s4_iat-new.txt -- ", delay_after_1
#print len(time4_after), len(time1_after)
with open('s4_iat-new.txt','w+') as s4iatnew:
	for i in range(delay_after_1):
		if i == 0:
			s4iatnew.write("  " + str(time4_after[i]) + "   " + str(0.0) + "                " + str(time1_after[i]) + "                " + str(0.0) + "\n")
		else:
			s4iatnew.write("  " + str(time4_after[i]) + "   " + str(time4_after[i + 1] - time4_after[i]) + "                " + str(time1_after[i]) + "                " + str(time1_after[i + 1] - time1_after[i]) + "\n")


#'''''