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

canvas_width = 300
canvas_height =300
plotno = Canvas(glowne_okno,
           width=canvas_width,
           height=canvas_height)
plotno.pack()
img = Image.open("h.jpg")
img = img.resize((300,305))
imgTk = ImageTk.PhotoImage(img)
plotno.create_image(200,200,image=imgTk)

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
glowne_okno.geometry("700x550")
v = IntVar()
v.set(0)  
languages = [
    ("A"),
    ("B"),
    ("C"),
    ("D")
]
def ShowChoice():
    print(v.get())
Label(glowne_okno,
         text="""Poprawna odpowiedź na to pytanie to... :""",
         font=("Times New Roman",11,"italic"),
         padx = 20).pack()
for val, language in enumerate(languages):
    Radiobutton(glowne_okno,
                  text=language,
                  indicatoron = 0,
                  width = 20,
                  padx = 20,
                  variable=v,
                  command=ShowChoice,
                  font=("Curier",10,"bold"),
                  bg = "white",
                  activebackground = "light blue",
                  value=val).pack(anchor=S)


glowne_okno.mainloop()
