import xml.etree.ElementTree as ET
import os.path
from os import path
import sys,os
import configparser
import json
from openpyxl import Workbook
from openpyxl import load_workbook
import pathlib
import tkinter
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import OptionMenu
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from os.path import basename
import os.path
import win32com.client

import pythoncom
import win32api

def findText(a):
    tree = ET.parse(a)
    for elem in tree.iter():
        if "Artifact" in elem.tag:
            if len(elem.attrib) > 0:
                for inner in elem.attrib:
                    if inner == "TextAnnotation":
                        memoryElem = elem
                        print(memoryElem.get("TextAnnotation"))
                        lp = memoryElem.get("TextAnnotation").split(",")
                        return lp
                        

def transformTabIntoDct(tab):
    newDict = dict()
    for element in tab:
        newDict[element.upper()] = element
    return newDict



def selectFile(msg):
    """Display a popup to ask the user to select a fill to use

    Args:
        the message to be displayed in the popup

    Returns:
        the path of the file name selected  

    """
    
    popup = tkinter.Tk()
    popup.title("Faire un choix de fichier")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="OK", command = popup.destroy)
    B1.pack()
    popup.mainloop()

    root = tkinter.Tk()
    root.withdraw()
    pathFile = askopenfilename(parent=root)
    root.destroy()

    return pathFile


def check(a):
    print(path.exists(a))


a = selectFile('test')
check(a)
tab=findText(a)
di=transformTabIntoDct(tab)
print(di)