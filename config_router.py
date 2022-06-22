import getpass
import sys
import telnetlib
from this import s


def raw_input(param):
    pass


HOST = input("Enter Device IP: \n")
username = input("Enter Your username of the Router: \n")

password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(username.encode('ascii')+b"\n")


if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii')+ b"\n")


tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t \n")
tn.write(b"int fa1/0 \n")
tn.write(b"ip address 10.10.10.7 255.255.255.0 \n")
tn.write(b"end \n")
tn.write(b"exit \n")

print(tn.read_all().decode('ascii'))