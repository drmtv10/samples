# -*- coding: cp1252 -*-
###—— INPUT: as one string

###[tboltm23#a]$ PlatCmd --raid

import pprint
from copy import deepcopy

InputStr = \
"MD-RAID \n\
    Disk 1.1   sdb5  active \n\
    Disk 1.17  sdf5  active \n\
    Disk 1.24  sdy5  active \n\
    Disk 1.18  sdl5  active \n\
    Disk 1.4   sdt5  active \n\
    Disk 1.16  sdw5  active \n\
    Disk 1.8   sdu5  active \n\
VM-RAID 1 \n\
    Disk 1.15  sdq  active \n\
    Disk 1.14  sdk  active \n\
    Disk 1.13  sde  active \n\
    Disk 1.11  sdp  active \n\
    Disk 1.10  sdj  active \n\
    Disk 1.9   sdd  active \n\
    Disk 1.7   sdo  active \n\
    Disk 1.6   sdi  active \n\
    Disk 1.5   sdc  active \n\
VM-RAID 2 \n\
    Disk 1.23  sds6  active \n\
    Disk 1.22  sdm6  active \n\
    Disk 1.21  sdg6  active \n\
    Disk 1.20  sdx6  active \n\
    Disk 1.19  sdr6  active \n\
    Disk 1.18  sdl6  active \n\
    Disk 1.17  sdf6  active \n\
    Disk 1.16  sdw6  active \n\
    Disk 1.12  sdv6  active \n\
    Disk 1.8   sdu6  active \n\
    Disk 1.4   sdt6  active \n\
    Disk 1.3   sdn6  active \n\
    Disk 1.2   sdh6  active \n\
    Disk 1.1   sdb6  active\n"

"""
— OUTPUT: dictionary of dictionary
{
    'MD-RAID': {
        '1.1':  { 'device': 'sdb5', 'status': 'active'},
        ‘1.17': { 'device': 'sdf5', 'status': 'active'},
        ...
    },
    'VM-RAID 1': {
    ..
    },
    'VM-RAID 2': {
    }
}
"""

def parse_Platcmd(platcmd_outstr):
    line=""
    raidg = dict() # raid group dict
    disks_ver = dict() # disk list items
    raids_disks = list()
    #print "PlatCmd=", platcmd_outstr
    for line in platcmd_outstr.splitlines():
        #print line
        if 'RAID' in line:
            # if disk entries for RAID, save.
            if disks_ver and raidkey:
                #print "***", raidkey, "***"
                raidg[raidkey]=deepcopy(disks_ver)
                #pprint.pprint(raidg)
                disks_ver.clear()
            # new RAID entry
            raidkey = line
            #print raidkey
        if 'Disk' in line:
            devd = dict()
            key_diskver = line.split()[1]
            devd ['device'] = line.split()[2]
            devd ['status'] = line.split()[3]
            disks_ver[key_diskver] = devd
            # print devd
    # last RAID - disk entries, save.
    if disks_ver and raidkey:
        raidg[raidkey]=disks_ver
    return raidg     

def main():
  outdict = parse_Platcmd(InputStr)
  pprint.pprint(outdict)

if __name__ == "__main__":
   main()
