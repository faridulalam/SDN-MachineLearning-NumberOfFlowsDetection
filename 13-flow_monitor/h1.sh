#!/bin/bash

#tcpdump   -i h1-eth0   -w h1 &	# for wireshark analysis

#tcpdump   -v -i h1-eth0 '( tcp and src 10.0.0.1 and dst 10.0.0.4 and  not arp)'   > h1.txt  &


> /var/log/syslog	# to clean up previous system log files

#ovs-ofctl snoop s1 --timestamp 2> switch1_snoop &	# capture packets information using "snoop"
#ovs-ofctl snoop s4 --timestamp 2> switch4_snoop &

ovs-ofctl monitor s1 --timestamp 65534 invalid_ttl  2> switch1_monitor & # capture packets information 
ovs-ofctl monitor s4 --timestamp 65534 invalid_ttl  2> switch4_monitor & # using "monitor" (preferable)


iperf -c 10.0.0.4 -t220 -i1 > iperf3h1.txt	# start sending packets to H4 for 200 sec


