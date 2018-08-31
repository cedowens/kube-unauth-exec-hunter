# Windows SMB Share Enumerator

Python3 script that allows you to quickly check what Windows shares and systems you have access to with a set of AD credentials. This script sweeps a subnet for hosts with port 445 open, and then checks to see if the provided credentials can view any shares. If so, it will list out the shares it can enumerate.

Since this script uses threading to run faster, you must first check the ulimit set on your host.

You can check the limit of the number of open file handles on your system by running:

ulimit -n

For Mac this number is often around 250. On Kali and other Linux distros this number is usually 1000+.

Since this is opens connections to ports and IPs concurrently, you'll need to set your thread number when promped accordingly.

Generally, I would recommend setting threads to 250 on Mac systems and 1000 on Kali or other Linux distros unless you follow the steps below to up the ulimit cap on your system.

first run pip3 install -r requirements.txt

-------------------------

Usage:

python3 smb-enumerator.py -r [IPBLOCK] -u [USERNAME] -d [DOMAIN] -t [THREADS]

The enter password when prompted.


-------------------------

STEPS TO PERSISTENTLY INCREASE ulimit on Mac and Linux to allow for more threads:

https://unix.stackexchange.com/questions/108174/how-to-persistently-control-maximum-system-resource-consumption-on-mac

------------------------

DISCLAIMER

Use at your own risk. Do not use without the appropriate authorizations.

