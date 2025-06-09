import tkinter as tk
from tkinter import PhotoImage
from tkinter import Text


window = tk.Tk()
window.title("Home Page")  # title 
window.geometry('565x600')  # dimension
window.resizable(width = 0, height =0) # non-resizable
window.eval('tk::PlaceWindow . center')
window.configure(border=10, relief="raised", bg="lightgrey")

#Declarng and Importing Images
Avatar = PhotoImage(file="images/app_images/profilepicture.png")
Spotify = PhotoImage(file="images/app_images/spotifylogo.png")
Youtube = PhotoImage(file="images/app_images//youtubelogo.png")
Instagram = PhotoImage(file="images/app_images//instagramlogo.png")





#Avatar Image
label1 = tk.Label(window, image=Avatar)
label1.place(x=232,y=0)
#Name of Artist
label3 = tk.Label(window,text="Name", foreground="Blue", bg= 'lightgrey', font=("Segoe Script", 10, "bold"))
label3.place(x=235,y=65)

#Label of text box to display infromation about Artist
label3 = tk.Label(window,text="About The Artist", foreground="Blue", bg= 'lightgrey', font=("Segoe Script", 10, "bold"))
label3.place(x=200,y=100)
#Text of Information
text1 = Text(window, width=40, height=10)
text1.place(x=100, y=135)

#Social Media Handles

#Spotify 
label6 = tk.Label(window, image=Spotify)
label6.place(x=130, y=400)
text2 = Text(window, width=25, height=1)
text2.place(x=170, y=400)
#Youtube
label7 = tk.Label(window, image=Youtube)
label7.place(x=130, y=440)
text3 = Text(window, width=25, height=1)
text3.place(x=170, y=440)
#Instagram
label8 = tk.Label(window, image=Instagram)
label8.place(x=130, y=480)
text4 = Text(window, width=25, height=1)
text4.place(x=170, y=480)

window.mainloop()
