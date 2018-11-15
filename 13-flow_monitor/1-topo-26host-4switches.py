	
#!/usr/bin/python

'''
26 hosts and 4 switches (13-flow) topology to work with Pox controller

'''

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

import time

from mininet.util import dumpNodeConnections

#import webbrowser


def topology():
	"Create a network."
	net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )
	print "*** Creating Hosts"
	h1 = net.addHost( 'h1', mac = '00:00:00:00:00:01')	# h1--10.0.0.1
	h2 = net.addHost( 'h2', mac = '00:00:00:00:00:02')	# h2--10.0.0.2
	h3 = net.addHost( 'h3', mac = '00:00:00:00:00:03')	# h3--10.0.0.3
	h4 = net.addHost( 'h4', mac = '00:00:00:00:00:04')	# h4--10.0.0.4

	h5 = net.addHost( 'h5', mac = '00:00:00:00:00:05')	# h5--10.0.0.5
	h6 = net.addHost( 'h6', mac = '00:00:00:00:00:06')	# h6--10.0.0.6

	h7 = net.addHost( 'h7', mac = '00:00:00:00:00:07')	# h7--10.0.0.7
	h8 = net.addHost( 'h8', mac = '00:00:00:00:00:08')	# h8--10.0.0.8
	
	h9 = net.addHost( 'h9', mac = '00:00:00:00:00:09')	# h8--10.0.0.9
	h10 = net.addHost( 'h10', mac = '00:00:00:00:00:0A')	# h10--10.0.0.10
	
	h11 = net.addHost( 'h11', mac = '00:00:00:00:00:0B')	# h11--10.0.0.11
	h12 = net.addHost( 'h12', mac = '00:00:00:00:00:0C')	# h12--10.0.0.12
	
	h13 = net.addHost( 'h13', mac = '00:00:00:00:00:0D')	# h13--10.0.0.13
	h14 = net.addHost( 'h14', mac = '00:00:00:00:00:0E')	# h14--10.0.0.14
	
	h15 = net.addHost( 'h15', mac = '00:00:00:00:00:0F')	# h15--10.0.0.15
	h16 = net.addHost( 'h16', mac = '00:00:00:00:00:10')	# h16--10.0.0.16
	
	h17 = net.addHost( 'h17', mac = '00:00:00:00:00:11')	# h17--10.0.0.17
	h18 = net.addHost( 'h18', mac = '00:00:00:00:00:12')	# h18--10.0.0.18
	
	h19 = net.addHost( 'h19', mac = '00:00:00:00:00:13')	# h19--10.0.0.19
	h20 = net.addHost( 'h20', mac = '00:00:00:00:00:14')	# h20--10.0.0.20

	h21 = net.addHost( 'h21', mac = '00:00:00:00:00:15')	# h21--10.0.0.21
	h22 = net.addHost( 'h22', mac = '00:00:00:00:00:16')	# h22--10.0.0.22

	h23 = net.addHost( 'h23', mac = '00:00:00:00:00:17')	# h23--10.0.0.23
	h24 = net.addHost( 'h24', mac = '00:00:00:00:00:18')	# h24--10.0.0.24

	h25 = net.addHost( 'h25', mac = '00:00:00:00:00:19')	# h25--10.0.0.25
	h26 = net.addHost( 'h26', mac = '00:00:00:00:00:1A')	# h26--10.0.0.26
	
	print "*** Creating Switches & Controller"
	s1 = net.addSwitch('s1')
	s2 = net.addSwitch('s2')
	s3 = net.addSwitch('s3')
	s4 = net.addSwitch('s4')
	
	c0 = net.addController('c0', controller = RemoteController, defaultIP ='127.0.0.1',port=6633)

	# between hosts & switches
	print "*** Creating and configuring link between Hosts & Switches"
	net.addLink(h1, s1, intfName1='h1-eth0', intfName2='s1-eth1')	# h1--s1
	net.addLink(h2, s2, intfName1='h2-eth0', intfName2='s2-eth1')	# h2--s2
	net.addLink(h3, s3, intfName1='h3-eth0', intfName2='s3-eth1')	# h3--s3
	net.addLink(h4, s4, intfName1='h4-eth0', intfName2='s4-eth1')	# h4--s4

	net.addLink(h5, s2, intfName1='h5-eth0', intfName2='s2-eth4')	# h5--s2
	net.addLink(h6, s3, intfName1='h6-eth0', intfName2='s3-eth4')	# h6--s3
	
	net.addLink(h7, s2, intfName1='h7-eth0', intfName2='s2-eth5')	# h7--s2
	net.addLink(h8, s3, intfName1='h8-eth0', intfName2='s3-eth5')	# h8--s3

	net.addLink(h9, s2, intfName1='h9-eth0', intfName2='s2-eth6')	# h9--s2
	net.addLink(h10, s3, intfName1='h10-eth0', intfName2='s3-eth6')	# h10--s3
	
	net.addLink(h11, s2, intfName1='h11-eth0', intfName2='s2-eth7')	# h11--s2
	net.addLink(h12, s3, intfName1='h12-eth0', intfName2='s3-eth7')	# h12--s3
	
	net.addLink(h13, s2, intfName1='h13-eth0', intfName2='s2-eth8')	# h13--s2
	net.addLink(h14, s3, intfName1='h14-eth0', intfName2='s3-eth8')	# h14--s3
	
	net.addLink(h15, s2, intfName1='h15-eth0', intfName2='s2-eth9')	# h15--s2
	net.addLink(h16, s3, intfName1='h16-eth0', intfName2='s3-eth9')	# h16--s3
	
	net.addLink(h17, s2, intfName1='h17-eth0', intfName2='s2-eth10')	# h17--s2
	net.addLink(h18, s3, intfName1='h18-eth0', intfName2='s3-eth10')	# h18--s3
	
	net.addLink(h19, s2, intfName1='h19-eth0', intfName2='s2-eth11')	# h19--s2
	net.addLink(h20, s3, intfName1='h20-eth0', intfName2='s3-eth11')	# h20--s3

	net.addLink(h21, s2, intfName1='h21-eth0', intfName2='s2-eth12')	# h21--s2
	net.addLink(h22, s3, intfName1='h22-eth0', intfName2='s3-eth12')	# h22--s3

	net.addLink(h23, s2, intfName1='h23-eth0', intfName2='s2-eth13')	# h23--s2
	net.addLink(h24, s3, intfName1='h24-eth0', intfName2='s3-eth13')	# h24--s3

	net.addLink(h25, s2, intfName1='h25-eth0', intfName2='s2-eth14')	# h25--s2
	net.addLink(h26, s3, intfName1='h26-eth0', intfName2='s3-eth14')	# h26--s3
	
	net.addLink(s1, s2, intfName1='s1-eth2', intfName2='s2-eth2')	# s1--s2
	net.addLink(s2, s3, intfName1='s2-eth3', intfName2='s3-eth2',bw=20, delay='30ms',max_queue_size=100)	# s2--s3
	net.addLink(s3, s4, intfName1='s3-eth3', intfName2='s4-eth2')	# s3--s4

	print "\n*** Starting controller"
	net.build()
	c0.start

	print "*** Starting 4 switches"
	s1.start([c0])
	s1.cmd('switch s1 start')
	s2.start([c0])
	s2.cmd('switch s2 start')
	s3.start([c0])
	s3.cmd('switch s3 start')
	s4.start([c0])
	s4.cmd('switch s4 start')

	s1.cmd('bash forwarding_table_normal.sh')	# setting up switches forwarding table
	
	time.sleep(5)

	
	# to set tcp segmentation tso, gro, gso offloading disabled
	print "\n*** Configuring tso, gro, gso & Flowtable"
	h1.cmd('bash eth.sh')	# host1 -- gro, gso, tso off
	h4.cmd('bash eth.sh')	# host4 -- gro, gso, tso off
	h2.cmd('bash eth.sh')	# host2 -- gro, gso, tso off
	h3.cmd('bash eth.sh')	# host3 -- gro, gso, tso off
	h5.cmd('bash eth.sh')	# host5 -- gro, gso, tso off
	h6.cmd('bash eth.sh')	# host6 -- gro, gso, tso off
	h7.cmd('bash eth.sh')	# host7 -- gro, gso, tso off
	h8.cmd('bash eth.sh')	# host8 -- gro, gso, tso off
	h9.cmd('bash eth.sh')	# host9 -- gro, gso, tso off
	h10.cmd('bash eth.sh')	# host10 -- gro, gso, tso off
	h11.cmd('bash eth.sh')	# host11 -- gro, gso, tso off
	h12.cmd('bash eth.sh')	# host12 -- gro, gso, tso off
	h13.cmd('bash eth.sh')	# host13 -- gro, gso, tso off
	h14.cmd('bash eth.sh')	# host14 -- gro, gso, tso off
	h15.cmd('bash eth.sh')	# host15 -- gro, gso, tso off
	h16.cmd('bash eth.sh')	# host16 -- gro, gso, tso off
	h17.cmd('bash eth.sh')	# host17 -- gro, gso, tso off
	h18.cmd('bash eth.sh')	# host18 -- gro, gso, tso off
	h19.cmd('bash eth.sh')	# host19 -- gro, gso, tso off
	h20.cmd('bash eth.sh')	# host20 -- gro, gso, tso off
	h21.cmd('bash eth.sh')	# host21 -- gro, gso, tso off
	h22.cmd('bash eth.sh')	# host22 -- gro, gso, tso off
	h23.cmd('bash eth.sh')	# host23 -- gro, gso, tso off
	h24.cmd('bash eth.sh')	# host24 -- gro, gso, tso off
	h25.cmd('bash eth.sh')	# host25 -- gro, gso, tso off
	h26.cmd('bash eth.sh')	# host26 -- gro, gso, tso off
	time.sleep(2)
	s1.cmd('bash eth.sh')	# switch1 -- gro, gso, tso off
	s2.cmd('bash eth.sh')	# switch2 -- gro, gso, tso off
	s3.cmd('bash eth.sh')	# switch3 -- gro, gso, tso off
	s4.cmd('bash eth.sh')	# switch4 -- gro, gso, tso off
	time.sleep(2)
	s2.cmd('bash reno.sh')		# setting tcp RENO, window_scalling on, maximum receiver buffer
	time.sleep(2)
	# StopWatch website to open
	# webbrowser.open('http://timer-tab.com/', new = 0)

	print "*** Dumping Host Connections"
	dumpNodeConnections(net.hosts)


	print "*** Ping : Checking connectivity"
	#net.pingAll()
	
	time.sleep(2)
	
	print "*** Start transfering data"
	h4.cmd('./h4.sh &')
	h3.cmd('./host.sh &')
	h6.cmd('./host.sh &')
	h8.cmd('./host.sh &')
	h10.cmd('./host.sh &')
	h12.cmd('./host.sh &')
	h14.cmd('./host.sh &')
	h16.cmd('./host.sh &')
	h18.cmd('./host.sh &')
	h20.cmd('./host.sh &')
	h22.cmd('./host.sh &')
	h24.cmd('./host.sh &')
	h26.cmd('./host.sh &')
	h1.cmd('./h1.sh &')
	h2.cmd('./h2.sh &')
	h5.cmd('./h5.sh &')
	h7.cmd('./h7.sh &')
	h9.cmd('./h9.sh &')
	h11.cmd('./h11.sh &')
	h13.cmd('./h13.sh &')
	h15.cmd('./h15.sh &')
	h17.cmd('./h17.sh &')
	h19.cmd('./h19.sh &')
	h21.cmd('./h21.sh &')
	h23.cmd('./h23.sh &')
	h25.cmd('./h25.sh &')
	'''
	# h1.cmd('h1 ping h2 -c 2')

	# h2.cmd('tcpdump -i h2-eth2 -w server-tcpdump')
	# h1.cmd('tcpdump -i h1-eth2 -w client-tcpdump')
	# h2.cmd('iperf -s > server_output.txt &')
	# h1.cmd('iperf -c ', h1.IP() + ' -i 1 -t 50   >  client_output.txt &')
	'''
	print "*** Running CLI"
	CLI( net )
	print "*** Stopping network"
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	topology()



















	
