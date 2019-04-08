from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink
import time
from subprocess import Popen, PIPE

class DumbbellTopology(Topo):
     #"4 hosts 4 switches."
     def build(self, _delay, **_kwargs):
        print 'printing the paramter delay ' + _delay
        switch_sender_access = self.addSwitch('sa1'+_delay)
        switch_sender_root = self.addSwitch('sr1'+_delay)
        self.addLink(switch_sender_access, switch_sender_root)

        switch_receiver_access = self.addSwitch('ra1'+_delay)
        switch_receiver_root = self.addSwitch('rr1'+_delay)
        self.addLink(switch_receiver_access,switch_receiver_root)

        self.addLink(switch_sender_root,switch_receiver_root,bw=10, delay=_delay)

        host_sender_1 = self.addHost('hs1'+_delay)
        self.addLink(host_sender_1, switch_sender_access)
        host_sender_2 = self.addHost('hs2'+_delay)
        self.addLink(host_sender_2, switch_sender_access)
        host_receiver_1 = self.addHost('hr1'+_delay)
        self.addLink(host_receiver_1, switch_receiver_access)
        host_receiver_2 = self.addHost('hr2'+_delay)
        self.addLink(host_receiver_2, switch_receiver_access)
        
def runTest(_delay='21ms',_port=5566):
    print 'running test for a delay of ' + _delay
    
    "Create and test the network"
    topo = DumbbellTopology(_delay)
    net = Mininet(topo, link=TCLink)
    net.start()
    
    print "Dumping host connections for "+_delay
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity for "+_delay
    
    s1, s2, r1, r2 = net.getNodeByName('hs1'+_delay, 'hs2'+_delay,'hr1'+_delay, 'hr2'+_delay)
    
    #start server on recievers
    serverArg = 'iperf3 -s -p '+_port+' -i 1'
    r1.sendCmd(serverArg)
    r2.sendCmd(serverArg)
    
    print serverArg
    
    #simulate message from senders 15 apart
    #from s1 to r1'
    client1Arg = 'iperf3 -c ' + r1.IP() + ' -p '+_port+' -t 15 -i .1 -J > '+_delay+'_s1r1.json' 
    #add delay
    #config algorithm
    s1.sendCmd(client1Arg)
    print client1Arg
    
    #wait 15 minutes
    #from s2 to r2
    time.sleep(5)
    client2Arg = 'iperf3 -c ' + r2.IP() + ' -p '+_port+' -t 15 -i .1 -J > '+_delay+'_s2r2.json'
    #add delay
    #config algorithm
    s2.sendCmd(client2Arg)
    print client2Arg

    return net
    #CLI(net)

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # _delay='81ms',_delay='162ms'
    net1 = runTest('21ms',5566)
    net2 = runTest('81ms',5567)
    net3 = runTest('162ms',5568)
    
    #wait for 20 minute to finish testing
    t = 0
    while t < 30 :
        t += 1
        time.sleep(1)
        print t+' of 30 seconds left'
    
    Popen("killall -9 top bwm-ng", shell=True).wait()
    net1.stop()
    net2.stop()
    net3.stop()
    
