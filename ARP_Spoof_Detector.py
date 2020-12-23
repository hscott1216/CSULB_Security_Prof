"""
Project Task

Create a script that extracts an ARP table from the cmd and checks if the machine is
being attacked using MITM via ARP spoof. The script must be able to run on Windows,
MacOs, and Linux. Keep in mind the different ways networking commands return data
in each Of those systems.

1. Create a function that prints each line Of the ARP table.

2. Make the function save only the IP and MAC addresses (without broadcast
addresses) in pairs.
Hint: the ARP table output should be iterated and filtered.

3. Create a function that checks if a MAC address exists twice in the ARP table. If found,
print that the machine is being ARP spoofed and complete the execution.
Hint: The ARP table was already extracted in a previous step.

4. Combine the functions in a logical flow and allow the code to run specifically from
this file. Modify the module importation.
Hint: This step involves writing the code block to start the program execution.

5. Create a function that saves a log with the message, date, and time, if the machine
was attacked.


"""



import os
import ipaddress
import arp

# The logic below will
# 1.Import arp table from the host machine
# 2. get the culled Arp table to Ip address paired with matching MAC address
# 3. check the culled table and report is a spoof is found (muliple Ip with the same MAC adress
def main():
    #arpSpoofDetector(fake_arp_list)

    arpCheck = arp.getarpTable()# this function gets an culls the arp table
    arp.arpSpoofDetector(arpCheck)

if __name__ == '__main__':
    main() # initiate code on this page 