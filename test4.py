import paramiko
import time

# must setup login local user on the device (set priv to 15)
username = "vincent"
password = "admin"


def main():
	# may want to take this IP address in a different way, hard coded for starter script
	ip_address = "192.168.100.150"

	# initialze the client
	ssh_client = paramiko.SSHClient()

	# sends the client and the IP axdress to initiate session function
	remote_connection = initiate_ssh_session(ssh_client, ip_address)

	# use the connection to do stuff in the router via the ssh connection
	remote_connection.send("configure terminal\n")
	remote_connection.send("int loop 0\n")
	remote_connection.send("ip address 1.1.1.1 255.255.255.255\n")
	remote_connection.send("int loop 1\n")
	remote_connection.send("ip address 2.2.2.2 255.255.255.255\n")
	remote_connection.send("router ospf 1\n")
	remote_connection.send("network 0.0.0.0 255.255.255.255 area 0\n")

	for n in range (2,21):
	    print("Creating VLAN ".format(str(n)))
	    remote_connection.send("vlan " + str(n) +  "\n")
	    remote_connection.send("name Python_VLAN " + str(n) +  "\n")
	    # pause long enough for vlan to be created
	    time.sleep(0.5)

	remote_connection.send("end\n")

	# wait for a second, then output the remote connection session to screen
	time.sleep(1)
	output = remote_connection.recv(65535)
	print(output)

	# be sure to close the client when work is completed
	ssh_client.close


# initiates ssh client, pulls public key from device, connects to device and return connection object
def initiate_ssh_session(ssh_client, ip_address):
	# accept a public key from switch for use to connect to the switch via SSH
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=ip_address,username=username,password=password)

	print("Successful connection".format(ip_address))

	# returns the remote shell connection object
	return ssh_client.invoke_shell()


if __name__ == "__main__":
	main()

exit()