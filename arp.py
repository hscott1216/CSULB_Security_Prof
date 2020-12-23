

# call arp Table
# func() takes arp table date and exstracts the IP and MAC addresses in pairs (with out broadcast addresses)
# func() Check Mac address to see if MAC appears more than once in arp table
# create a new code file and import previous function in to logic for complete program
# create a func() a log with the message date and time the machine was attack




import os
import ipaddress

def getarpTable():
    rawArpList = []
    arpList ={}

    os.system(r"arp -a > ArpCheck.txt")
    with open("ArpCheck.txt","r") as arpFile:
        for line in arpFile:  # if statements to remove unwanted lines
            if "Inter" in line:  # remove lines with text Descriptors
                continue
            elif "ff-ff-ff" in line:  # remove brodcast entries
                continue
            elif len(line) < 2: # remove lines without information
                continue
            else:
                rawArpList.append(line.split())  # combine raw data in to one list
    for line in rawArpList:# combine data in to a new Dictionary
        arpList[line[0]] = line[1]
    return arpList

def arpSpoofDetector(arpTable):
    macList = []
    spoofFound = 0
    for ip in arpTable: # intiates the loop to compare
        if arpTable[ip] in macList:
            print(f"Found duplicate MAC address {arpTable[ip]} in ARP Table ")
            spoofFound +=1
        else:
            macList.append(arpTable[ip])
    if spoofFound >0 :
        print("This could be an idicator of an ARP spoof attack")
        print("futher investoigation is required.")
    else:
        print("No ARP spoof detected")
    #print(macList)
    return