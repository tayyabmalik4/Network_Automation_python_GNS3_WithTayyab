import getpass
import sys
import telnetlib



# taking ip address of the router
HOST = input("Enter Device IP: \n")
# taking username of the router
username = input("Enter Your username of the Router: \n")
# taking input of the router
password = getpass.getpass()

# creating the variable of the telnet
tn = telnetlib.Telnet(HOST)


# check and write the username
tn.read_until(b"Username: ")
tn.write(username.encode('ascii')+b"\n")


# Check and write the password 
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii')+ b"\n")


# enable the password
tn.write(b"enable\n")
tn.write(b"cisco\n")
# go to configuration file
tn.write(b"conf t \n")
# confiure loopback 1 in the router
tn.write(b"int loop 1 \n")
tn.write(b"ip address 1.1.1.1 255.255.255.0 \n")
# confiure loopback 2 in the router
tn.write(b"int loop 2 \n")
tn.write(b"ip address 2.2.2.2 255.255.255.0 \n")
# configure router configuration
tn.write(b"router ospf 1 \n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0 \n")
# end the confiuration
tn.write(b"end \n")
# exit the router configuration
tn.write(b"exit \n")

# show all the command which we run in the script
print(tn.read_all().decode('ascii'))