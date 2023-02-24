from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os


### configuration fenetre:

root = Tk()
root.title("Lecteur MP3")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

mixer.init()

### code pr ouvrir allez chercher les fichiers audio
def ouvrir_fichier():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                playlist.delete(1, END)
                playlist.insert(END,song)

### Paramètre de la musique
def lireson():
    music_name = playlist.get(ACTIVE)
    #print(music_name[0:-1])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.set_volume(0.7)
    mixer.music.play()
    music.config(text=music_name[0:-2])

#icone
imagee_icon = PhotoImage(file=r"C:lecteurmp3python\note-de-musique.png")
root.iconphoto(False, imagee_icon)

Entete = PhotoImage(file=r"C:lecteurmp3python\entete.png")
Label(root, image=Entete, bg="#0f1a2b", width=1587, height=250).pack()

logo = PhotoImage(file=r"C:lecteurmp3python\casque.png")
Label(root, image=logo, bg="#ffffff").place(x=65, y=115)

play_button = PhotoImage(file=r"C:lecteurmp3python\play1.png")
Button(root, image=play_button, bg="#0f1a2b", bd=0, command=lireson).place(x=95, y=300)


stop_button = PhotoImage(file=r"C:lecteurmp3python\stop.png")
Button(root, image=stop_button, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=10, y=425)

resume_button = PhotoImage(file=r"C:lecteurmp3python\resume.png")
Button(root, image=resume_button, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=100, y=550)

pause_button = PhotoImage(file=r"C:lecteurmp3python\pause.png")
Button(root, image=pause_button, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=175, y=425)

volume_moin_button = PhotoImage(file=r"C:lecteurmp3python\speaker-g35ce87ee6_640.png" ,width=50, height=50)
Button(root, image=volume_moin_button, bg="#0f1a2b", bd=0, command=mixer.music.set_volume).place(x=5 ,y=525)

###label

music = Label(root, text="", font="arial15", fg="white", bg="#0f1a2b")
music.place(x=150, y=360, anchor="center")

###Music
Menu = PhotoImage(file=r"C:lecteurmp3python\menu.png")
Label(root, image=Menu, bg="#0f1a2b", width=575, height=550).pack(padx=12, pady=8, side=RIGHT)

music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=330, y=350, width=560, height=300)

Button(root, text="Ouvrir Fichier", width=15, height=2, font="arial 10 bold", fg="white", bg="#21b3de", command=ouvrir_fichier).place(x=330, y=300)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font="arial 10", bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)
root.mainloop()


### je n'ai pas pus réussir à coder le script concernant le volume