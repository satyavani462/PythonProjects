email=input("enter your email").strip()
username=email[:email.index('@')]
domainname=email[email.index('@'):]
print(f"Name is {username} and domain name is {domainname}")