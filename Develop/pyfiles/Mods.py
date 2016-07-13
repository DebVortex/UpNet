#Module to intepreit all the files in a mod.

'''Info scan
Scans all 
'''
import os
import sys
import logging

def InfoScan():
    logging.info('starting to scan for all Info.xml files...')
    for root, dir, files in os.walk(os.getcwd()):
        for name in files:
            if name == "Info.xml":
                logging.info('Found a info.xml file! location: ' + os.path.join(root, name))
InfoScan()
