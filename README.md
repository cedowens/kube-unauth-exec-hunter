# Kubernetes Node Unauthenticated Exec API Hunter

Simple python3 script to sweep a network range looking for kubernetes nodes that allow system:anonymous (unauthenticated) execution of the exec API command, which allows unauthenticated remote execution of system shell commands.

instructions:
1. pip3 install -r requirements.txt
2. python3 -W ignore kube-exec-hunter.py -r [range] -t [threads]

