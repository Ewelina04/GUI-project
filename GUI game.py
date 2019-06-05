from tkinter import *
from tkinter import messagebox


def tele():
    messagebox.showinfo("Dzwonimy do Twojego przyjaciela", "H: Witaj! Z tej strony Hubert Urbański z Milionerów.\nTwój przyjaciel gra właśnie o milion i potrzebuje Twojej pomocy przy pytaniu.\nMasz do dyspozycji 4 odpowiedzi.\nP: Myślę, że poprawna jest odpowiedź'...\ni jestem tego pewny na... Mogę się jednak mylić...\n")
def pol_na_pol():
    messagebox.showinfo("50/50", "Proszę o odrzucenie 2 błędnych odpowiedzi.\nDo wyboru pozostały:")
def publicznosc():
    messagebox.showinfo("pomoc publicznosci", "Proszę publiczność o zagłosowanie na poprawną państwa zdaniem odpowiedź.\nOto wyniki procentowe kolejno dla odp A, B, C i D:")

def akcjaAutor():
    messagebox.showinfo("Hubert", "jestem hubert urbański i prowadzę grę milionerzy w tvn\nod pon. do pt. o 20.55\nZapraszam!")

def akcja_przycisk ():
    print ("Czesc")


glowne_okno=Tk()
pasekMenu = Menu(glowne_okno)
peirwszeMenu = Menu(pasekMenu, tearoff=0)
peirwszeMenu.add_command(label="Telefon do przyjaciela", command=tele)
peirwszeMenu.add_command(label="pół na pół", command=pol_na_pol)
peirwszeMenu.add_command(label="publicznosc", command=publicznosc)

peirwszeMenu.add_command(label="wyjdz", command=glowne_okno.quit)
pasekMenu.add_cascade(label="koła ratunkowe", menu=peirwszeMenu)
pomocMenu = Menu(pasekMenu, tearoff=0)
pomocMenu.add_command(label="info o prowadzącym", command=akcjaAutor)
pasekMenu.add_cascade(label="Prowadzący", menu=pomocMenu)
glowne_okno.config(menu=pasekMenu)



glowne_okno.title("OKNO GRY")
glowne_okno.geometry("700x450")
przycisk1 = Button(glowne_okno, text="Powitanie", command=akcja_przycisk)
przycisk1.grid()
odp_a= Button(glowne_okno, text="A", fg = "red")
odp_a.place(x=30, y=80)
odp_b= Button(glowne_okno, text="B", fg = "blue")
odp_b.place(x=80, y=80)
odp_c= Button(glowne_okno, text="C", fg = "green")
odp_c.place(x=30, y=150)
odp_d= Button(glowne_okno, text="D", fg = "purple")
odp_d.place(x=80, y=150)

glowne_okno.mainloop()
