# Author: Deendayal Kumawat
"""
Date: 11/01/21
Descriptions: Window Activator
"""
from PIL import ImageTk, Image
import subprocess
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import platform
import socket
import re
import uuid
import json
import peutils
import logging
import os

# ***********Main GUI******************#
root = Tk()
root.title("Activator Version 2.0")
root.wm_iconbitmap('user.ico')

# *****************Heading of GUI************************#
Head = Label(text='Activator', font='Lucida 20 bold',
             bg='black', fg='#F4C724', padx=5, pady=5)
Head.pack(pady=10, fill=X)


# ****************Get System Information******************#


def getSystem_Information():
    # traverse the info
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []

    # arrange the string into clear info
    for item in Id:
        new.append(str(item.split("\r")[:-1]))
    for i in new:
        #  print(i[2:-2])
        data = i[2:-2]
        try:
            # get username of pc
            username = os.getlogin()
            with open(f"C:\\Users\\{username}\\Desktop\\system_info.txt", "a") as file:
                file.write(str(data).capitalize())
                file.write("\n")
                # pyauto.alert(text="File Generated Successfully",title="Success")
                file.close
        except:
            # messagebox.showerror("Error", "Something went wrong try again!!!")
            print("Something went wrong!!!!")

    # File Generating Message
    response = False

    if response != True:
        messagebox.showinfo("Success", "File Generated Successfully")
        # print("Hello")
    else:
        response == False
        messagebox.showerror("Error", "Something went wrong try again!!!")


# ****************Window 10 All Version ******************#


def activateWindow10():
    subprocess.call([r'window10.bat'])


# ****************Window 10 All Version end ******************#

# ****************Window 8 8.1 All Version ******************#


def activateWindow8():
    subprocess.call([r'window8.bat'])


# ****************Window 8 8.1 All Version end ******************#

# ****************Window 7 All Version ******************#


def activateWindow7():
    subprocess.call([r'window7.bat'])


# ****************Window 7 All Version end ***************#


# ****************Microsoft Office All Version ******************#
def activateOffice():
    #  messagebox.showwarning("Working", "Available on Next Update")
    # Toplevel object which will
    # be treated as a new window
    global officeWindow
    officeWindow = Toplevel(root)
    officeWindow.wm_iconbitmap(
        'office.ico')

    # sets the title of the
    # Toplevel widget
    officeWindow.title("Microsoft Office")

    # sets the geometry of toplevel
    officeWindow.geometry('600x400')
    officeWindow.resizable(width=False, height=False)

    # A Label widget to show in toplevel
    Label(officeWindow,
          text="Microsoft Office", font='Lucida 20 bold',
          bg='black', fg='#F4C724', padx=5, pady=5).pack(pady=10, fill=X)

    # Button for Office
    btn1 = Button(officeWindow, text=' Microsoft Office 2003  ',
                  background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=office2003)
    btn2 = Button(officeWindow, text=' Microsoft Office 2007  ',
                  background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=office2007)

    btn3 = Button(officeWindow, text=' Microsoft Office 2010 ',
                  background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=office2010)

    btn4 = Button(officeWindow, text=' Microsoft Office  2013 ',
                  background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=office2013)
    btn5 = Button(officeWindow, text=' Microsoft Office  2016 ',
                  background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=office2016)
    btn6 = Button(officeWindow, text=' Microsoft Office  2019 ',
                  background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=office2019)

    btn1.place(x=70, y=110)
    btn2.place(x=300, y=110)
    btn3.place(x=70, y=200)
    btn4.place(x=300, y=200)
    btn5.place(x=70, y=280)
    btn6.place(x=300, y=280)


def office2003():
    # subprocess.call([r'office2003.bat'])
    # function to open a new window

    # Toplevel object which will
    # be treated as a new window
    office2003 = Toplevel(root)
    office2003.wm_iconbitmap(
        'office.ico')

    # sets the title of the
    # Toplevel widget
    office2003.title("Office 2003")

    # sets the geometry of toplevel
    office2003.geometry('500x400')
    root.resizable(width=False, height=False)

    # A Label widget to show in toplevel
    Label(office2003,
          text="Serial number Microsoft Office 2003", fg='#000000', font='Lucida 20 bold', padx=5, pady=5).pack()

    serialKey2003 = ''' 
    1. C3P4R-8JGP4-CF3FC-KQMCX-4V67M\n
    2. KY6HJ-BDYBC-2FXGJ-W29B3-TQGBB\n
    3. HQB4W-XFFTW-YQ7QP-FJQK2-X2FDY\n
    4. J9972-F8QC7-34R72-DWKP7-8K8YB\n
    5. KJ9W7-FH68K-9PC3Q-YJYBJ-HMYQY\n
    6. F3W2H-RGTTQ-GQPT2-3QKD2-4TKXM\n
    7. GWH28-DGCMP-P6RC4-6J4MT-3HFDY


    '''
    Label(office2003,
          text=f"{serialKey2003}", fg='#000000', font='Lucida 10 bold', padx=5, pady=5).pack()


