from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pygame import mixer
import random
import time
import tkinter as tk 

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


pasekMenu = Menu(glowne_okno)
peirwszeMenu = Menu(pasekMenu, tearoff=0)

# nazwy okienek u góry(tytuły) po wcisnieciu poszczególnych kół z menu
peirwszeMenu.add_command(label="Telefon do przyjaciela", command=info_tele)
peirwszeMenu.add_command(label="pół na pół", command=info_pol_na_pol)
peirwszeMenu.add_command(label="publicznosc", command=info_publicznosc)

# dalsze menu po lewej u góry co się wyświetla
peirwszeMenu.add_command(label="wyjdz", command=glowne_okno.quit)
pasekMenu.add_cascade(label="MENU", menu=peirwszeMenu)
pomocMenu = Menu(pasekMenu, tearoff=0)
pomocMenu.add_command(label="info o prowadzącym", command=akcjaAutor)
pasekMenu.add_cascade(label="PROWADZĄCY", menu=pomocMenu)
glowne_okno.config(menu=pasekMenu)

glowne_okno.title("OKNO GRY")
glowne_okno.geometry("800x900")
glowne_okno.configure(bg='dark blue') #granatowy kolor tła gry


zestaw_pytan_1 = [['Przydomek wiedźmina Geralta wskazuje na to, że bohater sagi Andrzeja Sapkowskiego pochodzi z...','A. Vengerbergu','B. Rivii','C. Oxenfurtu','D. Tretogoru',1],
['Jaką cześć liter w wyrazie "bajzel" stanowią samogłoski?','A. jedną trzecią',' B. jedną piątą','C. jedną czwartą','D. jedną drugą',0],
['Na akord można:','A. spać','B. śpiewać','C. podróżować','D. pracować',3],
['Gromada gadów to inaczej: ', 'A. Arachnida', 'B. Reptilia', 'C. Amphibia', 'D. Insecta', 1],
['W którym z miast znajdują się korty Flushing Meadows?', 'A. w Londynie', 'B. w Paryżu', 'C. w Nowym Jorku', 'D. w Wiedniu', 2],
['Co jest głównym składnikiem maści ichtiolowej?', 'A. tlenek cynku', 'B. szkielet ryb karpiowatych', 'C. łupki bitumiczne','D. tran', 2],
['Na strychu suszy się 13 par białych i 9 par czarnych skarpetek. Jest tam tak ciemno, że nie widać ich kolorów. Ile pojedynczych skarpetek powinno się wziąć, by być pewnym, że dwie będą w tym samym kolorze?', 'A.5', 'B.13', 'C.3', 'D.14', 2],
['Który aktor urodził się w roku opatentowania kinematografu braci Lumière?', 'A. Rudolph Valentino', 'B. Humphrey Bogart', 'C. Charlie Chaplin', 'D. Fred Astaire', 0],
['Kto był pierwszym królem Zjednoczonych Włoch?', 'A. Fryderyk II', 'B. Karol V', 'C. Mikołaj I', 'D. Wiktor Emanuel II', 3],
['Magazyn "Time" ogłosił w lipcu 2015 r. ranking 10 najbogatszych osób w historii powszechnej. Kto z nich znalazł się najwyżej?', 'A. cesarz Shenzong (Chiny,XI w.)', 'B. Czyngis-chan (Mongolia,XII w.)', 'C. Bill Gates (USA,XX/XXI w.)', 'D. Oktawian August (Rzym, I w. n.e.)', 3],
['Yeren to: ', 'A. Bohater jednej z bajek w stylu anime', 'B. Tradycyjna walijska potrawa', 'C. Chiński odpowiednik Wielkiej Stopy', 'D. Imię żony Kim Dzong Una', 3],
['System kanałów na rzece Huang He zaplanował i zlecił wykonanie:', 'A. Mao Zedong', 'B. Yu', 'C. Vladimir Putin', 'D. Marco Polo', 1],
['Z którym państwem Wielka Brytania toczyła konflikt zbrony o Falklandy w 1982r.?', 'A. z Chile', 'B. z Kolumbią', 'C. z Argentyną', 'D. z Brazylią', 2],
['Bouillabaisse to potrawa, z której słynie:', 'A. Bordeaux', 'B. Genua', 'C. Wenecja', 'D. Marsylia', 3]]


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

