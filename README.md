# Red Team SMB Password Checker (Single Host)

Simple python script to to check a username and password combination over smb on a given host. 

In AD environments, be careful running this script to ensure you do not cause lockouts by running multiple checks using a single domain username.

Usage: python3 smb-single-test.py

for domain joined systems, you can enter the domain or leave it blank when prompted (either will work).

