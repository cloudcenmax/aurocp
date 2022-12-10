#!/usr/bin/env python
import os

os.system("echo Hello from the other side!")
os.system('yum update httpd')
os.system('yum install httpd')
os.system('firewall-cmd --permanent --add-service=http')
os.system('firewall-cmd --permanent --add-service=https')
os.system('firewall-cmd --reload')
os.system('systemctl start httpd')
os.system('systemctl status httpd')