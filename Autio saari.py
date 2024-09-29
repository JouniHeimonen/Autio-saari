import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *
from PIL import Image
import winsound
from threading import Thread
import random


saari_x = 194
saari_y = 368
mantere_x = 161
apina_y = 120
kuoleman_todennakoisyys = 0.05
hataviesti = ["Ernesti", "ja" ,"Kernesti","tässä", "terve!","Olemme", "autiolla",
               "saarella", "voisiko", "joku", "tulla", "sieltä", "sivistyneestä",
               "maailmasta", "hakemaan", "meidät","pois!", "Kiitos!"]


def ernesti_aseta_apina():
    #asettaa alku arvon apinalle ja lisätään viestin apinalle ja lisätään yhden yrityksen
    #tekoälyltä otettu vähän pohjaa tähän koodi pätkään
    x,y = saari_x, saari_y-apina_y-40
    lähetä_apina_ernesti(x,y)

def lähetä_apina_ernesti(x,y):
        for _ in range(1):
        #tarkistaa pääsikö apina perille
        #tekoälyltä otettu vähän pohjaa tähän koodi pätkään
            if x >= ikkuna.winfo_width() - mantere_x:
                    winsound.Beep(700,1000)
                    canvas.delete("apina")
                    break          
            else:
            #liikuttaa apinaa ja päästää äänen joka askeleella
            #tekoälyltä otettu vähän pohjaa tähän koodi pätkään    
                winsound.Beep(200,100)
                canvas.delete("apina")
                canvas.create_image(x, y, anchor=tk.NW, image=apina_tk, tags="apina")
                ikkuna.after(1000, lähetä_apina_ernesti, x + 50, y)
                 

def kernesti_aseta_apina():
    #asettaa alku arvon apinalle ja lisätään viestin apinalle ja lisätään yhden yrityksen
    #tekoälyltä otettu vähän pohjaa tähän koodi pätkään
    x,y = saari_x, saari_y+apina_y
    lähetä_apina_kernesti(x,y)

def lähetä_apina_kernesti(x,y):
        for _ in range(1):
        #tarkistaa pääsikö apina perille
        #tekoälyltä otettu vähän pohjaa tähän koodi pätkään
            if x >= ikkuna.winfo_width() - mantere_x:
                    winsound.Beep(700,1000)
                    canvas.delete("apina")
                    break
            else:
            #liikuttaa apinaa ja päästää äänen joka askeleella
            #tekoälyltä otettu vähän pohjaa tähän koodi pätkään     
                winsound.Beep(200,100)
                canvas.delete("apina")
                canvas.create_image(x, y, anchor=tk.NW, image=apina_tk, tags="apina")
                ikkuna.after(1000, lähetä_apina_kernesti, x + 50, y) 

def ernesti_aseta_apina_viesti():
    x,y = saari_x, saari_y-apina_y-40
    h_viesti= random.choice(hataviesti)
    print(h_viesti)
    lähetä_apina_ernesti_viesti(x,y,h_viesti)


def lähetä_apina_ernesti_viesti(x,y,h_viesti):
    for _ in range(1):

        #tarkistaa pääsikö apina perille ja jos pääsi perille antaa viestin
        if x >= ikkuna.winfo_width() - mantere_x:
                    winsound.Beep(700,1000)
                    canvas.delete("apina")
                    print(h_viesti)
                    break
                                 
        else: 
            winsound.Beep(300,100)
            canvas.delete("apina")
            canvas.create_image(x, y, anchor=tk.NW, image=apina_tk, tags="apina")
            ikkuna.after(1000, lähetä_apina_ernesti_viesti, x + 50, y,h_viesti)


def kernesti_aseta_apina_viesti():

    x,y = saari_x, saari_y+apina_y
    #asettaa yhden sanan hätäviestistä apinalle
    h_viesti= random.choice(hataviesti)
    print(h_viesti)
    lähetä_apina_kernesti_viesti(x,y,h_viesti)


def lähetä_apina_kernesti_viesti(x,y,h_viesti):
    for _ in range(1):
        #tarkistaa pääsikö apina perille ja jos pääsi perille antaa viestin
        if x >= ikkuna.winfo_width() - mantere_x:
                    winsound.Beep(700,1000)
                    canvas.delete("apina")
                    print(h_viesti)
                    break    
        else:  
            winsound.Beep(300,100)
            canvas.delete("apina")
            canvas.create_image(x, y, anchor=tk.NW, image=apina_tk, tags="apina")
            ikkuna.after(1000, lähetä_apina_kernesti_viesti, x + 50, y,h_viesti)


def ernesti_aseta_apina_hai():

    x,y = saari_x, saari_y-apina_y-40
    h_viesti= random.choice(hataviesti)
    print(h_viesti)
    #lisää yhden yrityksen taulukkoon
    ernesti_yritykset['e_yritys'] += 1
    lähetä_apina_ernesti_hai(x,y,h_viesti)


