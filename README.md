# Simple Powershell One-Liners

Listing of some basic and useful powershell one liners:

-Dump all active AD user accounts and show their username (samaccoutname), first name (GivenName), last name (Surname), email address (mail), and title (title):
Get-ADUser -Filter ("Enabled -eq 'True'") -Properties samaccountname,GivenName,Surname,mail,title | Select-Object samaccountname,GivenName,Surname,mail,title | export-csv <path to csv>

-Dump all computers in AD and show the server name, OS, Location, IP Address, and lastlogondate fields:
Get-ADComputer -Filter * -Properties Name,OperatingSystem,Location,IPv4Address,lastlogondate | Select-Object Name,OperatingSystem,Location,IPv4Address,lastlogondate | export-csv <path to csv>

-List all domain controllers via powershell:
Get-ADDomainController -Filter * | Select-Object Name

