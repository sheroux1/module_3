import re
my_emails = ["jordanw@codingtemple.orgcom", "pocohontas1776@gmail.com", "helloworld@aol..com",
             "yourfavoriteband@g6.org", "@codingtemple.com"]

def checkEmails(email_addresses):
    email_pattern = re.compile(r'([\w]+["@"][\w]+["."]([c][o][m]$|[o][r][g]$))')
    matches = []
    # test = email_pattern.findall(my_emails.split(', '))
    # print(my_emails)
    for email in my_emails:
        match = email_pattern.search(email)
        # print(match.groups(1))
        if match:
            matches.append(match.groups()[0]) 
        else:
            matches.append((f"None"))
            continue
    return matches

print(checkEmails(my_emails))