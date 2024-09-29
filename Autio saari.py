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
mantere_y = 363
apina_x = 66
apina_y = 160
kuoleman_todennakoisyys = 0.01
hataviesti = ["Ernesti", "ja" ,"Kernesti" "tässä", "terve!","Olemme", "autiolla",
               "saarella", "voisiko", "joku", "tulla", "sieltä", "sivistyneestä",
               "maailmasta", "hakemaan", "meidät","pois!", "Kiitos!"]



def viesti():
      h_viesti= random.choice(hataviesti)
      print(h_viesti) 


def ernesti_aseta_apina():
    #asettaa alku arvon apinalle ja lisää viestin apinalle ja yhden yrityksen
    #tekoälyltä otettu vähän pohjaa tähän koodi pätkään
    x,y = saari_x, saari_y-apina_y
    t = Thread(target=viesti)
    t.run()
    ernesti_yritykset['e_yritys'] += 1
    lähetä_apina_ernesti(x,y)


def lähetä_apina_ernesti(x,y):
    for _ in range(1):
        print(ernesti_yritykset)

        #tarkistaa pääsikö apina perille
        #tekoälyltä otettu vähän pohjaa tähän koodi pätkään
        if x >= ikkuna.winfo_width() - mantere_x:
                    winsound.Beep(700,1000)
                    canvas.delete("apina")
                    ernesti_selviytymiset['e_selviytyminen'] += 1
                    print(ernesti_selviytymiset)
                    print(ernesti_yritykset)
                    viesti()
                    break
        
        #tarkistaa tuliko apina syödyksi
        #tekoälyltä otettu vähän pohjaa tähän koodi pätkään 
        if random.random() < kuoleman_todennakoisyys:
                    print("apina tuli syödyksi.")
                    winsound.Beep(500,100)
                    canvas.delete("apina")
                    break
                          
        else:
            #liikuttaa apinaa 
            #tekoälyltä otettu vähän pohjaa tähän koodi pätkään
            print("apina on vielä elossa!")     
            winsound.Beep(200,100)
            canvas.delete("apina")
            canvas.create_image(x, y, anchor=tk.NW, image=apina_tk, tags="apina")
            ikkuna.after(1000, lähetä_apina_ernesti, x + 10, y)       

def kernesti_aseta_apina():
    #asettaa alku arvon apinalle ja lisää viestin apinalle ja yhden yrityksen
    #tekoälyltä otettu vähän pohjaa tähän koodi pätkään
    x,y = saari_x, saari_y+apina_y
    t = Thread(target=viesti)
    t.run()
    kernesti_yritykset['k_yritys'] += 1
    lähetä_apina_kernesti(x,y)


def lähetä_apina_kernesti(x,y):
    for _ in range(1):
        print(kernesti_yritykset)
        #tarkistaa pääsikö apina perille
        #tekoälyltä otettu vähän pohjaa tähän koodi pätkään
        if x >= ikkuna.winfo_width() - mantere_x:
                    winsound.Beep(700,1000)
                    canvas.delete("apina")
                    kernesti_selviytymiset['k_selviytyminen'] += 1
                    print(kernesti_selviytymiset)
                    print(kernesti_yritykset)
                    viesti()
                    break
        
        #tarkistaa tuliko apina syödyksi
        #tekoälyltä otettu vähän pohjaa tähän koodi pätkään  
        if random.random() < kuoleman_todennakoisyys:
                    print("apina tuli syödyksi.")
                    winsound.Beep(500,100)
                    canvas.delete("apina")
                    break
                          
        else:
            #liikuttaa apinaa
            #tekoälyltä otettu vähän pohjaa tähän koodi pätkään 
            print("apina on vielä elossa!")     
            winsound.Beep(200,100)
            canvas.delete("apina")
            canvas.create_image(x, y, anchor=tk.NW, image=apina_tk, tags="apina")
            ikkuna.after(1000, lähetä_apina_kernesti, x + 10, y)


def lähetä_kymmenen_erne():
       for _ in range (10):
              #käynistää apinan liikkeen threadin sisälle
              th= Thread(target=ernesti_aseta_apina)
              th.run()
              
              
def lähetä_kymmenen_kerne():
       for _ in range (10):
            #käynistää apinan liikkeen threadin sisälle
            th= Thread(target=kernesti_aseta_apina)
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


ikkuna = tk.Tk()
ikkuna.geometry("1000x800")


apina_img = Image.open("apina.PNG")  
apina_tk = ImageTk.PhotoImage(apina_img)


canvas = tk.Canvas(ikkuna, width=1000, height=800)
canvas.pack()


saari=ImageTk.PhotoImage(file="saari.PNG")
label=Label(ikkuna, image=saari)
label.place(x=0, y=200)


mantere=ImageTk.PhotoImage(file="mantere.PNG")
label=Label(ikkuna, image=mantere)
label.place(x=835, y=200)


btn = tk.Button(ikkuna, text="ernesti lähettää apinan", command=ernesti_aseta_apina)
btn.place(x=400,y=10)


btn = tk.Button(ikkuna, text="ernesti lähettää kymmenen apinaa", command=lähetä_kymmenen_erne)
btn.place(x=200,y=10)


btn = tk.Button(ikkuna, text="kernesti lähettää kymmenen apinaa", command=lähetä_kymmenen_kerne)
btn.place(x=750,y=10)


btn = tk.Button(ikkuna, text="kernesti lähettää apinan", command=kernesti_aseta_apina)
btn.place(x=600,y=10)


ikkuna.mainloop()