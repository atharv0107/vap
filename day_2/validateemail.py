"""email=input("What is your email address?")
     
if "@" in email:
    print('Valid email address')
else:
    print('Invalid email address')
    
    
#2.

email=input("What is your email address?").strip()
username,Domain=email.split("@")

if username and"." in Domain:
    print('Valid email address')
else:
    print('Invalid email address')
  
#3.
email=input("What is your email address?").strip()

username,Domain=email.split("@")

if username and Domain.endswith(".edu",".com",".am"):
    print('Valid email address')
else:
    print('Invalid email address')  
    
#4.regular expression (re)re.search(pattern, string,flags=0)
import re
phone = input("What is your phone number?").strip()

# Accepts 10 digits, optionally separated by spaces or dashes
if re.fullmatch(r'(\d{10}|(\d{3}[- ]\d{3}[- ]\d{4}))', phone):
    print('Valid phone number')
else:
    print('Invalid phone number')
    
    
#5.re.iGNORECASE

import re
email=input("What is your email address?").strip()  

if re.search(r'^[\w.-]+@[\w.-]+\.(edu|com|asm)$',email):
    print('Valid email address')
else:
    print('Invalid email address') 
    
   """  
#6.re.
import re
m_number=input("enter your mobile number:").strip()  

if re.search(r'^\d{10}$',m_number):
    print('Valid number')   
else:
    print('Invalid number') 