import paramiko

def Interfaces():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()


    DEVICE_ACCESS = ssh.invoke_shell()
    DEVICE_ACCESS.send(b"en\n")
    DEVICE_ACCESS.send(b"vdcvdc\n")
    DEVICE_ACCESS.send(b"conf t\n")
    DEVICE_ACCESS.send(b"int g0/2\n")
    DEVICE_ACCESS.send(b"ip address 192.168.42.25 255.255.255.0\n")
    DEVICE_ACCESS.send(b"no shut\n")
    DEVICE_ACCESS.send(b"end\n")
    DEVICE_ACCESS.send(b"sh ip int br\n")
    time.sleep(1)

config_interface = Interfaces()



