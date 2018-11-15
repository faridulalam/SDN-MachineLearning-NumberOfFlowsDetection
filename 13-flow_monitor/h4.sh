#!/bin/bash

#tcpdump   -i h4-eth0  -w h4 &

#tcpdump   -v -i h4-eth0 '(tcp and src 10.0.0.1 and dst 10.0.0.4 and  not arp)'  > h4.txt  &

#tcpdump -vvv -ttt -i h4-eth0 src 10.0.0.1 and dst 10.0.0.4 and greater 28  > h4Delta.txt  &

iperf -s
