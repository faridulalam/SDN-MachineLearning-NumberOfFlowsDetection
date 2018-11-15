#!/bin/bash

######## 4switches 20hosts (10-flow) ethtool configuration ##########

"""
To enhance the performance of a TCP connection.... the operating system can offload
TCP functionality in the network interface card of packet segmentation such as

1. generic segmentation (gso)
2. generic receive (gro)
3. TCP segmentation (tso)
 
Disabling these functions with ethtool -K command will enable inspecting individual 
packets using tcpdump and simple wireshark tools. These setting are implemented on 
every interface of each host and switch in the topology.
"""

### HOST 1 ###
ethtool -K h1-eth0 gro off
ethtool -K h1-eth0 gso off
ethtool -K h1-eth0 tso off

### HOST 2 ###
ethtool -K h2-eth0 gro off
ethtool -K h2-eth0 gso off
ethtool -K h2-eth0 tso off

### HOST 3 ###
ethtool -K h3-eth0 gro off
ethtool -K h3-eth0 gso off
ethtool -K h3-eth0 tso off

### HOST 4 ###
ethtool -K h4-eth0 gro off
ethtool -K h4-eth0 gso off
ethtool -K h4-eth0 tso off

### HOST 5 ###
ethtool -K h5-eth0 gro off
ethtool -K h5-eth0 gso off
ethtool -K h5-eth0 tso off

### HOST 6 ###
ethtool -K h6-eth0 gro off
ethtool -K h6-eth0 gso off
ethtool -K h6-eth0 tso off

### HOST 7 ###
ethtool -K h7-eth0 gro off
ethtool -K h7-eth0 gso off
ethtool -K h7-eth0 tso off

### HOST 8 ###
ethtool -K h8-eth0 gro off
ethtool -K h8-eth0 gso off
ethtool -K h8-eth0 tso off

### HOST 9 ###
ethtool -K h9-eth0 gro off
ethtool -K h9-eth0 gso off
ethtool -K h9-eth0 tso off

### HOST 10 ###
ethtool -K h10-eth0 gro off
ethtool -K h10-eth0 gso off
ethtool -K h10-eth0 tso off

### HOST 11 ###
ethtool -K h11-eth0 gro off
ethtool -K h11-eth0 gso off
ethtool -K h11-eth0 tso off

### HOST 12 ###
ethtool -K h12-eth0 gro off
ethtool -K h12-eth0 gso off
ethtool -K h12-eth0 tso off

### HOST 13 ###
ethtool -K h13-eth0 gro off
ethtool -K h13-eth0 gso off
ethtool -K h13-eth0 tso off

### HOST 14 ###
ethtool -K h14-eth0 gro off
ethtool -K h14-eth0 gso off
ethtool -K h14-eth0 tso off

### HOST 15 ###
ethtool -K h15-eth0 gro off
ethtool -K h15-eth0 gso off
ethtool -K h15-eth0 tso off

### HOST 16 ###
ethtool -K h16-eth0 gro off
ethtool -K h16-eth0 gso off
ethtool -K h16-eth0 tso off

### HOST 17 ###
ethtool -K h17-eth0 gro off
ethtool -K h17-eth0 gso off
ethtool -K h17-eth0 tso off

### HOST 18 ###
ethtool -K h18-eth0 gro off
ethtool -K h18-eth0 gso off
ethtool -K h18-eth0 tso off

### HOST 19 ###
ethtool -K h19-eth0 gro off
ethtool -K h19-eth0 gso off
ethtool -K h19-eth0 tso off

### HOST 20 ###
ethtool -K h20-eth0 gro off
ethtool -K h20-eth0 gso off
ethtool -K h20-eth0 tso off

### HOST 21 ###
ethtool -K h21-eth0 gro off
ethtool -K h21-eth0 gso off
ethtool -K h21-eth0 tso off

### HOST 22 ###
ethtool -K h22-eth0 gro off
ethtool -K h22-eth0 gso off
ethtool -K h22-eth0 tso off

### HOST 23 ###
ethtool -K h23-eth0 gro off
ethtool -K h23-eth0 gso off
ethtool -K h23-eth0 tso off

### HOST 24 ###
ethtool -K h24-eth0 gro off
ethtool -K h24-eth0 gso off
ethtool -K h24-eth0 tso off

### HOST 25 ###
ethtool -K h25-eth0 gro off
ethtool -K h25-eth0 gso off
ethtool -K h25-eth0 tso off

### HOST 26 ###
ethtool -K h26-eth0 gro off
ethtool -K h26-eth0 gso off
ethtool -K h26-eth0 tso off

