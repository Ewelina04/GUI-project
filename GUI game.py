from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pygame import mixer
import random
import time
import tkinter as tk

# 3 koła ratunkowe w pasku menu, po ich kliknięciu wyświetla się info że one coś tam robią
def tele():
    messagebox.showinfo("Dzwonimy do Twojego przyjaciela", "H: Witaj! Z tej strony Hubert Urbański z Milionerów.\nTwój przyjaciel gra właśnie o milion i potrzebuje Twojej pomocy przy pytaniu.\nMasz do dyspozycji 4 odpowiedzi.\nP: Myślę, że poprawna jest odpowiedź'...\ni jestem tego pewny na... Mogę się jednak mylić...\n")
def pol_na_pol():
    messagebox.showinfo("50/50", "Proszę o odrzucenie 2 błędnych odpowiedzi.\nDo wyboru pozostały:")
def publicznosc():
    messagebox.showinfo("pomoc publicznosci", "Proszę publiczność o zagłosowanie na poprawną państwa zdaniem odpowiedź.\nOto wyniki procentowe kolejno dla odp A, B, C i D:")

# teraz info co te kola robią bedzie się pojawiało w menu a te przyciski tak jak wcześniej, zostają bez zmian    
def info_tele():
    messagebox.showinfo("telefon do Twojego przyjaciela", "Wybierając to koło dzwonimy do Twojego przyjaciela, który pomaga Ci poprawnie odpowiedzieć i wygrać milion!!")
def info_pol_na_pol():
    messagebox.showinfo("50/50", "Wybierając to koło odrzucamy 2 błęde odpowiedzi.\nZwiększa to twoją szansę z 25% na 50% że wybierzesz poprawną odpowiedź i wygrasz milion!!")
def info_publicznosc():
    messagebox.showinfo("pomoc publicznosci", "Wybierając to koło proszę publiczność o zagłosowanie na poprawną ich zdaniem odpowiedź.\nPrzedstawiane są wyniki procentowe kolejno dla odp:\nA, B, C i D\nPubliczność może pomóc Ci poprawnie odpowiedzieć i wygrać milion!!")

    
# prowadzący po kliknięciu wyżwietla info o hubercie, takie jego cv i autopromocja ;-)
def akcjaAutor():
    messagebox.showinfo("Hubert", "jestem hubert urbański i prowadzę grę milionerzy w tvn\nod pon. do pt. o 20.55\nZapraszam!")

def akcja_przycisk ():
    print ("Czesc")


glowne_okno=Tk()
glowne_okno.state('zoomed') # od razu pojawia się okno gry full screen, wtedy wszystko widać, nic nie jest ucięte (raczej tak jest lepiej)

# dźwięk
file = 'milionmusic.mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()


# tworzone zdjęcie huberta
canvas_width = 300
canvas_height =300
plotno = Canvas(glowne_okno,
           width=canvas_width,
           height=canvas_height)
plotno.pack(side=TOP)
img = Image.open("h.jpg")
img = img.resize((320,320))
imgTk = ImageTk.PhotoImage(img)
plotno.create_image(145,162,image=imgTk)

#przyciski kół
img50na50 = tk.PhotoImage(file="50-50.jpg")
przycisk_50na50 = tk.Button(glowne_okno, image=img50na50 ,command=pol_na_pol)
przycisk_50na50.pack()
imgPublicznosc = tk.PhotoImage(file="publicznosc.jpg")
przycisk_publicznosc=Button(glowne_okno, image=imgPublicznosc ,command=publicznosc)
przycisk_publicznosc.pack()
imgTelefon = tk.PhotoImage(file="telefon.jpg")
przycisk_telefon=Button(glowne_okno, image=imgTelefon ,command=tele)
przycisk_telefon.pack()

pasekMenu = Menu(glowne_okno)
peirwszeMenu = Menu(pasekMenu, tearoff=0)

# nazwy okienek u góry(tytuły) po wcisnieciu poszczególnych kół z menu
peirwszeMenu.add_command(label="Telefon do przyjaciela", command=info_tele)
peirwszeMenu.add_command(label="pół na pół", command=info_pol_na_pol)
peirwszeMenu.add_command(label="publicznosc", command=info_publicznosc)

# dalsze menu po lewej u góry co się wyświetla
peirwszeMenu.add_command(label="wyjdz", command=glowne_okno.quit)
pasekMenu.add_cascade(label="koła ratunkowe", menu=peirwszeMenu)
pomocMenu = Menu(pasekMenu, tearoff=0)
pomocMenu.add_command(label="info o prowadzącym", command=akcjaAutor)
pasekMenu.add_cascade(label="Prowadzący", menu=pomocMenu)
glowne_okno.config(menu=pasekMenu)

glowne_okno.title("OKNO GRY")
glowne_okno.geometry("800x900")
glowne_okno.configure(bg='dark blue') #granatowy kolor tła gry


zestaw_pytan_1 = [['Przydomek wiedźmina Geralta wskazuje na to, że bohater sagi Andrzeja Sapkowskiego pochodzi z...','A. Vengerbergu','B. Rivii','C. Oxenfurtu','D. Tretogoru','B'],
['Jaką cześć liter w wyrazie "bajzel" stanowią samogłoski?','A. jedną trzecią',' B. jedną piątą','C. jedną czwartą','D. jedną drugą','A'],
['Na akord można:','A. spać','B. śpiewać','C. podróżować','D. pracować','D'],
['Gromada gadów to inaczej: ', 'A. Arachnida', 'B. Reptilia', 'C. Amphibia', 'D. Insecta', 'B']]

class Pytanie:
    def losuj(self):
        wylosowane_pytanie=random.choice(zestaw_pytan_1)
        zestaw_pytan_1.remove(wylosowane_pytanie)
        return wylosowane_pytanie

pytanie=Pytanie()
wylosowane = pytanie.losuj()
a=wylosowane[1]
b=wylosowane[2]
c=wylosowane[3]
d=wylosowane[4]
Label(glowne_okno,text=wylosowane[0], bg = 'dark blue', fg = 'white', font=("Arial",16,"italic"), padx = 20).pack(side=TOP) #granatowe tło przycisków lepiej to wygląga jako calość gry

# to te przyciski odpowiedzi A B C D i ten tekst nad nimi, 
# ladne kolorki, nie? mogą zostać
v = IntVar()
v.set(0)  # to zazanaczona wartosc początkowa czyli 0 = odpowiedzi A
languages = [
    (a),
    (b),
    (c),
    (d)
]
def ShowChoice():
    print(v.get())
Label(glowne_okno,
         text="""Poprawna odpowiedź na to pytanie to... :""",
         bg = 'dark blue',
         fg = 'white',
         font=("Arial",16,"italic"),
         padx = 20).pack(side=TOP)
# wygląd przycisków A B C D i ich umiejscowienie
for val, language in enumerate(languages):
    Radiobutton(glowne_okno,
                  text=language,
                  indicatoron = 0,
                  width = 20,
                  padx = 20,
                  variable=v,
                  command=ShowChoice,
                  font=("Curier",12,"bold"),
                  bg = "light blue",
                  activebackground = "dark red",
                  value=val).pack(anchor=S)


glowne_okno.mainloop()
