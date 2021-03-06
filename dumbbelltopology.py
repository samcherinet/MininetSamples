from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink
import time
import sys
from subprocess import Popen, PIPE

class DumbbellTopology(Topo):
    "4 hosts 4 switches."
    def build(self, d, **_kwargs):
        switch_sender_access = self.addSwitch('sa1')
        switch_sender_root = self.addSwitch('sr1')
        self.addLink(switch_sender_access
                    , switch_sender_root
                    , max_queue_size = 50
                    , bw = 250)
        
        switch_receiver_access = self.addSwitch('ra1')
        switch_receiver_root = self.addSwitch('rr1')
        self.addLink(switch_receiver_access
                    , switch_receiver_root
                    , max_queue_size = 50
                    , bw = 250)
        
        self.addLink(switch_sender_root,switch_receiver_root,bw=960, delay=d)
        
        host_sender_1 = self.addHost('hs1')
        self.addLink(host_sender_1, switch_sender_access,bw=960)
        host_sender_2 = self.addHost('hs2')
        self.addLink(host_sender_2, switch_sender_access,bw=960)
        host_receiver_1 = self.addHost('hr1')
        self.addLink(host_receiver_1, switch_receiver_access,bw=960)
        host_receiver_2 = self.addHost('hr2')
        self.addLink(host_receiver_2, switch_receiver_access,bw=960)
        
def runTest(d='21ms',alg='RENO',l=100):
    "Create and test the network"
    topo = DumbbellTopology(d=d)
    net = Mininet(topo, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    
    s1, s2, r1, r2 = net.getNodeByName('hs1', 'hs2','hr1', 'hr2')
    
    #start server on recievers
    serverArg = 'iperf3 -s -p 5566 -i 1'
    r1.sendCmd(serverArg)
    time.sleep(2)
    r2.sendCmd(serverArg)
    
    print serverArg
    
    #simulate message from senders 15 apart
    #from s1 to r1'
    client1Arg = 'iperf3 -c ' + r1.IP() + ' -p 5566 -t '+str(l)+' -i .2 -C '+alg+' -J > s1r1_'+d+'_'+alg+'.json' 
    #add delay
    #config algorithm
    s1.sendCmd(client1Arg)
    print client1Arg
    
    #wait 15 minutes
    #from s2 to r2
    time.sleep(int(float(l)*.25))
    print 'starting the second send'
    client2Arg = 'iperf3 -c ' + r2.IP() + ' -p 5566 -t '+str(int(float(l)*.75))+' -i .2 -C '+alg+' -J > s2r2_'+d+'_'+alg+'.json'
    #add delay
    #config algorithm
    s2.sendCmd(client2Arg)
    print client2Arg
        
    #wait for 20 minute to finish testing
    t = 0
    while t < int(float(l)*.75) :
        t += 1
        print str(t) + ' seconds completed'
        time.sleep(1)
    
    #CLI(net)
    #Popen("killall -9 iperf3", shell=True).wait()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # _delay='81ms',_delay='162ms'
    runTest(d=sys.argv[1],alg=sys.argv[2],l=sys.argv[3])
