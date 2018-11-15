#!/bin/bash

# run Iperf at regular interval ( eg. run for 3 sec, after every 3 sec of sleep )

# tcpdump -i h2-eth0 -w h2 


#Flow_time=$[ ( $RANDOM % 5 )  + 1 ]


sleep 8 

iperf -c 10.0.0.12 -t212 -i1 > iperf3h11.txt


'''
iperf(){
	#x=$[ ( $RANDOM % 10 )  + 1 ]
	echo $(date) >> iperf3h2.txt
iperf3 -c 10.0.0.3 -t500 -i0.1 >> iperf3h2.txt

}

while true 
do 
	#Sleep_time=$[ ( $RANDOM % 5 )  + 1 ]
	iperf
	sleep 5
done
'''

#iperf3 -c 10.0.0.3 -t500 -i0.1 > iperf3h5.txt
