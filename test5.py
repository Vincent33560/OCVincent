import paramiko
import time
import os
import csv

from pip._vendor.distlib.compat import raw_input


def sendRec(ssh, command):
    """Send a command to the device and receive and print the result."""

    # Send the device a command
    ssh.send("\n")
    ssh.send(str(command) + "\n")

    # Wait for the command to complete in seconds
    time.sleep(1)

    # Receive 5000 bytes and print to screen
    output = ssh.recv(5000)
    print
    output


def sendRecWrite(ssh, file_name, command):
    """Send a command to the device and save the output to a file."""

    # Send the device a command
    ssh.send("\n")
    ssh.send(str(command) + "\n")

    # Wait for the command to complete in seconds
    time.sleep(1)

    # Receive 5000 bytes and print to file_name
    output = ssh.recv(5000)
    to_file = open(file_name, 'w')
    print >> to_file, output
    to_file.close()


def disablePaging(ssh):
    """Disable paging on a Cisco router"""

    ssh.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output = ssh.recv(1000)

    return output


def main():
    longstring = """\
    \n
            /,,
           /\  )
             \,'
          /`'`\.
              ,
             ,@,
            ,@@@,
           ,@@@@@,
    `@@@@@@@@@@@@@@@@@@@`
      `@@@@@@@@@@@@@@@`
        `@@@@@@@@@@@`
       ,@@@@@@`@@@@@@,
       @@@@`     `@@@@
      ;@`           `@;
        _   _   _   _
       (   (   (   |_)
        ~   ~   ~  |

    Cisco 
    CLI
    Configuration with
    Paramiko
    Written by: Patrick Sinotte
    Version 2.2864
    Welcome, Comrade!
    """

    # Clear screen and print welcome to screen
    os.system("clear")
    print
    longstring

    # Prompt user for pre-configured IP address and ssh credentials
    ip = raw_input("Enter IP address of device (q to quit): ")
    if ip == "q":
        exit()
    else:
        username = raw_input("username: ")
        password = raw_input("password: ")

    # Create instance of SSHClient object
    ssh_pre = paramiko.SSHClient()
    # Automatically add untrusted hosts
    ssh_pre.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    # initiate SSH connection
    ssh_pre.connect(ip, username=username, password=password)
    print
    "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
    ssh = ssh_pre.invoke_shell()
    print
    "Interactive SSH session established"

    # Strip the initial router prompt
    output = ssh.recv(1000)

    # Turn off paging
    disablePaging(ssh)

    # Turn off automatic domain-lookup
    sendRec(ssh, "conf t")
    sendRec(ssh, "no ip domain-lookup")

    devMain(ssh)


def devMain(ssh):
    """The main menu once connected to a device.

    Allows user to go to show(), confMain(), connTest(), fileMan(), or main().
    """

    # Show version and connected users
    sendRec(ssh, "\x1a")
    sendRec(ssh, "show version | include Cisco IOS")
    sendRec(ssh, "show users")

    # Show main menu and interpret user choice
    menu_choice = -1
    while 0 > menu_choice or 4 < menu_choice:
        try:
            print
            "\nMAIN MENU"
            print
            "Please choose from one of the following options:"
            print
            """\n
                1 - show configuration \n
                2 - configure device \n
                3 - test connectivity \n
                4 - save/load \n
                0 - logout \n"""
            menu_choice = int(raw_input())
        except ValueError:
            print
            "Choose a number from 1 to 4"
    if menu_choice == 1:
        show(ssh)
    elif menu_choice == 2:
        confMain(ssh)
    elif menu_choice == 3:
        connTest(ssh)
    elif menu_choice == 4:
        fileMan(ssh)
    elif menu_choice == 0:
        main()


