from tkinter import *

coordinat = [700, 250]
window = Tk()
window.title("Online Banking Terminal")
window.geometry("800x500+{}+{}".format(coordinat[0], coordinat[1]))
btn = Button(window, text="Hello", activebackground='green')

btn.pack()


