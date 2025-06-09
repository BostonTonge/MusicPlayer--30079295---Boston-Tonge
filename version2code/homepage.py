import tkinter as tk
from tkinter import PhotoImage
import subprocess
import sys

window = tk.Tk()
window.title("Home Page")  # title 
window.geometry('565x350')  # dimension
window.resizable(width = 0, height =0) # non-resizable
window.eval('tk::PlaceWindow . center')
window.configure(border=10, relief="raised", bg="lightgrey")

Logo = PhotoImage(file="images/app_images/logo1.png")
TeReo = PhotoImage(file="images/app_images/button_tereo.png")
Pasifika = PhotoImage(file="images/app_images/button_pasifika.png")
Multicultural = PhotoImage(file="images/app_images/button_multicultural.png")
Pop = PhotoImage(file="images/app_images/button_pop.png")
Rap = PhotoImage(file="images/app_images/button_rap.png")
RB = PhotoImage(file="images/app_images/button_rb.png")
Country = PhotoImage(file="images/app_images/button_country.png")
Reggae = PhotoImage(file="images/app_images/button_reggae.png")
Rock = PhotoImage(file="images/app_images/button_rock.png")

def open_musicplayer(genre):
    window.destroy()
    if sys.platform.startswith("win"):
        subprocess.Popen(["python", "musicplayer.py", genre])
    else:
        subprocess.Popen(["python3", "musicplayer.py", genre])

# Button Row 1
button1 = tk.Button(window, image=TeReo, command=lambda: open_musicplayer("tereo"))
button1.place(x=0, y=80)
button2 = tk.Button(window, image=Pasifika, command=lambda: open_musicplayer("pasifika"))
button2.place(x=180, y=80)
button3 = tk.Button(window, image=Multicultural, command=lambda: open_musicplayer("multicultural"))
button3.place(x=360, y=80)
# Button Row 2
button4 = tk.Button(window, image=Pop, command=lambda: open_musicplayer("pop"))
button4.place(x=0, y=150)
button5 = tk.Button(window, image=Rap, command=lambda: open_musicplayer("rap"))
button5.place(x=180, y=150)
button6 = tk.Button(window, image=RB, command=lambda: open_musicplayer("rnb"))
button6.place(x=360, y=150)
# Button Row 3
button7 = tk.Button(window, image=Country, command=lambda: open_musicplayer("country"))
button7.place(x=0, y=220)
button8 = tk.Button(window, image=Reggae, command=lambda: open_musicplayer("reggae"))
button8.place(x=180, y=220)
button9 = tk.Button(window, image=Rock, command=lambda: open_musicplayer("rock"))
button9.place(x=360, y=220)

window.mainloop()