def show(ssh):
    """Allows user to run a variety of show commands."""

    menu_choice = -1
    while 0 > menu_choice or 8 < menu_choice:
        try:
            print
            "\nSHOW MENU"
            print
            "Please choose from one of the following options:"
            print
            """\n
                1 - show running configuration \n
                2 - show ip interfaces brief \n
                3 - show routing table \n
                4 - show CDP neighbors \n
                5 - show flash \n
                6 - show version \n
                7 - show license \n
                8 - show vlans \n
                0 - back \n"""
            menu_choice = int(raw_input())
        except ValueError:
            print
            "Choose a number from 1 to 8"
    if menu_choice == 1:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show run")
    elif menu_choice == 2:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show ip int b")
    elif menu_choice == 3:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show ip route")
    elif menu_choice == 4:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show cdp neigh")
    elif menu_choice == 5:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show flash")
    elif menu_choice == 6:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show version")
    elif menu_choice == 7:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show license")
    elif menu_choice == 8:
        sendRec(ssh, "\x1a")
        sendRec(ssh, "show vlan")

    elif menu_choice == 0:
        devMain(ssh)
    show(ssh)


def confMain(ssh):
    menu_choice = -1
    while 0 > menu_choice or 4 < menu_choice:
        try:
            print
            "\nCONFIGURATION MENU"
            print
            "Please choose from one of the following options:"
            print
            """\n
                1 - device configuration \n
                2 - interface configuration \n
                3 - routing configuration \n
				4 - vlan configuration \n
                0 - back \n"""
            menu_choice = int(raw_input())
        except ValueError:
            print
            "Choose a number from 1 to 4"
    if menu_choice == 1:
        devConf(ssh)
    elif menu_choice == 2:
        intConf(ssh)
    elif menu_choice == 3:
        routeConf(ssh)
    elif menu_choice == 4:
        vlanConf(ssh)

    elif menu_choice == 0:
        devMain(ssh)


def devConf(ssh):
    menu_choice = -1
    while 0 > menu_choice or 2 < menu_choice:
        try:
            print
            "\nDEVICE CONFIGURATION MENU"
            print
            "Please choose from one of the following options:"
            print
            """\n
                1 - set clock \n
                2 - set hostname \n
                0 - back \n"""
            menu_choice = int(raw_input())
        except ValueError:
            print
            "Choose a number from 1 to 2"
    if menu_choice == 1:
        setClock(ssh)
    elif menu_choice == 2:
        setHostname(ssh)
    elif menu_choice == 0:
        confMain(ssh)
    devConf(ssh)


def setClock(ssh):
    print
    "\nCLOCK CONFIGURATION"
    print
    "SYNTAX: hh mm ss dd MONTH yyyy \n"
    hh = raw_input("hh: ")
    mm = raw_input("mm: ")
    ss = raw_input("ss: ")
    dd = raw_input("date: ")
    mo = raw_input("month: ")
    yy = raw_input("year: ")
    sendRec(ssh, "\x1a")
    sendRec(ssh, "clock set " + hh + ":" + mm + ":" + ss + " " + dd + " " + mo + " " + yy)
    devConf(ssh)


def setHostname(ssh):
    print
    "\nHOSTNAME CONFIGURATION"
    hostname = raw_input("hostname:")
    sendRec(ssh, "\x1a")
    sendRec(ssh, "conf t")
    sendRec(ssh, "hostname " + hostname)
    devConf(ssh)


def intConf(ssh):
    print
    "\nINTERFACE CONFIGURATION"
    sendRec(ssh, "\x1a")
    sendRec(ssh, "show ip int b")
    iface = raw_input("Interface to configure (x to exit): ")
    if iface == "x":
        confMain(ssh)
    else:
        if_desc = raw_input("Description: ")
        ip_addr = raw_input("IP address: ")
        net_mask = raw_input("Subnet mask in dotted decimal: ")
        sendRec(ssh, "conf t")
        sendRec(ssh, "int " + iface)
        sendRec(ssh, "desc " + if_desc)
        sendRec(ssh, "ip add " + ip_addr + " " + net_mask)
        sendRec(ssh, "no shut")
    intConf(ssh)


def routeConf(ssh):
    print
    "\nROUTING CONFIGURATION"
    sendRec(ssh, "\x1a")
    sendRec(ssh, "show ip route")
    route_net = raw_input("Network address to reach (x to exit): ")
    if route_net == "x":
        confMain(ssh)
    else:
        route_mask = raw_input("Subnet mask in dotted decimal: ")
        next_hop = raw_input("Exit interface or IP address of next hop: ")
        sendRec(ssh, "conf t")
        sendRec(ssh, "ip route " + route_net + " " + route_mask + " " + next_hop)
    routeConf(ssh)