def lähetä_apina_ernesti_hai(x,y,h_viesti):
    for _ in range(1):

        if x >= ikkuna.winfo_width() - mantere_x:
                    winsound.Beep(700,1000)
                    canvas.delete("apina")
                    #lisää yhden selviytymiseen jokaisesta apinasta joka pääsi mantereelle
                    ernesti_selviytymiset['e_selviytyminen'] += 1
                    print(ernesti_selviytymiset)
                    print(ernesti_yritykset)
                    print(h_viesti)
                    break
        
        #tarkistaa tuliko apina syödyksi
        if random.random() < kuoleman_todennakoisyys:
                    print("apina tuli syödyksi.")
                    winsound.Beep(500,100)
                    canvas.delete("apina")
                    break
                          
        else:    
            winsound.Beep(300,100)
            canvas.delete("apina")
            canvas.create_image(x, y, anchor=tk.NW, image=apina_tk, tags="apina")
            ikkuna.after(1000, lähetä_apina_ernesti_hai, x + 50, y,h_viesti)                     


def kernesti_aseta_apina_hai():

    x,y = saari_x, saari_y+apina_y
    h_viesti= random.choice(hataviesti)
    print(h_viesti)
    kernesti_yritykset['k_yritys'] += 1
    lähetä_apina_kernesti_hai(x,y,h_viesti)


def lähetä_apina_kernesti_hai(x,y,h_viesti):
    for _ in range(1):

        if x >= ikkuna.winfo_width() - mantere_x:
                    winsound.Beep(700,1000)
                    canvas.delete("apina")
                    kernesti_selviytymiset['k_selviytyminen'] += 1
                    print(kernesti_selviytymiset)
                    print(kernesti_yritykset)
                    print(h_viesti)
                    break
        #tarkistaa tuliko apina syödyksi
        #tekoälyltä otettu vähän pohjaa tähän koodi pätkään 
        if random.random() < kuoleman_todennakoisyys:
                    print("apina tuli syödyksi.")
                    winsound.Beep(500,100)
                    canvas.delete("apina")
                    break                  
        else:  
            winsound.Beep(300,100)
            canvas.delete("apina")
            canvas.create_image(x, y, anchor=tk.NW, image=apina_tk, tags="apina")
            ikkuna.after(1000, lähetä_apina_kernesti_hai, x + 100, y,h_viesti) 

def lähetä_viesti_erne():
      #ernestin apina viestin Threadiin
      th=Thread(target=ernesti_aseta_apina_viesti)
      th.run()

def lähetä_viesti_kerne():
      #kernestin apina viestin Threadiin
      th=Thread(target=kernesti_aseta_apina_viesti)
      th.run()      

def lähetä_kymmenen_erne():
       for _ in range (10):
              #pistää apina hai vaaran kanssa Threadiin ja toistaa kymmenen kertaa
              th= Thread(target=ernesti_aseta_apina_hai)
              th.run()
              
              
def lähetä_kymmenen_kerne():
       for _ in range (10):
            #pistää apina hai vaaran kanssa Threadiin ja toistaa kymmenen kertaa
            th= Thread(target=kernesti_aseta_apina_hai)
            th.run()
              

ernesti_yritykset = {
    'e_yritys': 0
}


ernesti_selviytymiset = {
    'e_selviytyminen': 0
}


kernesti_yritykset = {
    'k_yritys': 0
}


kernesti_selviytymiset = {
    'k_selviytyminen': 0
} 

#tkinterin ikkunan luominen
ikkuna = tk.Tk()
ikkuna.geometry("1000x800")

#apina kuvan luonti
apina_img = Image.open("apina.PNG")  
apina_tk = ImageTk.PhotoImage(apina_img)

#canvasin luonti
canvas = tk.Canvas(ikkuna, width=1000, height=800)
canvas.pack()

#saari kuvan luonti
saari=ImageTk.PhotoImage(file="saari.PNG")
label=Label(ikkuna, image=saari)
label.place(x=0, y=200)

#mantere kuvan luonti
mantere=ImageTk.PhotoImage(file="mantere.PNG")
label=Label(ikkuna, image=mantere)
label.place(x=835, y=200)

#lähetää ernestin apinan
btn = tk.Button(ikkuna, text="erne lähettää apinan", command=ernesti_aseta_apina)
btn.place(x=10,y=10)
#lähettää ernestin apinan viestin kanssa
btn = tk.Button(ikkuna, text="erne lähettää apinan viestillä", command=lähetä_viesti_erne)
btn.place(x=150,y=10)
#lähettää ernestin apinan hai vaaran kanssa
btn = tk.Button(ikkuna, text="erne lähettää apinan viestillä (hai vaara)", command=ernesti_aseta_apina_hai)
btn.place(x=10,y=50)
#lähettää kymmenen apinaa ernestiltä
btn = tk.Button(ikkuna, text="erne lähettää kymmenen apinaa", command=lähetä_kymmenen_erne)
btn.place(x=250,y=50)

#lähetää kernestin apinan
btn = tk.Button(ikkuna, text="kerneä lähettää apinan", command=kernesti_aseta_apina)
btn.place(x=600,y=10)
#lähettää kernestin apinan viestin kanssa
btn = tk.Button(ikkuna, text="kerne lähettää apinan viestillä", command=lähetä_viesti_kerne)
btn.place(x=750,y=10)
#lähettää kernestin apinan hai vaaran kanssa
btn = tk.Button(ikkuna, text="kerne lähettää apinan viestillä (hai vaara)", command=kernesti_aseta_apina_hai)
btn.place(x=500,y=50)
#lähettää kymmenen apinaa kernestiltä
btn = tk.Button(ikkuna, text="kerne lähettää kymmenen apinaa", command=lähetä_kymmenen_kerne)
btn.place(x=750,y=50)


ikkuna.mainloop()