from cgitb import reset
from glob import glob
from ipaddress import collapse_addresses
import os, time
from tkinter import *
from tkinter import messagebox

import black

# LIJST VARIABELEN
scherm = Tk()

# VARIABELEN VOOR DE SCHERMEIGENSCHAPPEN
titel = "Oefenen op Buttons"
breedte = "500"
hoogte = "500"
afmetingen = breedte + "x" + hoogte
# icoon = "favicon.ico"
achtergrondkleur = "#387389"

# VARIABELEN VOOR DE KNOPPEN
naam = "Ik ben een knoppeke"
achtergrond = "#25b9f0"
voorgrond = "white"
image = PhotoImage(file="./image.png")

# FUNCTIES
def geklikt():
    print("Jippie je hebt op knop 1 geklikt!")


def informatie():
    messagebox.showinfo("BERICHT", "BOE")


def waarschuwing():
    messagebox.showwarning("BELANGRIJK", "Nog 1X klikken en de pc wordt afgesloten")


def foutmelding():
    messagebox.showerror("ERROR", "Je pc is gecrasht, klik niet op ok!")


def afsluiten():
    if messagebox.askyesno("KIEZEN", "Wil je de pc afsluiten?"):
        messagebox.showinfo("AFSLUITEN", "Klik nog eens")
        time.sleep(3)
        os.system("shutdown -s")
    else:
        messagebox.showinfo("AFSLUITEN", "Goed gekozen")


def kleur_veranderen():
    global knop6
    knop6.configure(bg="white")
    knop6.configure(fg="black")


def onbruikbaar():
    global knop7
    knop7.configure(state="disabled")
    knop7.configure(bg="white")


def reset():
    global knop7
    knop7.configure(state="active")


# AANMAKEN KNOPPPEN

knop1 = Button(scherm, text=naam, command=informatie)

knop2 = Button(
    scherm, text="informatie", bg="red", overrelief="sunken", command=informatie
)
knop3 = Button(
    scherm, text="red alert", fg="green", relief="sunken", command=waarschuwing
)
knop4 = Button(scherm, text="image")

knop5 = Button(scherm, text="Shut down", width=20, height=10, command=afsluiten)

knop6 = Button(scherm, text="knop6", fg="white", bg="black", command=kleur_veranderen)

knop7 = Button(
    scherm,
    text="knop7",
    fg="white",
    bg="black",
    width=5,
    height=10,
    padx=10,
    pady=10,
    command=onbruikbaar,
)

knop8 = Button(scherm, text="reset", width=1, height=10, command=reset)

# INSTELLEN EIGENSCHAPPEN SCHERM

scherm.title(titel)
scherm.geometry(afmetingen)
# scherm.wm_iconbitmap (icoon)
scherm.configure(bg=achtergrondkleur)

# PLAATSEN KNOPPEN OP HET SCHERM
knop1.grid()
knop2.grid()
knop3.grid()
knop4.grid()
knop5.grid()
knop6.grid()
knop7.grid()
knop8.grid()


# HOOFDPROGRAMMA

scherm.mainloop()  # altijd de functie mainloop oproepen
# deze kijkt na of er ergens iets gebeurt (muisklik, druk op knop,...) op je scherm ook al heb je dat nu niet nodig
