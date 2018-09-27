import datetime
import sys

writedate = datetime.datetime.now().strftime("%Y-%m-%d-%H_%M")

outfile = open('phish-difficulty-score-%s.txt' %writedate,'w')
outfile.write("Phishing difficulty score output file\n")
outfile.write("\n")
outfile.write("Timestamp of this file: ")
outfile.write(writedate)
outfile.write("\n")
outfile.write("-"*40)
outfile.write("\n")

print("-"*50)
print("Phishing exercise difficulty scoring script.")
print("-"*50)
print("Answer the following questions to get a difficulty rating for your phishing exercise:")
print("#######")

print("Select the type of phishing email campaign used:")
print("--->1: Credential harvesting campaign.")
print("--->2: Attachment-based campaign.")
print("--->3: Email with a link to a malicious payload.")
print("--->4: Business Email Compromise (BEC) email campaign.")
emailtype = input("Enter answer: ").strip()
outfile.write(emailtype)
if emailtype == '1':
    outfile.write(": Credential harvesting campaign.")
elif emailtype == '2':
    outfile.write(": Attachment-based campaign.")
elif emailtype == '3':
    outfile.write(": Email with a link to a malicious payload.")
elif emailtype == '4':
    outfile.write(": Business Email Compromise (BEC) email campaign.")
else:
    print("Invalid selection...exiting")
    sys.exit(1)

outfile.write("\n")

print("1. How was the sending email address crafted??")
print("--->1: Email sender is generic and not related to the email theme or a company name (ex: no-reply@<domain.com>).")
print("--->2: Email sender is relevant to the email theme but not related to a company name (ex: shippingadmin@<domain.com>).")
print("--->3: Email sender is relevant to the email theme and is related to a company name (ex: fedexadmin@<domain.com>).")
ans1 = input("Enter answer: ").strip()


if ans1 == '1':
    outfile.write("--->1: Email sender is generic and not related to the email theme or a company name (ex: no-reply@<domain.com>).")
elif ans1 == '2':
    outfile.write("--->2: Email sender is relevant to the email theme but not related to a company name (ex: shippingadmin@<domain.com>).")
elif ans1 == '3':
    outfile.write("--->3: Email sender is relevant to the email theme and is related to a company name (ex: fedexadmin@<domain.com>).")
else:
    print("Invalid selection...exiting")
    sys.exit(1)

ans1val = int(ans1)*int(40/3)

outfile.write("\n")
print("2. What type of domain did you use to send the mail??")
print("--->1: Domain has no relevance at all to the email theme or to a real company name.")
print("--->2: Domain is relevant to the email theme but does not mimic a company name.")
print("--->3: Domain is not relevant to the email theme but mimics a company name.")
print("--->4: Domain is relevant to the email theme and mimics a company name.")
ans2 = input("Enter answer: ").strip()


if ans2 == '1':
    outfile.write("--->1: Domain has no relevance at all to the email theme or to a real company name.")
elif ans2 == '2':
    outfile.write("--->2: Domain is relevant to the email theme but does not mimic a company name.")
elif ans2 == '3':
    outfile.write("--->3: Domain is not relevant to the email theme but mimics a company name.")
elif ans2 == '4':
    outfile.write("--->4: Domain is relevant to the email theme and mimics a company name.")
else:
    print("Invalid selection...exiting")
    sys.exit(1)

ans2val = int(ans2)*int(80/4)
    
outfile.write("\n")

print("3. What type of domain did you use for C2 or the fake login page??")
print("--->1: Domain has no relevance at all to the email theme or to a real company name.")
print("--->2: Domain is relevant to the email theme but does not mimic a company name.")
print("--->3: Domain is not relevant to the email theme but mimics a company name.")
print("--->4: Domain is relevant to the email theme and mimics a company name.")
ans3 = input("Enter answer: ").strip()


if ans3 == '1':
    outfile.write("--->1: Domain has no relevance at all to the email theme or to a real company name.")
elif ans3 == '2':
    outfile.write("--->2: Domain is relevant to the email theme but does not mimic a company name.")
elif ans3 == '3':
    outfile.write("--->3: Domain is not relevant to the email theme but mimics a company name.")
elif ans3 == '4':
    outfile.write("--->4: Domain is relevant to the email theme and mimics a company name.")
