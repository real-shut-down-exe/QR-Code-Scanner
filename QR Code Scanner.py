import tkinter as tk # pip install tk
import pyperclip # pip install pyperclip
from pyzbar import pyzbar # pip install pyzbar
from PIL import Image # pip install Pillow
from cfonts import render, say # pip install python-cfonts
from tkinter import filedialog

# Banner
banner1 = render('QR Code', colors=['red', 'white'], align='center')
banner2 = render('Scanner', colors=['red', 'white'], align='center')
print(banner1)
print(banner2)

# Select File Path
print("Select File Path:")
root = tk.Tk()
root.withdraw()

# Open file with windows file dialog
qrSrc = filedialog.askopenfilename()
print("Dosya Yolu:",qrSrc,"\n")

# SRC
print("QR Code Source:")
qrcode = pyzbar.decode(Image.open(qrSrc))
src = qrcode[0].data.decode('ascii')
print(src)

# Copie Link
print("\nLink Copied ...")
pyperclip.copy(src)

# Wait
input("")
