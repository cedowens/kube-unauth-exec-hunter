# Page Finder Python 3 Script

Python3 script that searches for a few interesting web pages. This script is currently hard coded to search only on port 8080, but that can easily be modified in the code.

This script works in the following way:

1. Prompts for IP range and number of threads (note: ulimit -n will show you the max number of threads currently configured on your device; that number can be increased)
2. Attempts a socket connection to hosts in the provided IP range
3. Builds a list of all hosts it was able to successfully connect to port 8080 on
4. For each host in the list (#3 above), the script searches for the following interesting pages:

-Jenkins unauthenticated script console page (/script)

-Tomcat HTML Manager page (/manager/html)

-Tomcat Text Manager page (/manager/text)

-/Console page (such as what is used by the Werkzeug debugger)

-/Command page (any interesting pages)


Usage:
-pip3 install -r requirements.txt

-python3 page-hunter.py