else:
    print("Invalid selection...exiting")
    sys.exit(1)

ans3val = int(ans3)*int(80/4)

outfile.write("\n")

print("4. What type of layout did you use for the phishing email??")
print("--->1: Plain text used with no formatting.")
print("--->2: Plain text used with a fake logo.")
print("--->3: Plain text used with a real logo.")
print("--->4: Formatting used but no logos used.")
print("--->5: Formatting and a fake logo used.")
print("--->6: Formatting used with a real logo.")
ans4 = input("Enter answer: ").strip()


if ans4 == '1':
    outfile.write("--->1: Plain text used with no formatting.")
elif ans4 == '2':
    outfile.write("--->2: Plain text used with a fake logo.")
elif ans4 == '3':
    outfile.write("--->3: Plain text used with a real logo.")
elif ans4 == '4':
    outfile.write("--->4: Formatting used but no logos used.")
elif ans4 == '5':
    outfile.write("--->5: Formatting and a fake logo used.")
elif ans4 == '6':
    outfile.write("--->6: Formatting used with a real logo.")
else:
    print("Invalid selection...exiting")
    sys.exit(1)

ans4val = int(ans4)*int(60/6)
    
outfile.write("\n")

print("5. How much contextual business information did the phishing email contain??")
print("--->1: Email theme made without prior knowledge (i.e., an outsider could easily craft this phishing email without knowing a lot about the company).")
print("--->2: Email theme made using publicly avaiable company knowledge.")
print("--->3: Email theme made using knowledge only available after lots of recon or that only an employee would have.")
ans5 = input("Enter answer: ").strip()


if ans5 == '1':
    outfile.write("--->1: Email theme made without prior knowledge (i.e., an outsider could easily craft this phishing email without knowing a lot about the company).")
elif ans5 == '2':
    outfile.write("--->2: Email theme made using publicly avaiable company knowledge.")
elif ans5 == '3':
    outfile.write("--->3: Email theme made using knowledge only available after lots of recon or that only an employee would have.")
else:
    print("Invalid selection...exiting")
    sys.exit(1)

ans5val = int(ans5)*int(80/3)
    
outfile.write("\n")

print("6. Did the phishing email have any grammatical or spelling errors??")
print("--->1: The email contained 2 or more grammatical or spelling errors.")
print("--->2: The email contained a single grammatical or spelling error.")
print("--->3: The email contained no grammatical or spelling errors.")
ans6 = input("Enter answer: ").strip()


if ans6 == '1':
    outfile.write("--->1: The email contained 2 or more grammatical or spelling errors.")
elif ans6 == '2':
    outfile.write("--->2: The email contained a single grammatical or spelling error.")
elif ans6 == '3':
    outfile.write("--->3: The email contained no grammatical or spelling errors.")
else:
    print("Invalid selection...exiting")
    sys.exit(1)

ans6val = int(ans6)*int(40/3)

outfile.write("\n")

print("7. How much did you personalize the phishing email??")
print("--->1: No personalization used (employee name or company name not used).")
print("--->2: A single personalization used (employee name or company name used).")
print("--->3: More than one personalization used (employee name and company name used).")
ans7 = input("Enter answer: ").strip()


if ans7 == '1':
    outfile.write("--->1: No personalization used (employee name or company name not used).")
elif ans7 == '2':
    outfile.write("--->2: A single personalization used (employee name or company name used).")
elif ans7 == '3':
    outfile.write("--->3: More than one personalization used (employee name and company name used).")
else:
    print("Invalid selection...exiting")
    sys.exit(1)

ans7val = int(ans7)*int(60/3)

outfile.write("\n")

