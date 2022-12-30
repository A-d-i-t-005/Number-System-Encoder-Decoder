#Imports
from tkinter import *
from base64 import *

#Start-Up Window
root = Tk()
root.title('Encoder/Decoder')
root.geometry('400x250')
root.configure(background = 'White')
mainframe = Frame(root, height = 230, width = 380, bg = '#0d84b6')
mainframe.place(relx = 0.5, rely = 0.5, anchor = CENTER)
head = Label(mainframe, text = 'Encoder - Decoder' 
            ,font = ('Segoe UI Variable Display Light', 35,'underline')
            , bg = '#0d84b6',height = 20, width = 150)            
head.place(relx = 0.501, rely = 0.19, anchor = CENTER)
text = Label(mainframe
            ,text = 'Binary, Octal, Decimal, Hexadecimal, Base 64\nEncoding and Decoding'
            ,font = ('Segoe UI Variable Display Light', 15)
            ,bg = '#0d84b6',height = 5, width = 100)       
text.place(relx = 0.5, rely = 0.6, anchor = CENTER)

#Main Window
def entries():
    global mainframe2
    mainframe.destroy()
    root.geometry('720x900')
    root.configure(background = '#ade7ff')
    mainframe2 = Frame(root, height = 800, width = 550, background = '#363636')
    mainframe2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    Title = Label(mainframe2, text = 'Encoder/Decoder'
                  ,font = ('Segoe UI Variable Display Light', 30, 'bold'))
    Title.place(relx = 0.5, rely = 0.07, anchor = CENTER)
    
    label1 = Label(mainframe2, text = 'ASCII:', font = ('Ariel, 14'))
    label1.place(relx = 0.5, rely = 0.14, anchor = CENTER)
    asc = Entry(mainframe2, width = 80)
    asc.place(relx = 0.5, rely = 0.17, anchor = CENTER)

    label2 = Label(mainframe2, text = 'Decimal:', font = ('Ariel, 14'))
    label2.place(relx = 0.5, rely = 0.29, anchor = CENTER)
    deci = Entry(mainframe2, width = 80)
    deci.place(relx = 0.5, rely = 0.32, anchor = CENTER)    
    
    label3 = Label(mainframe2, text = 'Binary:', font = ('Ariel, 14'))
    label3.place(relx = 0.5, rely = 0.44, anchor = CENTER)
    binn = Entry(mainframe2, width = 80)
    binn.place(relx = 0.5, rely = 0.47, anchor = CENTER)
    
    label4 = Label(mainframe2, text = 'Octal:', font = ('Ariel, 14'))
    label4.place(relx = 0.5, rely = 0.59, anchor = CENTER)
    octt = Entry(mainframe2, width = 80)
    octt.place(relx = 0.5, rely = 0.62, anchor = CENTER)
    
    label5 = Label(mainframe2, text = 'Hexadecimal:', font = ('Ariel, 14'))
    label5.place(relx = 0.5, rely = 0.74, anchor = CENTER)
    hexa = Entry(mainframe2, width = 80)
    hexa.place(relx = 0.5, rely = 0.77, anchor = CENTER)

    label6 = Label(mainframe2, text = 'Base 64:', font = ('Ariel, 14'))
    label6.place(relx = 0.5, rely = 0.89, anchor = CENTER)
    base = Entry(mainframe2, width = 80)
    base.place(relx = 0.5, rely = 0.92, anchor = CENTER)
    
    button1 = Button(mainframe2, text = 'Enter', command = lambda: asciii_(asc))
    button1.place(relx = 0.85, rely = 0.19)
    button2 = Button(mainframe2, text = 'Enter', command = lambda: decimal(deci))
    button2.place(relx = 0.85, rely = 0.34)
    button3 = Button(mainframe2, text = 'Enter', command = lambda: binary_(binn))
    button3.place(relx = 0.85, rely = 0.49)
    button4 = Button(mainframe2, text = 'Enter', command = lambda: octal_(octt))
    button4.place(relx = 0.85, rely = 0.64)
    button5 = Button(mainframe2, text = 'Enter', command = lambda: hex_(hexa))
    button5.place(relx = 0.85, rely = 0.79)
    button6 = Button(mainframe2, text = 'Enter', command = lambda: base64(base))
    button6.place(relx = 0.85, rely = 0.94)

    button_reset = Button(mainframe2, text = 'Reset', command = lambda: reset())
    button_reset.place(relx = 0.75, rely = 0.94)
    
