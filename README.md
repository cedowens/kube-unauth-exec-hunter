# Red Team Threaded Port Sweeper

Threaded python3 script to sweep across an IP block and see what hosts have a specified port open.check whether a socket connection can be established to a given port on each host within an IP range. 

Each IP address in the block is counted and the corresponding number of threads is created and run concurrently.

Results are written to a file named "outfile.txt" in the current directory.

Usage: python3 threaded-portsweepr.py

You can check the limit of the number of open file handles on your system by running:

ulimit -n

For Mac this number is often around 250. On Kali and other Linux distros this number is usually 1000+.

Since this is opens connections to ports and IPs concurrently, you'll need to set your thread number when promped accordingly.

Generally, I would recommend setting it to 250 on Mac systems and 1000 on Kali or other Linux distros.

------------------------

If you want to persistently up the ulimit on your host so that you can run more threads and complete the sweep faster, instructions are here:

https://unix.stackexchange.com/questions/108174/how-to-persistently-control-maximum-system-resource-consumption-on-mac

------------------------
DISCLAIMER

Use at your own risk. Do not use without the appropriate authorizations.