if emailtype == '1':
    print("8. For credential harvesting emails, was HTTPs used for the fake login page??")
    print("--->1: Simple HTTP used for the fake login page (HTTPs not used).")
    print("--->2: HTTPs used for the fake login page.")
    ans8 = input("Enter answer: ").strip()
    

    if ans8 == '1':
        outfile.write("--->1: Simple HTTP used for the fake login page (HTTPs not used).")
    elif ans8 == '2':
        outfile.write("--->2: HTTPs used for the fake login page.")
    else:
        print("Invalid selection...exiting")
        sys.exit(1)

    ans8val = int(ans8)*int(60/2)
    

    outfile.write("\n")

    print("9. How visible was the link??")
    print("--->1: Link plainly visible in the email body just by reading it.")
    print("--->2: A button or other text used for the hyperlink, but the recipient can mouse over and get the link.")
    print("--->3: A url shortener was used.")
    ans9 = input("Enter answer: ").strip()

    if ans9 == '1':
        outfile.write("--->1: Link plainly visible in the email body just by reading it.")
    elif ans9 == '2':
        outfile.write("--->2: A button or other text used for the hyperlink, but the recipient can mouse over and get the link.")
    elif ans9 == '3':
        outfile.write("--->3: A url shortener was used.")
    else:
        print("Invalid selection...exiting")
        sys.exit(1)

    ans9val = int(ans9)*int(60/3)
    total = int(ans1val + ans2val + ans3val + ans4val + ans5val + ans6val + ans7val + ans8val + ans9val)
    avg = int(total/9)
    maxpts = int(560)
    
    outfile.write("\n")

if emailtype == '2':
    print("8. For attachment-based emails, how much user interaction was required to 'compromise' the user?")
    print("--->1: The user would need to open the attachment and click through more than 1 prompt.")
    print("--->2: The user would need to open the attachment and click through 1 prompt.")
    print("--->3: The user is 'compromised' by simply opening the attachment without any additional actions.")
    ans8 = input("Enter answer: ").strip()
 
    if ans8 == '1':
        outfile.write("--->1: The user would need to open the attachment and click through more than 1 prompt.")
    elif ans8 == '2':
        outfile.write("--->2: The user would need to open the attachment and click through 1 prompt.")
    elif ans8 == '3':
        outfile.write("--->3: The user is 'compromised' by simply opening the attachment without any additional actions.")
    else:
        print("Invalid selection...exiting")
        sys.exit(1)

    ans8val = int(ans8)*int(60/3)
    total = int(ans1val + ans2val + ans3val + ans4val + ans5val + ans6val + ans7val + ans8val)
    avg = int(total/8)
    maxpts = int(500)
    
    outfile.write("\n")

if emailtype == '3':
    print("8. How visible was the link??")
    print("--->1: Link plainly visible in the email body just by reading it.")
    print("--->2: A button or other text used for the hyperlink, but the recipient can mouse over and get the link.")
    print("--->3: A url shortener was used.")
    ans8 = input("Enter answer: ").strip()
    
    if ans8 == '1':
        outfile.write("--->1: Link plainly visible in the email body just by reading it.")
    elif ans8 == '2':
        outfile.write("--->2: A button or other text used for the hyperlink, but the recipient can mouse over and get the link.")
    elif ans8 == '3':
        outfile.write("--->3: A url shortener was used.")
    else:
        print("Invalid selection...exiting")
        sys.exit(1)
        
    ans8val = int(ans8)*int(60/3)
    total = int(ans1val + ans2val + ans3val + ans4val + ans5val + ans6val + ans7val + ans8val)
    avg = int(total/8)
    maxpts = int(500)
    
    outfile.write("\n")

if emailtype == '4':
    print("8. How similar was the sender to the target executive or company?")
    print("--->1: A generic email account by executive title was used on an external domain (ex: 'ceo@yahoo.com').")
    print("--->2: An email account using an executive's name was used on an external domain (ex: 'jon.doe@yahoo.com').")
    print("--->3: An email account using an executive's name was used on an external domain that mimics the company name.")
    print("--->4: An executive's account and domain name were spoofed to appear as though it were an internal email.")
    ans8 = input("Enter answer: ").strip()

    if ans8 == '1':
        outfile.write("--->1: A generic email account by executive title was used on an external domain (ex: 'ceo@yahoo.com').")
    elif ans8 == '2':
        outfile.write("--->2: An email account using an executive's name was used on an external domain (ex: 'jon.doe@yahoo.com').")
    elif ans8 == '3':
        outfile.write("--->3: An email account using an executive's name was used on an external domain that mimics the company name.")
    elif ans8 == '4':
        outfile.write("--->4: An executive's account and domain name were spoofed to appear as though it were an internal email.")
    else:
        print("Invalid selection...exiting")
        sys.exit(1)
        
    ans8val = int(ans8)*int(60/4)
    total = int(ans1val + ans2val + ans3val + ans4val + ans5val + ans6val + ans7val + ans8val)
    avg = int(total/8)
    maxpts = int(500)
    
    outfile.write("\n")

