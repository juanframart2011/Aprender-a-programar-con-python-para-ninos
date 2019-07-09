from tkinter import*
import random

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

def rectangulo_aleatorio(ancho,alto, relleno):
    x1 = random.randrange(ancho)
    y1 = random.randrange(alto)
    
    x2 = x1 + random.randrange(ancho)
    y2 = y1 + random.randrange(alto)

    canvas.create_rectangle(x1,y1,x2,y2, fill=relleno)

def escribiendo():
    canvas.create_text(150,100,text='estoy escribiendo e tkinter')
