from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=20):
        switch_sender_access = self.addSwitch('sa1')
        switch_sender_root = self.addSwitch('sr1')
        self.addLink(switch_sender_access, switch_sender_root)
        
        switch_receiver_access = self.addSwitch('ra1')
        switch_receiver_root = self.addSwitch('rr1')
        self.addLink(switch_receiver_access,switch_receiver_root)
        
        self.addLink(switch_sender_root,switch_receiver_root)
        
        host_sender_1 = self.addHost('hs1')
        self.addLink(host_sender_1, switch_sender_access)
        host_sender_2 = self.addHost('hs2')
        self.addLink(host_sender_2, switch_sender_access)
        host_receiver_1 = self.addHost('hr1')
        self.addLink(host_receiver_1, switch_receiver_access)
        host_receiver_2 = self.addHost('hr2')
        self.addLink(host_receiver_2, switch_receiver_access)
        
def simpleTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=20)
    net = Mininet(topo)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
