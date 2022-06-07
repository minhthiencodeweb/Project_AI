# import re
# import subprocess
# device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
# df = subprocess.check_output("lsusb")
# devices = []
# for i in df.split('\n'):
#     if i:
#         info = device_re.match(i)
#         if info:
#             dinfo = info.groupdict()
#             dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
#             devices.append(dinfo)
# print (devices)
#=============================================
# import os ,string ,time
# from ctypes import windll
# from tkinter import *
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import csv
# import shutil
# from tkinter import filedialog
# import os ,string ,time
# from ctypes import windll
#
# def get_driveStatus():
#     devices = []
#     record_deviceBit = windll.kernel32.GetLogicalDrives(  )  # The GetLogicalDrives function retrieves a bitmask
#     # representing the currently available disk drives.
#     for label in string.ascii_uppercase:  # The uppercase letters 'A-Z'
#         if record_deviceBit & 1:
#             devices.append(label)
#         record_deviceBit >>= 1
#     return devices
#
# def detect_device():
#     original = set(get_driveStatus())
#     print ('Detecting...')
#     time.sleep(5)
#     add_device =  set(get_driveStatus() )- original
#     # subt_device = original - set(get_driveStatus())
#
#     if (len(add_device)):
#         print ("There were %d "% (len(add_device)))
#         for drive in add_device:
#             path= (r"The drives added: %s:" % (drive)  + '\Attend.csv')  #r'E:\attend.csv'
#     print(path)
#
#
#
#
#
#     # elif(len(subt_device)):
#     #     print ("There were %d "% (len(subt_device)))
#     #     for drive in subt_device:
#     #         print ("The drives remove: %s:" % (drive))
#
#
# detect_device()
#
#
# def usb_data(self):
#     try:
#         usb_file = messagebox.askyesno("Export", "Do you want to Export to USB", parent=self.root)
#         filepath = (r'E:\attend.csv')
#         if not (os.path.exists(filepath) and (usb_file > 0)):
#             open(r'E:\attend.csv', 'w')
#         shutil.copy(src=r'C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\attend.csv', dst=r'E:\attend.csv')
#         messagebox.showinfo("Success", "Exported to USB successfully", parent=self.root)
#     except Exception as es:
#         messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)






















#=========================================================
# from tkinter import messagebox
# import os.path
# import shutil
#
# def diff(list1, list2):
#     list_difference = [item for item in list1 if item not in list2]
#     return list_difference
#
# dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
# print(drives)
# while True:
#     uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
#     x = diff(uncheckeddrives, drives)
#     if x:
#         x = "+".join(x)
#         print(str(x) + "\Attend.csv")
#         break
#=======================================================================
from tkinter import messagebox
import os
import shutil
import pathlib



def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference

def usb_data(self):
    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    print(drives)
    while True:
        uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
        x = diff(uncheckeddrives, drives)
        if x:
            x = "+".join(x)
            filepath = (str(x) + "/Attend.csv")
            print(filepath)                        #E:/Attend.csv
            print(os.path.exists(filepath))        #True or False
            try:
                usb_file = messagebox.askyesno("Export", "Please connect ", parent=self.root)
                if not (os.path.exists(filepath) and (usb_file>0)):
                    open(filepath, 'w')
                shutil.copy(src=r'C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\attend.csv', dst=filepath)
                messagebox.showinfo("Success", "Exported to USB successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)



# def usb_data(self):
#     try:
#         usb_file = messagebox.askyesno("Export", "Please connect ", parent=self.root)
#         filepath = (r'E:\attend.csv')
#         if not (os.path.exists(filepath) and (usb_file > 0)):
#             open(r'E:\attend.csv', 'w')
#         shutil.copy(src=r'C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\attend.csv', dst=r'E:\attend.csv')
#         messagebox.showinfo("Success", "Exported to USB successfully", parent=self.root)
#     except Exception as es:
#         messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)


#==========================================================================================
# import pyudev
# from pyudev import Monitor
#
# context = pyudev.Context()
# monitor = Monitor.from_netlink()
# # For USB devices
# monitor.filter_by(susbsytem='usb')
# # OR specifically for most USB serial devices
# monitor.filter_by(susbystem='tty')
# for action, device in monitor:
#     vendor_id = device.get('ID_VENDOR_ID')
#     # I know the devices I am looking for have a vendor ID of '22fa'
#     if vendor_id in ['22fa']:
#         print('Detected {} for device with vendor ID {}'.format(action, vendor_id))



#====================================================================================