def office2007():
    # Toplevel object which will
    # be treated as a new window
    office2007 = Toplevel(root)
    office2007.wm_iconbitmap(
        'office.ico')
    # sets the title of the
    # Toplevel widget
    office2007.title("Office 2007")

    # sets the geometry of toplevel
    office2007.geometry('500x800')
    root.resizable(width=False, height=False)

    # A Label widget to show in toplevel
    Label(office2007,
          text="Serial number Microsoft Office 2007", fg='#000000', font='Lucida 20 bold', padx=5, pady=5).pack()

    serialKey2007 = '''
    1.  F3DJD-6FFQ4-XQTQF-PGK47-8MDQ8\n
    2.  VBWYT-BBWKV-P86YX-G642C-3C3D3\n
    3.  R2WBR-GG6HV-GTPMB-RG9B9-YBJVM\n
    4.  TT3M8-H3469-V89G6-8FWK7-D3Q9Q\n
    5.  KJYPC-VDYR6-82242-PFR9R-688VM\n
    6.  KGFVY-7733B-8WCK9-KTG64-BC7D8\n
    7.  MTP6Q-D868F-448FG-B6MG7-3DBKT\n
    8.  DPK3W-F6FGP-9JDGJ-23VQM-TRHYB\n
    9.  XC84W-M642D-2QDWY-YTKMM-RWJQW\n
    10. VB48G-H6VK9-WJ93D-9R6RM-VP7GT\n
    11. RV29T-JVXGX-968YT-RFC79-RRT33\n
    12. HCFPT-K86VV-DCKH3-87CCR-FM6HW\n
    13. FR6D9-89FTC-87WC6-MM4PB-G6VYB\n
    14. TQ7MT-BQTJD-V4MJ6-J6KT8-RP2VW\n
    15. J67F8-BB7GM-8VPH2-8YMXP-K49QQ\n
    16. WRWWX-G9MMD-X4B8X-7JQP3-CMD93\n
    17. RYC22-PRMXB-8HP8W-384PD-GXHX3\n
    18. VM98J-C9X4C-MM7YX-93G64-BJMK3\n
    19  VK626-MQWCC-FXXWY-W2H6F-KVKQQ\n
    20. PGHBF-6K7PC-J9989-BGGJD-TKT3Q\n
        '''
    Label(office2007,
          text=f"{serialKey2007}", fg='#000000', font='Lucida 10 bold', padx=5, pady=5).pack()


def office2010():
    print("Office 2010")
    subprocess.call([r'office2010.bat'])


def office2013():
    print("Office 2013")
    subprocess.call([r'office2013.bat'])


def office2016():
    print("Office 2016")
    subprocess.call([r'office2016.bat'])


def office2019():
    print("Office 2019")
    subprocess.call([r'office2019.bat'])


# ****************Microsoft Office All Version End ******************#

# ****************About Me ******************#
# function to open a new window
# on a button click

# global img


def aboutMe():
    # from PIL import ImageTk, Image
    # Toplevel object which will
    # be treated as a new window
    aboutme = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    aboutme.title("About Me")

    # A Label widget to show in toplevel
    # self.canvas =Canvas(aboutme,width = 250 ,height = 200)
    # self.canvas.pack()
    # # self.img = PhotoImage(file ="ptoj.png")
    # self.img = ImageTk.PhotoImage(Image.open("Images/ptoj.png"))
    # print(self.img)
    # self.canvas.create_image(20, 20, anchor=NW, image=self.img)
    # self.canvas.image=self.img
    Label(aboutme, text="About Me", fg='#000000',
          font='Lucida 20 bold').pack(side="top")
    email = "codewithcup.developer@gmail.com "
    descriptions = ''' 
        I'm Java,Python and Android Developer \n 
        I've experiences in multiple technologies \n 
        For any Queries Feel Free Contact us on\n 
    '''
    Label(aboutme, text=f'''{descriptions}
        Email:-{email}''', font='Lucida 10 bold').pack()

    # sets the geometry of toplevel
    aboutme.geometry('350x300')
    root.resizable(width=False, height=False)


# ****************About Me End ******************#


def clearJunckFiles():
    print("junk files")
    subprocess.call([r'junkCleaner.bat'])


# Button for Main Window
b1 = Button(root, text=' Get System Information  ',
            background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=getSystem_Information)

b2 = Button(root, text=' Windows 10 All Version  ',
            background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=activateWindow10)

b3 = Button(root, text='Windows 8 8.1 All Version',
            background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=activateWindow8)

b4 = Button(root, text=' Windows 7 All    Version  ',
            background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=activateWindow7)
b5 = Button(root, text=' Ms  Office   All    Version  ',
            background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=activateOffice)
b6 = Button(root, text='             Clear Junk            ',
            background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=clearJunckFiles)
b7 = Button(root, text='                About Me           ',
            background='Green', fg='#000000', font='Lucida 10 bold', padx=5, pady=5, command=aboutMe)

b1.place(x=70, y=120)
b2.place(x=300, y=120)
b3.place(x=70, y=200)
b4.place(x=300, y=200)
b5.place(x=70, y=280)
b6.place(x=300, y=280)
b7.place(x=70, y=350)

# # Status Bar
# sbar = Label(text='By Deendayal Kumawat', font='Helvetica 10 bold',
#              relief=SUNKEN, anchor='w', padx=10)
# sbar.pack(side=BOTTOM, fill=X)

# Footer of GUI
Head = Label(text='By Deendayal Kumawat', font='Lucida 10 bold',
             bg='black', fg='#F4C724', padx=5, pady=5)
Head.pack(side=BOTTOM, pady=1, fill=X)

root.geometry('600x450')
root.resizable(width=False, height=False)
root.mainloop()
