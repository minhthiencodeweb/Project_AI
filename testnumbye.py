# # with open("attend.csv", "r+", newline="\n") as f:  # mở file attend; vừa đọc vừa ghi
# #     myDataList = f.readlines()  #
# #     print(myDataList)
# #     name_list = []
# #     for line in myDataList:  # load từng dòng 1  ==>
# #         print(line)
# #         entry = line.split((","))  # tách theo dấu ','
# #         print(entry)
# #         name_list.append(entry[0])  # tách là lấy phần tử thứ 1
# #         print(name_list)
#
#
# # ['1,0344777347,thien,CCNA']
# # 1,0344777347,thien,CCNA
# # ['1', '0344777347', 'thien', 'CCNA']
# # ['1']
#
import shutil

import mysql.connector
from datetime import datetime



# def mark_attendance(self, i, n, d):
#     conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123", database="face_recognizer")
#     my_cursor = conn.cursor()
#
#     my_cursor.execute("select Name from studentinfo ")
#     namee = my_cursor.fetchone()
#     namee = "+".join(namee)
#
#     my_cursor.execute("select Id from studentinfo ")
#     idd = my_cursor.fetchone()
#     idd = "+".join(idd)
#
#     my_cursor.execute("select Dep from studentinfo ")
#     depp = my_cursor.fetchone()
#     depp = "+".join(depp)
#
#     with open("attend.csv", "r+", newline="\n") as f:  # mở file attend; vừa đọc vừa ghi
#         myDataList = f.readlines()  # ['1,0344777347,thien,CCNA,22:07:51,16/06/2022,Preset'] ==>table all trong file csv
#         name_list = []
#         for line in myDataList:  # load từng dòng 1  ==>1,0344777347,thien,CCNA,22:07:51,16/06/2022,Preset
#             entry = line.split((","))  # tách theo dấu ','
#             name_list.append(entry[0])  # tách là lấy phần tử thứ 1
#
#         if ((i not in name_list) and (n not in name_list) and (d not in name_list)):
#             if ((i in idd) and ( n in namee) and (d in depp)):
#                 now = datetime.now()
#                 d1 = now.strftime("%d/%m/%Y")
#                 dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#                 f.writelines(f"\n{i},{n},{d},{dtString},{d1},YES")
#             else:
#                 now = datetime.now()
#                 d1 = now.strftime("%d/%m/%Y")
#                 dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#                 f.writelines(f"\n{i},{n},{d},{dtString},{d1},AB")
#
#         # for p in data:
#         #     p = "+".join(p)
#         #     if((i not in name_list) and (n not in name_list) and (d not in name_list)):
#         #         if i in p:
#         #             now = datetime.now()
#         #             d1 = now.strftime("%d/%m/%Y")
#         #             dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#         #             f.writelines(f"\n{i},{n},{d},{dtString},{d1},YES")
#         #         else:
#         #             now = datetime.now()
#         #             d1 = now.strftime("%d/%m/%Y")
#         #             dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#         #             f.writelines(f"\n{p},{n},{d},{dtString},{d1},AB")


#
#
# def mark_attendance(self, i, n, d):
#     with open("attend.csv", "r+", newline="\n") as f:  # mở file attend; vừa đọc vừa ghi
#
#         conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="face_recognizer")
#         my_cursor = conn.cursor()
#         my_cursor.execute("select Id, Name, Dep from studentinfo ")
#         namee = my_cursor.fetchall()
#
#         myDataList = f.readlines()  # ['1,0344777347,thien,CCNA,22:07:51,16/06/2022,Preset'] ==>table all trong file csv
#         name_list = []
#         for line in myDataList:  # load từng dòng 1  ==>1,0344777347,thien,CCNA,22:07:51,16/06/2022,Preset
#             entry = line.split((","))  # tách theo dấu ','
#             name_list.append(entry[0])  # tách là lấy phần tử thứ 1
#
#         if ((i not in name_list) and (n not in name_list) and (d not in name_list)):  # kiểm tra xem coi đã có phần tử name_list(csv) hay chưa
#             for x, y, z in namee:
#                 x = "".join(x)
#                 y = "".join(y)
#                 z = "".join(z)
#                 if ((i in x) and (n in y) and (d in z)):
#                     now = datetime.now()
#                     d1 = now.strftime("%d/%m/%Y")
#                     dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#                     f.writelines(f"\n{x},{y},{z},{dtString},{d1},YES")
#                 else:
#                     now = datetime.now()
#                     d1 = now.strftime("%d/%m/%Y")
#                     dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#                     f.writelines(f"\n{x},{y},{z},{dtString},{d1},NO")


