# CloudflareDNSUpdatey
CloudflareDNSUpdatey updates your Cloudflare record IP - useful for homelabs and the like with dynamic IPs. 

# Usage
Provide the script with the four required parameters - token, email, zone and record. You can make it run automatically by running it as a task on your OS.

Example usage:
> CloudflareDNSUpdatey.py -token 12345abcd -email john@example.org -zone example.org -record test.example.org



### Requirements
Python  3.6.5  
[Requests ](http://docs.python-requests.org/en/master/) 
