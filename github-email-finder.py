import requests
import re

domain = input("Enter domain: ").strip()
partition = domain.partition('.')
company = partition[0]

maingithub = "https://github.com/%s" % company

githubpeople = "https://github.com/orgs/%s/people" % company

response = requests.get(maingithub)
response_text = response.text

response2 = requests.get(githubpeople)
response2_text = response2.text

listofusers = re.findall(r'itemprop="name">[a-zA-Z0-9\-]{3,}<',response2_text)
listofusers2 = [each.replace('>', '').replace('<', '').replace('"name"', '').replace('=', '').replace('itemprop', '') for each in listofusers]

print('+'*50)
print("\033[33mList of github user pages in company %s:\033[0m" % domain)
for user in listofusers2:
    userpage = "https://github.com/%s" % user
    print(userpage)

print('+'*50)

print("\033[33mList of your company email addresses harvested from %s github user pages:\033[0m" % domain)
for user in listofusers2:
    userpage = "https://api.github.com/users/%s/events/public" % user
    response3 = requests.get(userpage)
    response3_text = response3.text
    findemail = re.findall(r'[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+', response3_text)
    emailset = set(findemail)
    for each in emailset:
        if domain in each:
            print(each)

print("\033[33mList of company email addresses found from duckduckgo search:\033[0m:")
searchurl = 'https://duckduckgo.com/html/?q=site%3Alinkedin.com+email+%40%22' + domain
webresponse = requests.get(searchurl)
webresponse2 = webresponse.text
findemail2 = re.findall(r'[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+', webresponse2)
emailset2 = set(findemail2)
for each in emailset2:
    if domain in each:
        print(each)