# def mark_attendance(self, i, n, d):
#     with open("attend.csv", "r+", newline="\n") as f:  # mở file attend; vừa đọc vừa ghi
#         conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="face_recognizer")
#         my_cursor = conn.cursor()
#         my_cursor.execute("select Id, Name, Dep from studentinfo ")
#         namee = my_cursor.fetchall()
#
#         myDataList = f.readlines()  # ['1,0344777347,thien,CCNA,22:07:51,16/06/2022,Preset'] ==>table all trong file csv
#         name_list = []
#         for line in myDataList:  # load từng dòng 1  ==>1,0344777347,thien,CCNA,22:07:51,16/06/2022,Preset
#             entry = line.split((","))  # tách theo dấu ','
#             name_list.append(entry[0])  # tách là lấy phần tử thứ 1
#
#         for x, y, z in namee:
#             x = "".join(x)
#             y = "".join(y)
#             z = "".join(z)
#             if ((i not in name_list) and (n not in name_list) and (d not in name_list)):  # kiểm tra xem coi đã có phần tử name_list(csv) hay chưa
#                 if (i in x) and (n in y) and (d in z):
#                     now = datetime.now()
#                     d1 = now.strftime("%d/%m/%Y")
#                     dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#                     f.writelines(f"\n{x},{y},{z},{dtString},{d1},YES")
#                 else:
#                     now = datetime.now()
#                     d1 = now.strftime("%d/%m/%Y")
#                     dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#                     f.writelines(f"\n{x},{y},{z},{dtString},{d1},NO")

# #308191044,son,CCNA,10:47:58,24/06/2022,NO

#
# mylist = []
# def absent_attendance(self,i, n, d):
#     mylist.append((i, n, d))
#     with open("attend.csv", "r+", newline="\n") as f:
#         conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="face_recognizer")
#         my_cursor = conn.cursor()
#         my_cursor.execute("select Id, Name, Dep from studentinfo ")
#         namee = my_cursor.fetchall()
#
#         myDataList = f.readlines()
#         name_list = []
#         for line in myDataList:
#             entry = line.split((","))
#             name_list.append(entry[0])
#
#         if ((i not in name_list) and (n not in name_list) and (d not in name_list)):
#             for si,sn,sd in mylist:
#                 for sqi,sqn,sqd in namee:
#                     if (si == sqi) and (sn == sqn) and (sd == sqd):
#                         continue
#                     if (i not in sqi) and (n not in sqn) and (d not in sqd):
#                         now = datetime.now()
#                         d1 = now.strftime("%d/%m/%Y")
#                         dtString = now.strftime("%H:%M:%S")
#                         f.writelines(f"\n{sqi},{sqn},{sqd},{dtString},{d1},NO")
#                 if len(namee) > len(mylist):
#                     break
#
# mark_attendance("0308191073","thien","CCNA")

# list=[]
# mylist=[]
# a="0308191073"
# b="thien"
# c="CCNA"
# x="0308191044"
# y="huy"
# z="CCNA"
#
#
#
# mylist.append((a,b,c))
# mylist.append((x,y,z))
#
# print(mylist)
# conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123", database="face_recognizer")
# my_cursor = conn.cursor()
# my_cursor.execute("select Id, Name, Dep from studentinfo ")
# namee = my_cursor.fetchall()
#
# print(namee)
#
# print(len(namee))
#
#
# for my in mylist:
#     for sq in namee:
#         if (my==sq):
#             print("có mặt")
#         else:
#             print("vắng")
#         if len(namee) > len(mylist):
#             break

#======OK
# def absent_attendance(self, i, n, d):
#     with open("attend.csv", "r+", newline="\n") as f:
#         conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123", database="face_recognizer")
#         my_cursor = conn.cursor()
#         my_cursor.execute("select Id, Name, Dep from studentinfo ")
#         namee = my_cursor.fetchall()
#
#         myDataList = f.readlines()
#         name_list = []
#         for line in myDataList:
#             entry = line.split((","))
#             name_list.append(entry[0])
#         for x, y, z in namee:
#             x = "".join(x)
#             y = "".join(y)
#             z = "".join(z)
#             if (i in x) and (n in y) and (d in z):
#                 now = datetime.now()
#                 d1 = now.strftime("%d/%m/%Y")
#                 dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#                 f.writelines(f"\n{x},{y},{z},{dtString},{d1},YES")
#             else:
#                 now = datetime.now()
#                 d1 = now.strftime("%d/%m/%Y")
#                 dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#                 f.writelines(f"\n{x},{y},{z},{dtString},{d1},NO")





#=================OK
# def mark_attendance(self, i, n, d):
#     with open("attend.csv", "r+", newline="\n") as f:
#         conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="face_recognizer")
#         my_cursor = conn.cursor()
#         my_cursor.execute("select Id, Name, Dep from studentinfo ")
#         namee = my_cursor.fetchall()
#
#         myDataList = f.readlines()  # ['0308191073,thien,CCNA,22:07:51,16/06/2022,Preset'] ==>table all trong file csv
#         name_list = []
#         for line in myDataList:  # load từng dòng 1  ==>0308191073,thien,CCNA,22:07:51,16/06/2022,Preset
#             entry = line.split((","))  # tách theo dấu ','
#             name_list.append(entry[0]) #0308191073
#
#         for x, y, z in namee:
#             x = "".join(x)
#             y = "".join(y)
#             z = "".join(z)
#
#             if ((i not in name_list) and (n not in name_list) and (d not in name_list)):
#                 if (i in x) and (n in y) and (d in z):
#                     now = datetime.now()
#                     d1 = now.strftime("%d/%m/%Y")
#                     dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#                     f.writelines(f"\n{x},{y},{z},{dtString},{d1},YES")
#                 else:
#                     now = datetime.now()
#                     d1 = now.strftime("%d/%m/%Y")
#                     dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#                     f.writelines(f"\n{x},{y},{z},{dtString},{d1},NO")



