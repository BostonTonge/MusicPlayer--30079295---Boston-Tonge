import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
window.title("Home Page")  # title 
window.geometry('565x350')  # dimension
window.resizable(width = 0, height =0) # non-resizable
window.eval('tk::PlaceWindow . center')
window.configure(border=10, relief="raised", bg="lightgrey")

Logo = PhotoImage(file="images/logo1.png")
TeReo = PhotoImage(file="images/button_tereo.png")
Pasifika = PhotoImage(file="images/button_pasifika.png")
Multicultural = PhotoImage(file="images/button_multicultural.png")
Pop = PhotoImage(file="images/button_pop.png")
Rap = PhotoImage(file="images/button_rap.png")
RB = PhotoImage(file="images/button_rb.png")
Country = PhotoImage(file="images/button_country.png")
Reggae = PhotoImage(file="images/button_reggae.png")
Rock = PhotoImage(file="images/button_rock.png")



#Button Row 1
#button1 = tk.Button(window,bg="steelblue", fg="white",text="TeReo",font=("Impact", 20))
button1 = tk.Button(window,image=TeReo)
button1.place(x=0,y=80)
button2 = tk.Button(window,image=Pasifika)
button2.place(x=180,y=80)
button3 = tk.Button(window, image=Multicultural)
button3.place(x=360,y=80)
#Button Row 2
button4 = tk.Button(window,image=Pop)
button4.place(x=0,y=150)
button5 = tk.Button(window,image=Rap)
button5.place(x=180,y=150)
button6 = tk.Button(window,image=RB)
button6.place(x=360,y=150)
#Button Row 3
button7 = tk.Button(window,image=Country)
button7.place(x=0,y=220)
button8 = tk.Button(window,image=Reggae)
button8.place(x=180,y=220)
button9 = tk.Button(window,image=Rock)
button9.place(x=360,y=220)

window.mainloop()
