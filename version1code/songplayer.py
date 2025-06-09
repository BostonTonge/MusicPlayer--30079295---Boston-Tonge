import tkinter as tk
from tkinter import PhotoImage


window = tk.Tk()
window.title("Music Page")  # title 
window.geometry('570x650')  # dimension
window.resizable(width = 0, height =0) # non-resizable
window.eval('tk::PlaceWindow . center') # Puts window in center of page
window.configure(border=10, relief="raised", bg="lightgrey")

#Importing and Defining Images
LeftArrow = PhotoImage(file="images/button_leftarrow.png")
DownArrow = PhotoImage(file="images/button_downarrow.png")
RightArrow = PhotoImage(file="images/button_rightarrow.png")

#Return Button

#Arrow Button
button1 = tk.Button(window,image=LeftArrow)
button1.place(x=0,y=300)
label2 = tk.Label(window, text="Previous Song", foreground="Blue", bg= 'lightgrey', font=("Segoe Script", 10, "bold"))
label2.place(x=30,y=380)
button2 = tk.Button(window,image=DownArrow)
button2.place(x=180,y=300)
label3 = tk.Label(window, text="See More Information", foreground="Blue", bg= 'lightgrey', font=("Segoe Script", 10, "bold"))
label3.place(x=190,y=380)
button3 = tk.Button(window,image=RightArrow)
button3.place(x=360,y=300)
label4 = tk.Label(window, text="Next Song", foreground="Blue", bg= 'lightgrey', font=("Segoe Script", 10, "bold"))
label4.place(x=410,y=380)





window.mainloop()