#Button Which Displays Main Window        
initiate = Button(mainframe, text = 'Open', width = 10, command = entries)
initiate.place(relx = 0.4, rely = 0.8)

#Function to Convert Decimal to Binary, Octal, Hexadecimal, Base 64
#r is Decimal Representation of the Number
def rep(r): 
    r1 = r
    r = r.split()
    asciii,binary,octal,hexadecimal = str(), str(), str(), str()
    for n in r:
        asciii = asciii + chr(int(n))
        binary = binary + bin(int(n))[2:]
        octal = octal + oct(int(n))[2:]
        hexadecimal = hexadecimal + hex(int(n))[2:]
    hexadecimal = hexadecimal.upper()
    string_bytes = asciii.encode('ascii')
    bytes = b64encode(string_bytes)
    base_64 = bytes.decode('ascii')
    
    global label_a, label_b, label_d, label_o, label_h, label_64
    label_a = Label(mainframe2, text = asciii, width = 68, bg = 'White')
    label_a.place(relx = 0.5, rely = 0.17, anchor = CENTER)
    label_d = Label(mainframe2, text = r1, width = 68, bg = 'White')
    label_d.place(relx = 0.5, rely = 0.32, anchor = CENTER)    
    label_b = Label(mainframe2, text = binary, width = 68, bg = 'White')
    label_b.place(relx = 0.5, rely = 0.47, anchor = CENTER)
    label_o = Label(mainframe2, text = octal,width = 68, bg = 'White')
    label_o.place(relx = 0.5, rely = 0.62, anchor = CENTER)
    label_h = Label(mainframe2, text = hexadecimal,width = 68, bg = 'White')
    label_h.place(relx = 0.5, rely = 0.77, anchor = CENTER)
    label_64 = Label(mainframe2, text = base_64,width = 68, bg = 'White')
    label_64.place(relx = 0.5, rely = 0.92, anchor = CENTER)

#Function to Delete Existing Labels for Taking Another Input
def reset():
    label_a.destroy()
    label_b.destroy()
    label_d.destroy()
    label_o.destroy()
    label_h.destroy()
    label_64.destroy()

#Functions to Recieve Input from User and To Convert Input to Decimal
def decimal(d): 
    y = d.get()
    rep(y)
     
def asciii_(a):
    word1 = str()
    z1 = a.get()
    for p in z1:
        word1 = word1 + str(ord(p)) + ' '
    rep(word1)

def binary_(b):
    word2 = str()
    z2 = b.get()
    z2 = str(z2).split()
    for s in z2:
        word2 = word2 + str(int(s, 2)) + ' '
    rep(word2)
    
def octal_(o):
    word3 = str()
    z3 = o.get()
    z3 = str(z3).split()
    for s in z3:
        word3 = word3 + str(int(s, 8)) + ' '
    rep(word3)

def hex_(h):
    word4 = str()
    z4 = h.get()
    z4 = z4.split()
    for m in z4:
        word4 = word4 + str(int(str(m), 16)) + ' '
    rep(word4) 

def base64(e):
    z5 = e.get()
    base64_bytes = z5.encode('ascii')
    word5_bytes = b64decode(base64_bytes)
    word5 = word5_bytes.decode('ascii')
    
    w = str()
    for p in word5:
        w = w + str(ord(p)) + ' '
    rep(w)    
    
mainloop()
