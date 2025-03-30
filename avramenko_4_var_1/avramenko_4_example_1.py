from tkinter import *

ventana = Tk()
V = IntVar(); m = IntVar()
ventana.title("Radiobutton")
ventana.geometry("200x150")

etiquental = Label(ventana, text = "Radio demos").place(x=20,y=20)

Color = Radiobutton(ventana,text="Color",variable=V,value=0).pack()
Query = Radiobutton(ventana,text="Query",variable=V,value=1).pack()
Input = Radiobutton(ventana,text="Input",variable=V,value=2).pack()
Open  = Radiobutton(ventana,text="Open", variable=V,value=3).pack()
Error = Radiobutton(ventana,text="Error",variable=V,value=4).pack()

ventana.mainloop()
