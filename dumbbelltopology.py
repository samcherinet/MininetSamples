from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class DumbbellTopology(Topo, _delay):
    "4 hosts 4 switches."
    def build(self):
        switch_sender_access = self.addSwitch('sa1')
        switch_sender_root = self.addSwitch('sr1')
        self.addLink(switch_sender_access, switch_sender_root)
        
        switch_receiver_access = self.addSwitch('ra1')
        switch_receiver_root = self.addSwitch('rr1')
        self.addLink(switch_receiver_access,switch_receiver_root)
        
        self.addLink(switch_sender_root,switch_receiver_root,delay=_delay)
        
        host_sender_1 = self.addHost('hs1')
        self.addLink(host_sender_1, switch_sender_access)
        host_sender_2 = self.addHost('hs2')
        self.addLink(host_sender_2, switch_sender_access)
        host_receiver_1 = self.addHost('hr1')
        self.addLink(host_receiver_1, switch_receiver_access)
        host_receiver_2 = self.addHost('hr2')
        self.addLink(host_receiver_2, switch_receiver_access)
        
def runTest(_delay):
    "Create and test the network"
    topo = DumbbellTopology()
    net = Mininet(topo)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    
    s1, s2, r1, r2 = net.getNodeByName('hs1', 'hs2','hr1', 'hr2')
    
    
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # _delay='81ms',_delay='162ms'
    runTest(_delay='21ms')
