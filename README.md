# Red/Blue Team Gobbler Reconnaissance Tool

Gobbler is a python script that automates some of the initial data gethering steps during reconnaissance. To run Gobbler, you feed it a domain when prompted. 

For additinoal data gathering, you can enter a shodan API key when prompted, and it will search shodan, format the results, and write to a file.

Gobbler gathers data such as:
-all ASN numbers for the domain searched
-public facing IP blocks directly assigned to the domain you enter
-dns NS, TXT, and MX records (good info can be gleaned from these such as where mail is hosted, if docusign or azure is used, etc.)
-hosts of interest (login pages)
-data seen by Shodan for the ASN 

gobbler pulls the ASN information from mxtoolbox.com's ASN lookup, which I use frequently when searching ASN info for a domain.

gobbler uses some libraries not included in the Python standard library, so first run:
pip3 install -r requirements.txt

Usage: "python3 gobbler.py" and enter in the domain to search along with your shodan API key when prompted for additional data.



