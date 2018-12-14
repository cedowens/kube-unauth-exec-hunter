# Kubernetes Node Unauthenticated Exec API Hunter

Simple python3 script to sweep a network range looking for kubernetes nodes that allow system:anonymous (unauthenticated) execution of the exec API command, which allows execution of system shell commands.

instructions:
1. pip3 install -r requirements.txt
2. python3 -W ignore kube-exec-hunter.py (-W ignore will suppress the SSL/certificate warning messages for some ssl sites)

This script will look for unauthenticated access, authenticated access, and also nodes that return null PodLists (just as FYI)
