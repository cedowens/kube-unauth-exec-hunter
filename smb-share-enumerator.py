import sys
import smb
from smb.SMBConnection import SMBConnection
from optparse import OptionParser
import getpass
import threading
import socket
from queue import Queue
import ipaddress
from ipaddress import IPv4Address, IPv4Network

if (len(sys.argv) < 5 and '-h' not in sys.argv):
    print("Not enough arguments. Usage: %s -t -u -d" % sys.argv[0])
    print("Try %s -h for help menu" % sys.argv[0])
    sys.exit(1)

parser = OptionParser()
parser.add_option("-r", "--range", help="IP range to check")
parser.add_option("-u", "--username", help="Username that will be used for authentication")
parser.add_option("-d", "--domain", help="Domain name that will be used for authentication")
parser.add_option("-t", "--threads", help="Number of threads to use")
(options, args) = parser.parse_args()
passwd = getpass.getpass('Ener password to use :: ')
    
iplist = []
portopenlist = []

def Connector(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        result = sock.connect_ex((str(ip),445))
        sock.close()
        if result == 0:
            print("\033[92mPort 445 OPEN on %s\033[0m" % str(ip))
            portopenlist.append(ip)
        
    except Exception as e:
        print(e)

def threader():
    while True:
        worker = q.get()
        Connector(worker)
        q.task_done()

def SmbCheck(ip):
    try:
        conn = SMBConnection(options.username, passwd, 'enumerator', ip, options.domain, use_ntlm_v2=True, is_direct_tcp=True)
        connected = conn.connect(ip,445)
        if connected:
            try:
                response = conn.listShares(timeout=30)
                for i in range(len(response)):
                    try:
                        response2 = conn.listPath(response[i].name,'/',timeout=30)
                        print('------->Listing of ' + ip + ' on share:',response[i].name)
                        for i in range(len(response2)):
                            print("*", response2[i].filename)
                    except:
                        pass
            except:
                pass
        
    except:
        pass

def threader2():
    while True:
        worker2 = q2.get()
        SmbCheck(worker2)
        q2.task_done()


q = Queue()

for ip in ipaddress.IPv4Network(options.range):
    iplist.append(str(ip))

for worker in iplist:
    q.put(worker)

for x in range(int(options.threads)):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

q.join()
       
q2 = Queue()

for worker2 in portopenlist:
    item = str(worker2)
    q2.put(item)

for y in range(int(options.threads)):
    t2 = threading.Thread(target=threader2)
    t2.daemon = True
    t2.start()

q2.join()

print("+"*50)
print("DONE!")
print("+"*50)