### SWITCH 1 ###
ethtool -K s1-eth1 gro off
ethtool -K s1-eth1 gso off
ethtool -K s1-eth1 tso off
ethtool -K s1-eth2 gro off
ethtool -K s1-eth2 gso off
ethtool -K s1-eth2 tso off
ethtool -K s1-eth3 gro off
ethtool -K s1-eth3 gso off
ethtool -K s1-eth3 tso off
ethtool -K s1-eth4 gro off
ethtool -K s1-eth4 gso off
ethtool -K s1-eth4 tso off

### SWITCH 2 ###
ethtool -K s2-eth1 gro off
ethtool -K s2-eth1 gso off
ethtool -K s2-eth1 tso off
ethtool -K s2-eth2 gro off
ethtool -K s2-eth2 gso off
ethtool -K s2-eth2 tso off
ethtool -K s2-eth3 gro off
ethtool -K s2-eth3 gso off
ethtool -K s2-eth3 tso off
ethtool -K s2-eth4 gro off
ethtool -K s2-eth4 gso off
ethtool -K s2-eth4 tso off
ethtool -K s2-eth5 gro off
ethtool -K s2-eth5 gso off
ethtool -K s2-eth5 tso off
ethtool -K s2-eth6 gro off
ethtool -K s2-eth6 gso off
ethtool -K s2-eth6 tso off
ethtool -K s2-eth7 gro off
ethtool -K s2-eth7 gso off
ethtool -K s2-eth7 tso off
ethtool -K s2-eth8 gro off
ethtool -K s2-eth8 gso off
ethtool -K s2-eth8 tso off
ethtool -K s2-eth9 gro off
ethtool -K s2-eth9 gso off
ethtool -K s2-eth9 tso off
ethtool -K s2-eth10 gro off
ethtool -K s2-eth10 gso off
ethtool -K s2-eth10 tso off
ethtool -K s2-eth11 gro off
ethtool -K s2-eth11 gso off
ethtool -K s2-eth11 tso off
ethtool -K s2-eth12 gro off
ethtool -K s2-eth12 gso off
ethtool -K s2-eth12 tso off
ethtool -K s2-eth13 gro off
ethtool -K s2-eth13 gso off
ethtool -K s2-eth13 tso off
ethtool -K s2-eth14 gro off
ethtool -K s2-eth14 gso off
ethtool -K s2-eth14 tso off

### SWITCH 3 ###
ethtool -K s3-eth1 gro off
ethtool -K s3-eth1 gso off
ethtool -K s3-eth1 tso off
ethtool -K s3-eth2 gro off
ethtool -K s3-eth2 gso off
ethtool -K s3-eth2 tso off
ethtool -K s3-eth3 gro off
ethtool -K s3-eth3 gso off
ethtool -K s3-eth3 tso off
ethtool -K s3-eth4 gro off
ethtool -K s3-eth4 gso off
ethtool -K s3-eth4 tso off
ethtool -K s3-eth5 gro off
ethtool -K s3-eth5 gso off
ethtool -K s3-eth5 tso off
ethtool -K s3-eth6 gro off
ethtool -K s3-eth6 gso off
ethtool -K s3-eth6 tso off
ethtool -K s3-eth7 gro off
ethtool -K s3-eth7 gso off
ethtool -K s3-eth7 tso off
ethtool -K s3-eth8 gro off
ethtool -K s3-eth8 gso off
ethtool -K s3-eth8 tso off
ethtool -K s3-eth9 gro off
ethtool -K s3-eth9 gso off
ethtool -K s3-eth9 tso off
ethtool -K s3-eth10 gro off
ethtool -K s3-eth10 gso off
ethtool -K s3-eth10 tso off
ethtool -K s3-eth11 gro off
ethtool -K s3-eth11 gso off
ethtool -K s3-eth11 tso off
ethtool -K s3-eth12 gro off
ethtool -K s3-eth12 gso off
ethtool -K s3-eth12 tso off
ethtool -K s3-eth13 gro off
ethtool -K s3-eth13 gso off
ethtool -K s3-eth13 tso off
ethtool -K s3-eth14 gro off
ethtool -K s3-eth14 gso off
ethtool -K s3-eth14 tso off

### SWITCH 4 ###
ethtool -K s4-eth1 gro off
ethtool -K s4-eth1 gso off
ethtool -K s4-eth1 tso off
ethtool -K s4-eth2 gro off
ethtool -K s4-eth2 gso off
ethtool -K s4-eth2 tso off
ethtool -K s4-eth3 gro off
ethtool -K s4-eth3 gso off
ethtool -K s4-eth3 tso off
ethtool -K s4-eth4 gro off
ethtool -K s4-eth4 gso off
ethtool -K s4-eth4 tso off