#===========OK
# listdata=[]
# def mark_attendance(i, n, d):
#     with open("attend.csv", "r+", newline="\n") as f:  # mở file attend; vừa đọc vừa ghi
#         myDataList = f.readlines()  # ['1,0344777347,thien,CCNA,22:07:51,16/06/2022,Preset'] ==>table all trong file csv
#         name_list = []
#         for line in myDataList:  # load từng dòng 1  ==>1,0344777347,thien,CCNA,22:07:51,16/06/2022,Preset
#             entry = line.split((","))  # tách theo dấu ','
#             name_list.append(entry[0])  # tách là lấy phần tử thứ 1
#
#         if ((i not in name_list) and (n not in name_list) and (d not in name_list)):  # kiểm tra xem coi đã có phần tử name_list(csv) hay chưa
#             now = datetime.now()
#             d1 = now.strftime("%d/%m/%Y")
#             dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#             f.writelines(f"\n{i},{n},{d},{dtString},{d1},YES")
#             listdata.append((i,n,d))
#             print(listdata)
#
#             conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="face_recognizer")
#             my_cursor = conn.cursor()
#             my_cursor.execute("select Id, Name, Dep from studentinfo ")
#             namee = my_cursor.fetchall()
#             print(namee)
#
#             for si,sn,sd in listdata:
#                 for sqi,sqn, sqd in namee:
#                     if (si == sqi) and (sn == sqn) and (sd == sqd):
#                         continue
#                     else:
#                         now = datetime.now()
#                         d1 = now.strftime("%d/%m/%Y")
#                         dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
#                         f.writelines(f"\n{sqi},{sqn},{sqd},{dtString},{d1},NO")
#
#
#
# mark_attendance("0308191073", "thien","CCNA")
# mark_attendance("308191044", "son","CCNA")
# mark_attendance("0308191073", "thien","CCNA")

#
#
import csv


import os


listdata = []
def absent_attendance(i, n, d):
    global namee
    with open("attend.csv", "r+", newline="\n") as f:  # mở file attend; vừa đọc vừa ghi
        myDataList = f.readlines()  # ['1,0344777347,thien,CCNA,22:07:51,16/06/2022,Preset'] ==>table all trong file csv
        name_list = []

        for line in myDataList:  # load từng dòng 1  ==>0344777347
            entry = line.split((","))  # tách theo dấu ','
            name_list.append(entry[0])  # tách là lấy phần tử thứ 1

        if ((i not in name_list)):  # kiểm tra xem coi đã có phần tử name_list(csv) hay chưa
            listdata.append(i)
            print(listdata)
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f"\n{i},{n},{d},{dtString},{d1},YES")
            mystring = ",".join(listdata)
            conn = mysql.connector.connect(host="localhost", username="root", password="Thien@123",database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT Id, Name, Dep FROM studentinfo WHERE Id NOT IN ("+mystring+")")
            namee = my_cursor.fetchall()
            print(namee)
#Trong đó f là một object file được tạo ra khi mở file csv bằng hàm open(), và fieldnames để chỉ định các giá trị của key trong dictionary làm dòng header trong file csv.

    with open('absent.csv', 'w',newline="\n") as p:
        if 'namee' in globals():
            for idd, naa, dee in namee:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")  # đẩy ra giờ phút giây
                p.writelines(f"\n{idd},{naa},{dee},{dtString},{d1},NO")



absent_attendance("0308191073", "thien","CCNA")
absent_attendance("308191044", "son","CCNA")
absent_attendance("0308191065", "Quy","CCNP")


file1 = open("attend.csv", "a")
file2 = open("absent.csv", "r")
for line in file2:
    file1.write(line)

file1.close()
file2.close()

# def mark_attendance( i, n, d):
#     with open("attend.csv", "r+", newline="\n") as f:
#         myDataList = f.readlines()
#         name_list = []
#         for line in myDataList:
#             entry = line.split((","))
#             name_list.append(entry[0])
#
#         if ((i not in name_list) and (n not in name_list) and (d not in name_list)):
#             now = datetime.now()
#             d1 = now.strftime("%d/%m/%Y")
#             dtString = now.strftime("%H:%M:%S")
#             f.writelines(f"\n{i},{n},{d},{dtString},{d1},YES")
#
# mark_attendance("0308191073", "thien","CCNA")             ===========NOT IN && IN