def vlanConf(ssh):
    """Allows user to configure multiple VLANs and access ports via .csv"""

    print
    "\nVLAN CONFIGURATION FROM CSV FILE"
    sendRec(ssh, "\x1a")
    sendRec(ssh, "show vlan brief")
    print
    "Ready to load VLANs from csv file"
    print
    "Note: csv file must contain 3 fields named 'vlan_id', 'name', and 'int'"
    csv_file = raw_input("Filepath of VLAN csv on your computer: (x to exit)")
    if csv_file == "x":
        confMain(ssh)
    else:
        sendRec(ssh, "conf t")
        with open(csv_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                sendRec(ssh, "vlan " + (row['vlan_id']))
                sendRec(ssh, "name " + (row['name']))
                sendRec(ssh, "interface " + (row['int']))
                sendRec(ssh, "switchport mode access")
                sendRec(ssh, "switchport access vlan " + (row['vlan_id']))
    sendRec(ssh, "\x1a")
    sendRec(ssh, "show vlan brief")
    confMain(ssh)


def connTest(ssh):
    print
    "\nCONNECTION TESTING"
    menu_choice = -1
    while 0 > menu_choice or 2 < menu_choice:
        try:
            print
            "Please choose from one of the following options:"
            print
            """\n
                1 - ping \n
                2 - traceroute \n
                0 - back \n"""
            menu_choice = int(raw_input())
        except ValueError:
            print
            "Choose a number from 1 to 2"
    if menu_choice == 1:
        pingTest(ssh)
    elif menu_choice == 2:
        traceTest(ssh)
    elif menu_choice == 0:
        devMain(ssh)


def pingTest(ssh):
    print
    "\nPING"
    sendRec(ssh, "\x1a")
    sendRec(ssh, "show cdp neigh")
    ping_addr = raw_input("Host address to ping (x to exit): ")
    if ping_addr == "x":
        connTest(ssh)
    else:
        sendRec(ssh, "ping " + ping_addr)
    pingTest(ssh)


def traceTest(ssh):
    print
    "\nTRACEROUTE"
    sendRec(ssh, "\x1a")
    sendRec(ssh, "show cdp neigh")
    trace_addr = raw_input("Host address to traceroute to (x to exit): ")
    if trace_addr == "x":
        connTest(ssh)
    else:
        sendRec(ssh, "traceroute " + trace_addr)
    traceTest(ssh)


def fileMan(ssh):
    print
    "\nSAVE/LOAD"
    sendRec(ssh, "\x1a")
    menu_choice = -1
    while 0 > menu_choice or 6 < menu_choice:
        try:
            print
            "Please choose from one of the following options:"
            print
            """\n
                1 - save running config to startup config \n
                2 - save running config to computer \n
                3 - save running config to flash \n
                4 - load running config from startup config \n
                5 - load running config from computer \n
                6 - load running config from flash \n
                0 - back \n"""
            menu_choice = int(raw_input())
        except ValueError:
            print
            "Choose a number from 1 to 6"
    if menu_choice == 1:
        sendRec(ssh, "copy run start")
    elif menu_choice == 2:
        file_name = raw_input("Local file to save to: ")
        sendRecWrite(ssh, file_name, "show run | begin service")
    elif menu_choice == 3:
        sendRec(ssh, "show flash")
        flash_file_name = raw_input("Name file to store in flash: ")
        sendRec(ssh, "copy run flash:" + flash_file_name)
    elif menu_choice == 4:
        sendRec(ssh, "copy start run")
    elif menu_choice == 5:
        print
        "Ready to load config from file"
        file_name = raw_input("Filepath of running config on your computer: ")
        sendRec(ssh, "\x1a")
        sendRec(ssh, "conf t")
        with open(file_name) as f:
            for line in f:
                sendRec(ssh, line)
    elif menu_choice == 6:
        sendRec(ssh, "show flash")
        flash_file_name = raw_input("Name of running config to load: ")
        sendRec(ssh, "copy " + flash_file_name + " run")
    elif menu_choice == 0:
        devMain(ssh)
    fileMan(ssh)


if __name__ == '__main__':
    main()