def przyciskWybor():
    if v.get()== wylosowane[5]:
        messagebox.showinfo("Poprawna odpowiedz!")
    else:
        messagebox.showinfo("Niestety to błędna odpowiedz..")

# to te przyciski odpowiedzi A B C D i ten tekst nad nimi, 
# ladne kolorki, nie? mogą zostać
v = IntVar()
v.set(0)  # to zazanaczona wartosc początkowa,domyślna czyli 0 == odp A, ale można to zmienić żeby nie było że hubert sugeruje odpowiedź 
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
                  selectcolor = "orange",
                  font=("Curier",12,"bold"),
                  bg = "light blue",
                  activebackground = "dark red",
                  value=val).pack(anchor=S)
przyciskZatwierdzania=Button(glowne_okno,
                                text="Zatwierdz odpowiedz",
                                width=15,
                                padx=20,
                                command=przyciskWybor,
                                font=("Curier",12,"bold"))
przyciskZatwierdzania.pack()
#przyciski kół
def brakKola():
    messagebox.showinfo("Brak koła","Już wykorzystałeś to koło ratunkowe")
def tele():
    messagebox.showinfo("Dzwonimy do Twojego przyjaciela", "H: Witaj! Z tej strony Hubert Urbański z Milionerów.\nTwój przyjaciel gra właśnie o milion i potrzebuje Twojej pomocy przy pytaniu.\nMasz do dyspozycji 4 odpowiedzi.\nP: Myślę, że poprawna jest odpowiedź'...\ni jestem tego pewny na... Mogę się jednak mylić...\n")
    przycisk_telefon.destroy()
    przycisk_telefon_Red = Button(glowne_okno, image=imgTelefonRed ,command=brakKola)
    przycisk_telefon_Red.pack()
def pol_na_pol():
    messagebox.showinfo("50/50", "Proszę o odrzucenie 2 błędnych odpowiedzi.\nDo wyboru pozostały:")
    przycisk_50na50.destroy()
    przycisk_50na50_Red = Button(glowne_okno, image=img50na50Red ,command=brakKola)
    przycisk_50na50_Red.pack()
def publicznosc():
    messagebox.showinfo("pomoc publicznosci", "Proszę publiczność o zagłosowanie na poprawną państwa zdaniem odpowiedź.\nOto wyniki procentowe kolejno dla odp A, B, C i D:")
    przycisk_publicznosc.destroy()
    przycisk_publicznosc_Red = Button(glowne_okno, image=imgPublicznoscRed ,command=brakKola)
    przycisk_publicznosc_Red.pack()

img50na50 = tk.PhotoImage(file="50-50.jpg")
img50na50Red = tk.PhotoImage(file="50-50Red.jpg")
przycisk_50na50 = tk.Button(glowne_okno, image=img50na50 ,command=pol_na_pol)
przycisk_50na50.pack()

imgTelefon = tk.PhotoImage(file="telefon.jpg")
imgTelefonRed = tk.PhotoImage(file="telefonRed.jpg")
przycisk_telefon=Button(glowne_okno, image=imgTelefon ,command=tele)
przycisk_telefon.pack()


imgPublicznosc = tk.PhotoImage(file="publicznosc.jpg")
imgPublicznoscRed = tk.PhotoImage(file="publicznoscRed.jpg")
przycisk_publicznosc=Button(glowne_okno, image=imgPublicznosc ,command=publicznosc)
przycisk_publicznosc.pack()
glowne_okno.mainloop()
