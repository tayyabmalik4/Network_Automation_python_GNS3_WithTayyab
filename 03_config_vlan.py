import getpass
import sys
import telnetlib

from pyrsistent import b

HOST = "10.10.10.8"
user = input("Enter your telnet username: \n")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") +b"\n")

tn.write(b"vlan database \n")
# Now we don't configure the enable password because we set the router as a privilege 15
tn.write(b"vlan 2 \n")
tn.write(b"name Python_VLAN_2 \n")
# tn.write(b"exit \n")
tn.write(b"vlan 3 \n")
tn.write(b"name Python_VLAN_3 \n")
# tn.write(b"exit \n")
# tn.write(b"vlan 4 \n")
# tn.write(b"name Python_VLAN_4 \n")
# tn.write(b"exit \n")
# tn.write(b"vlan 5 \n")
# tn.write(b"vlan 5 name Python_VLAN_5 \n")
# tn.write(b"exit \n")
# tn.write(b"vlan 6 \n")
# tn.write(b"vlan 6 name Python_VLAN_6 \n")
# tn.write(b"exit \n")
tn.write(b"exit \n")
tn.write(b"exit \n")

print(tn.read_all().decode("ascii"))
