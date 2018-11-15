"""This script combines all of the result file, and generates a single .arff file"""

l1=[]
l2=[]
l3=[]
l4=[]


## Open and append owd loss result file
with open("owd-results") as f1:
	for line1 in f1:
		l1.append(line1)


# print l1[1]
# print l1[1][:-3]

## Open and append iat loss result file
with open("iat-results") as f2:
	for line2 in f2:
		l2.append(line2)

print len(l1), len(l2)
## Open and append owd no-loss result file
#with open("owd-noloss-results_Offline") as f3:
#	for line3 in f3:

		# line3.strip()
#		l3.append(line3)

## Open and append iat no-loss result file
#with open("iat-noloss-results_Offline") as f4:
#	for line4 in f4:
		# line4.strip()
#		l4.append(line4)


## write to a new file
open("all_Offline_VIII.arff","w").close()

with open("all_Offline_VIII.arff","w+") as wf:
	wf.write('@relation ms-mbps-Q' + "\n" + "\n"  )
	wf.write('@attribute avgw3delay_div_avgw1delay numeric' + "\n" )
	wf.write('@attribute avgw3delay_div_minw1delay numeric' + "\n" )
	wf.write('@attribute avgw3delay_div_maxw1delay numeric' + "\n" )
	wf.write('@attribute avgw3delay_div_avgw2delay numeric' + "\n" )
	wf.write('@attribute avgw3delay_div_minw2delay numeric' + "\n" )
	wf.write('@attribute avgw3delay_div_maxw2delay numeric' + "\n" )
	wf.write('@attribute minw3delay_div_avgw1delay numeric' + "\n" )
	wf.write('@attribute minw3delay_div_minw1delay numeric' + "\n" )
	wf.write('@attribute minw3delay_div_maxw1delay numeric' + "\n" )
	wf.write('@attribute minw3delay_div_avgw2delay numeric' + "\n" )
	wf.write('@attribute minw3delay_div_minw2delay numeric' + "\n" )
	wf.write('@attribute minw3delay_div_maxw2delay numeric' + "\n" )
	wf.write('@attribute maxw3delay_div_avgw1delay numeric' + "\n" )
	wf.write('@attribute maxw3delay_div_minw1delay numeric' + "\n" )
	wf.write('@attribute maxw3delay_div_maxw1delay numeric' + "\n" )
	wf.write('@attribute maxw3delay_div_avgw2delay numeric' + "\n" )
	wf.write('@attribute maxw3delay_div_minw2delay numeric' + "\n" )
	wf.write('@attribute maxw3delay_div_maxw2delay numeric' + "\n" )
	wf.write('@attribute minw3delay_div_maxw3delay numeric' + "\n" )
	wf.write('@attribute stdw3delay_div_stdw1delay numeric' + "\n" )
	wf.write('@attribute stdw3delay_div_stdw2delay numeric' + "\n" )
	wf.write('@attribute stdw1delay_div_stdw2delay numeric' + "\n" )
	wf.write('@attribute avgw1delay_div_avgw2delay numeric' + "\n" )
	wf.write('@attribute avgw1delay_div_minw2delay numeric' + "\n" )
	wf.write('@attribute avgw1delay_div_maxw2delay numeric' + "\n" )
	wf.write('@attribute minw1delay_div_avgw2delay numeric' + "\n" )
	wf.write('@attribute minw1delay_div_minw2delay numeric' + "\n" )
	wf.write('@attribute minw1delay_div_maxw2delay numeric' + "\n" )
	wf.write('@attribute maxw1delay_div_avgw2delay numeric' + "\n" )
	wf.write('@attribute maxw1delay_div_minw2delay numeric' + "\n" )
	wf.write('@attribute maxw1delay_div_maxw2delay numeric' + "\n" )

	wf.write('@attribute avgw3iat_div_avgw1iat numeric' + "\n" )
	wf.write('@attribute avgw3iat_div_minw1iat numeric' + "\n" )
	wf.write('@attribute avgw3iat_div_maxw1iat numeric' + "\n" )
	wf.write('@attribute avgw3iat_div_avgw2iat numeric' + "\n" )
	wf.write('@attribute avgw3iat_div_minw2iat numeric' + "\n" )
	wf.write('@attribute avgw3iat_div_maxw2iat numeric' + "\n" )
	wf.write('@attribute minw3iat_div_avgw1iat numeric' + "\n" )
	wf.write('@attribute minw3iat_div_minw1iat numeric' + "\n" )
	wf.write('@attribute minw3iat_div_maxw1iat numeric' + "\n" )
	wf.write('@attribute minw3iat_div_avgw2iat numeric' + "\n" )
	wf.write('@attribute minw3iat_div_minw2iat numeric' + "\n" )
	wf.write('@attribute minw3iat_div_maxw2iat numeric' + "\n" )
	wf.write('@attribute maxw3iat_div_avgw1iat numeric' + "\n" )
	wf.write('@attribute maxw3iat_div_minw1iat numeric' + "\n" )
	wf.write('@attribute maxw3iat_div_maxw1iat numeric' + "\n" )
	wf.write('@attribute maxw3iat_div_avgw2iat numeric' + "\n" )
	wf.write('@attribute maxw3iat_div_minw2iat numeric' + "\n" )
	wf.write('@attribute maxw3iat_div_maxw2iat numeric' + "\n" )
	wf.write('@attribute minw3iat_div_maxw3iat numeric' + "\n" )
	wf.write('@attribute stdw3iat_div_stdw1iat numeric' + "\n" )
	wf.write('@attribute stdw3iat_div_stdw2iat numeric' + "\n" )
	wf.write('@attribute stdw1iat_div_stdw2iat numeric' + "\n" )
	wf.write('@attribute avgw1iat_div_avgw2iat numeric' + "\n" )
	wf.write('@attribute avgw1iat_div_minw2iat numeric' + "\n" )
	wf.write('@attribute avgw1iat_div_maxw2iat numeric' + "\n" )
	wf.write('@attribute minw1iat_div_avgw2iat numeric' + "\n" )
	wf.write('@attribute minw1iat_div_minw2iat numeric' + "\n" )
	wf.write('@attribute minw1iat_div_maxw2iat numeric' + "\n" )
	wf.write('@attribute maxw1iat_div_avgw2iat numeric' + "\n" )
	wf.write('@attribute maxw1iat_div_minw2iat numeric' + "\n" )
	wf.write('@attribute maxw1iat_div_maxw2iat numeric' + "\n" )

	wf.write('@attribute class{I   ,II  ,III ,IV  ,V   ,VI  ,VII ,VIII,IX  ,X   ,XI  ,XII ,XIII,XIV ,XV  }' + "\n" + "\n")		# c,n

	wf.write('@data' + "\n" )




	


	for i in range(len(l1)):
		#print l1[i]+l2[i]
		wf.write(l1[i][:-5] + l2[i])
#with open("all.arff","a") as wf:
	# wf.write("\n")
#	for i in range(len(l2)):
#		# print l3[i]+l4[i]
#		wf.write(l2[i])
# print len(l1), len(l2), len(l3), len(l4)
