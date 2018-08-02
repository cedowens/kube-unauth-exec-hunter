# Red Team Threaded Port Scanner

Python3 script that uses a queue and threads to concurrently scan the top 1000 most commonly used tcp ports on an IP range.

You can check the limit of the number of open file handles on your system by running:

ulimit -n

For Mac this number is often around 250. On Kali and other Linux distros this number is usually 1000+.

Since this is opens connections to ports and IPs concurrently, you'll need to set your thread number when promped accordingly.

Generally, I would recommend setting it to 250 on Mac systems and 1000 on Kali or other Linux distros.

On average it takes about 8 mins on Mac to scan the top 1000 ports on a /24 netblock.

On average it takes about 2 mins on Kali to scan the top 1000 ports on a /24 netblock.

Usage: 

python3 portscanner.py 

The enter IP block and thread count when prompted.

All hosts with open ports are written to a file in the current working directory named "scanresults.txt"

-------------------------------------------

DISCLAIMER

Use at your own risk. Do not use without the appropriate authorizations.

