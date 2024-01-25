import tkinter as tk
from tkinter import Button, Label, Canvas
import threading
import time
import random


def toggle_instrument(instrument):
    # Funció per canviar l'estat de l'instrument (encès/apagat)
    print(f"{instrument} toggled")

def toggle_start_stop():
    # Funció per canviar l'estat d'iniciar/parar
    print("Start/Stop toggled")

def change_ad_banner():
    # Funció del fil dimoni per canviar banners de publicitat
    ads = ["publicitat1.png", "publicitat2.png", "publicitat3.png"]

    while True:
        random_ad = random.choice(ads)
        ad_image = Image.open(random_ad)
        ad_photo = ImageTk.PhotoImage(ad_image)

        ad_canvas.config(width=ad_image.width, height=ad_image.height)
        ad_canvas.create_image(0, 0, anchor=tk.NW, image=ad_photo)
        ad_canvas.image = ad_photo

        time.sleep(5)  # Canvia el banner cada 5 segons

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Seqüenciador de Sons")

    # Instruments i fils corresponents
    instruments = ["Kick", "Snare", "Hi-Hat"]

    # Interfície gràfica per a instruments
    for i, instrument in enumerate(instruments):
        checkbox = tk.Checkbutton(root, text=instrument, command=lambda inst=instrument: toggle_instrument(inst))
        checkbox.grid(row=i, column=0, padx=10, pady=10)

    # Botó d'iniciar/parar
    start_stop_button = Button(root, text="Iniciar", command=toggle_start_stop)
    start_stop_button.grid(row=len(instruments), column=0, padx=10, pady=10)

    # Canvas per mostrar banners de publicitat
    ad_canvas = Canvas(root, width=200, height=100)
    ad_canvas.grid(row=len(instruments) + 1, column=0, padx=10, pady=10)

    # Fil dimoni per a banners de publicitat
    ad_thread = threading.Thread(target=change_ad_banner)
    ad_thread.daemon = True
    ad_thread.start()

    root.mainloop()
