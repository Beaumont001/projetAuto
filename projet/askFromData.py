import tkinter as tk
import json
from tkinter import *
import os

def welcomeBox():
    racine = tk.Tk()
    label = tk.Label(racine, text="Bienvenu dans le processus de création de code !")
    bouton = tk.Button(racine, text="Suivant", command=racine.quit)
    bouton["fg"] = "red"
    label.pack()
    bouton.pack()
    racine.mainloop()

def giveNUmberOfData():

    racine = Tk()
    entr1 = Entry(racine)
    label = Label(racine, text="Donner le nombre de data à stocker")
    label.grid(row =1, column =1)
    entr1.grid(row =2, column =1)
    bouton = Button(racine, text="Suivant", command=racine.quit)
    bouton["fg"] = "red"
    bouton.grid(row =3, column =1)
    racine.mainloop()
    return entr1.get()

def test(numOfData):
    fen1 = Tk()
    countLabel =0
    countEntr = 0
    tabOfVar = []
    listOfData = []
    mod = sys.modules[__name__]

    for i in range(0,numOfData):
        setattr(mod,"txt{}".format(i),1)
        setattr(mod,"entr{}".format(i),1)

    for a in dir(mod):
        if 'txt' in a:
            countLabel = countLabel +1
            a = Label(fen1, text ='champ n°'+ str(countLabel) +':')
            a.grid(row =countLabel, sticky =E)
            continue
            
        if 'entr' in a:
            countEntr = countEntr +1
            a = Entry(fen1)
            a.grid(row =countEntr, column =2)
            tabOfVar.append(a)
    
    bouton = Button(fen1, text="Suivant", command=fen1.quit)
    bouton["fg"] = "red"
    bouton.grid(row =countEntr +1, column =1)
    fen1.mainloop()
    for var in tabOfVar:
        listOfData.append(var.get().upper())
    return listOfData

num = giveNUmberOfData()
listOfD = test(int(num))
dictOfDt = {}
for i in listOfD:
    dictOfDt[i.replace(' ','_')] = i
input = json.dumps(dictOfDt)
print(input)
tabOfData = [num,input]
f1 = open('specData.txt', 'a')
f1.write(input)
f1.close()

# define the name of the directory to be created
path = "../test"
os.mkdir(path)


#welcomeBox()
