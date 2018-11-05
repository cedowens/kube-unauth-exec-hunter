# Devtools LFI Finder Python 3 Script

Python3 script that searches for LFI vulnerabilities in the versions_redirect_url parameter on devtools hosts running web servers on port 90.

This script works in the following way:

1. Prompts for IP range and number of threads (note: ulimit -n will show you the max number of threads currently configured on your device; that number can be increased)
2. Attempts a socket connection to hosts in the provided IP range
3. Builds a list of all hosts it was able to successfully connect to port 8080 on
4. For each host in the list (#3 above), the script searches for the /var/log/httpd/access_log file to see if it is injectable:

Usage:
-pip3 install -r requirements.txt

-python3 devtools-lfi-checker.py