print('-'*50)
outfile.write("\n")
outfile.write('-'*50)
outfile.write("\n")

if emailtype == '1':
    if  (total > 171 and total <= 311):
        print("This campaign is rated as EASY based on the data entered.")
        outfile.write("This campaign is rated as EASY based on the data entered.")
        outfile.write("\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")
    if (total > 311 and total <=435):
        print("This campaign is rated as MEDIUM based on the data entered.")
        outfile.write("This campaign is rated as MEDIUM based on the data entered.\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")
    if total > 435:
        print("This campaign is rated as HARD based on the data entered.")
        outfile.write("This campaign is rated as HARD based on the data entered.\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")

    print("Ranges:")
    print("EASY: 171 - 311")
    print("MEDIUM: 312 - 435")
    print("HARD: 436 - 560")

    outfile.write("Ranges:\n")
    outfile.write("EASY: 171 - 311\n")
    outfile.write("MEDIUM: 312 - 435\n")
    outfile.write("HARD: 436 - 560\n")

    outfile.close()

if emailtype == '2':
    if (total > 141 and total <= 270):
        print("This campaign is rated a EASY based on the data entered.")
        outfile.write("This campaign is rated a EASY based on the data entered.\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")
    if (total > 270 and total <=385):
        print("This campaign is rated as MEDIUM based on the data entered.")
        outfile.write("This campaign is rated as MEDIUM based on the data entered.\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")
    if total > 385:
        print("This campaign is rated as HARD based on the data entered.")
        outfile.write("This campaign is rated as HARD based on the data entered.\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")

    print("Ranges:")
    print("EASY: 142 - 270")
    print("MEDIUM: 271 - 385")
    print("HARD: 386 - 500")

    outfile.write("Ranges:\n")
    outfile.write("EASY: 142 - 270\n")
    outfile.write("MEDIUM: 271 - 385\n")
    outfile.write("HARD: 386 - 500\n")

    outfile.close()

if emailtype == '3':
    if (total > 141 and total <= 270):
        print("This campaign is rated a EASY based on the data entered.")
        outfile.write("This campaign is rated a EASY based on the data entered.\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")
    if (total > 270 and total <=385):
        print("This campaign is rated as MEDIUM based on the data entered.")
        outfile.write("This campaign is rated as MEDIUM based on the data entered.\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")
    if total > 385:
        print("This campaign is rated as HARD based on the data entered.")
        outfile.write("This campaign is rated as HARD based on the data entered.\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")

    print("Ranges:")
    print("EASY: 142 - 270")
    print("MEDIUM: 271 - 385")
    print("HARD: 386 - 500")

    outfile.write("Ranges:\n")
    outfile.write("EASY: 142 - 270\n")
    outfile.write("MEDIUM: 271 - 385\n")
    outfile.write("HARD: 386 - 500\n")

    outfile.close()

if emailtype == '4':
    if (total > 136 and total <= 270):
        print("This campaign is rated a EASY based on the data entered.")
        outfile.write("This campaign is rated a EASY based on the data entered.\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")
    if (total > 270 and total <=385):
        print("This campaign is rated as MEDIUM based on the data entered.")
        outfile.write("This campaign is rated as MEDIUM based on the data entered.\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")
    if total > 385:
        print("This campaign is rated as HARD based on the data entered.")
        outfile.write("This campaign is rated as HARD based on the data entered.\n")
        print("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.")
        outfile.write("The score was " + str(total) + " out of a total of " + str(maxpts) + " maximum points.\n")

    print("Ranges:")
    print("EASY: 137 - 270")
    print("MEDIUM: 271 - 385")
    print("HARD: 386 - 500")

    outfile.write("Ranges:\n")
    outfile.write("EASY: 137 - 270\n")
    outfile.write("MEDIUM: 271 - 385\n")
    outfile.write("HARD: 386 - 500\n")


print('-'*50)
print("DONE! Output written to phish-difficulty-score-%s.txt in the current directory" % writedate)
print('-'*50)
