import sys
import os.path

from tkinter import *
from configparser import ConfigParser

import ConfigCreate

# Read app configuration file or create new file when not present

parser = ConfigParser()
cfgfile = "config.ini"

if not os.path.exists(cfgfile):
    ConfigCreate.cfgWrite()
else:
    parser.read(cfgfile)

x_init = parser.get('main', 'x_init')
y_init = parser.get('main', 'y_init')
width = parser.get('main', 'width')
height = parser.get('main', 'height')
winparam = str(width+'x'+height+'+'+x_init+'+'+y_init)


def savepos():
    # Save current window position and size

    global parser
    global cfgfile

    geometry = GUI.geometry()
    act_width = GUI.winfo_width()
    act_height = GUI.winfo_height()
    temp, act_x_init, act_y_init = geometry.split("+")
    parser.read(cfgfile)
    parser.set('main', 'width', str(act_width))
    parser.set('main', 'height', str(act_height))
    parser.set('main', 'x_init', str(act_x_init))
    parser.set('main', 'y_init', str(act_y_init))
    file = open(cfgfile, 'w')
    parser.write(file, space_around_delimiters=False)
    file.close()


if __name__ == "__main__":
    GUI = Tk()
    GUI.geometry(winparam)
    GUI.title('Moje Pliki')
    GUI.configure(bg='dark gray')

    # Create app menu
    menubar = Menu(GUI)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Pliki", underline=0, menu=filemenu)
    filemenu.add_command(label="Wyjście", underline=1, command=quit)
    commenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Polecenia", underline=0, menu=commenu)
    commenu.add_command(label="Wyjście", underline=1, command=quit)
    viewmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Widok", underline=0, menu=viewmenu)
    viewmenu.add_command(label="Wyjście", underline=1, command=quit)
    cfgmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Konfiguracja", underline=0, menu=cfgmenu)
    cfgmenu.add_command(label="Zapisz ustawienia", underline=1, command=savepos)
    GUI.config(menu=menubar)

    # Status bar

#    statusbar = Label(GUI, text="on the way…", bd=1, relief=SUNKEN, anchor=W)
#    statusbar.pack(side=BOTTOM, fill=X)

    GUI.mainloop()
