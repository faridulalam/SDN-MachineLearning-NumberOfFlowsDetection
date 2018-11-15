#!/bin/bash

"""Switch S1 and S4 are being used to take packets information.........
This is why only these 2 switches are configured as dump switches. Therefore,
each and every packets should travel to controller and as a results all packets
information can be observed.

Switch S2 and S3 are being used to forward others flows and this is why 
these two switches are automatic"""


from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str # dpidstr
from pox.lib.util import str_to_bool
from pox.lib.addresses import EthAddr, IPAddr

import time

log = core.getLogger()
_flood_delay = 0


class LearningSwitch (object):
  log.info('alam_pox.py is running')

  def __init__ (self, connection, transparent):
    # Switch we'll be adding L2 learning switch capabilities to
    self.connection = connection	# Switch we'll be adding L2 learning switch capabilities to connection and transparent
    self.transparent = transparent	# to keep track of the connection to the switch so that we can send it messages!
    connection.addListeners(self)	# listen to the connection for packetIN msg


  def _handle_PacketIn (self, event):	# Handle packet in messages from the switch
  
    packet = event.parsed		# parsed/analyze packet data
    dpidstr = dpid_to_str(event.dpid)	# dpidstr - Convert a DPID from a long into the canonical string form
					# basically indicates switch address

    ######### for SWITCH 1 ############ 
    if dpidstr=="00-00-00-00-00-01":	# if switch address is this one
        fm = of.ofp_flow_mod()		# Set fields to match received packet
        fm.match.in_port = 1		# match if packet-in msg from port 1
        fm.priority = 33001	#	# # The priority at which a wildcarded entry will match in comparison to others
        fm.match.dl_type = 0x0800	# specifies that field must match the value
        fm.match.nw_src = IPAddr("10.0.0.1")	# match with source IP address
        fm.match.nw_dst = IPAddr("10.0.0.2")	# match with destination IP address
        fm.actions.append(of.ofp_action_output( port = of.OFPP_CONTROLLER ) )	# Add an action to send controller port
        fm.actions.append(of.ofp_action_output( port = 2 ) )			# Add an action to send data through port
        event.connection.send( fm )	# send an OpenFlow message to a switch

        fm = of.ofp_flow_mod()
        fm.match.in_port = 2
        fm.priority = 33001
        fm.match.dl_type = 0x0800
        fm.match.nw_src = IPAddr("10.0.0.2")
        fm.match.nw_dst = IPAddr("10.0.0.1")
        fm.actions.append(of.ofp_action_output( port = 1 ) )
        event.connection.send( fm )
	
	
    ########## for SWITCH 4 ############ 
    if dpidstr=="00-00-00-00-00-04":
        fm = of.ofp_flow_mod()
        fm.match.in_port = 2
        fm.priority = 33001
        fm.match.dl_type = 0x0800
        fm.match.nw_src = IPAddr("10.0.0.1")
        fm.match.nw_dst = IPAddr("10.0.0.2")
        fm.actions.append(of.ofp_action_output( port = of.OFPP_CONTROLLER ) )
        fm.actions.append(of.ofp_action_output( port = 1 ) )
        event.connection.send( fm )

        fm = of.ofp_flow_mod()
        fm.match.in_port = 1
        fm.priority = 33001
        fm.match.dl_type = 0x0800
        fm.match.nw_src = IPAddr("10.0.0.2")
        fm.match.nw_dst = IPAddr("10.0.0.1")
        fm.actions.append(of.ofp_action_output( port = 2) )
        event.connection.send( fm )


class l2_learning (object):


  def __init__ (self, transparent):
    core.openflow.addListeners(self)
    self.transparent = transparent

  def _handle_ConnectionUp (self, event):
    log.debug("Connection %s" % (event.connection,))
    LearningSwitch(event.connection, self.transparent)


def launch (transparent=False, hold_down=_flood_delay):
  """
  Starts an L2 learning switch.
  """
  try:
    global _flood_delay
    _flood_delay = int(str(hold_down), 10)
    assert _flood_delay >= 0
  except:
    raise RuntimeError("Expected hold-down to be a number")

  core.registerNew(l2_learning, str_to_bool(transparent))
