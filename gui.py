import tkinter as tk
from tkinter import messagebox
from dictionaries import *

fönster = tk.Tk()

def val_metod(var_val):
        val_get = var_val.get()
        print("Värdet är", val_get)
        if val_get == "Abbey Road":
            messagebox.showinfo(f"{val_get}", f"{musikalbum["Abbey Road"].show_info_music()}")
        elif val_get == "News of the World":
            messagebox.showinfo(f"{val_get}", f"{musikalbum["News of the World"].show_info_music()}")
        elif val_get == "Nevermind":
            messagebox.showinfo(f"{val_get}", f"{musikalbum["Nevermind"].show_info_music()}")
        elif val_get == "Jurassic Park":
            messagebox.showinfo(f"{val_get}", f"{filmer["Jurassic Park"].show_info_movie()}")
        elif val_get == "Titanic":
            messagebox.showinfo(f"{val_get}", f"{filmer["Titanic"].show_info_movie()}")
        elif val_get == "Pulp Fiction":
            messagebox.showinfo(f"{val_get}", f"{filmer["Pulp Fiction"].show_info_movie()}")
        elif val_get == "En världsomsegling under havet":
            messagebox.showinfo(f"{val_get}", f"{böcker["En världsomsegling under havet"].show_info_book()}")
        elif val_get == "Da Vinci-koden":
            messagebox.showinfo(f"{val_get}", f"{böcker["Da Vinci-koden"].show_info_book()}")
        elif val_get == "Röda Rummet":
            messagebox.showinfo(f"{val_get}", f"{böcker["Röda Rummet"].show_info_book()}")

def musik_metod():
    while True:
        huvudram.pack_forget()

        musik_ram = tk.Frame(fönster)
        musik_ram.pack()

        var_val = tk.StringVar(fönster)

        etikett = tk.Label(fönster, text="Välj ett album")
        etikett.pack(pady=20)

        abbeyroad_knapp = tk.Radiobutton(fönster, text="Abbey Road", value="Abbey Road", variable=var_val)
        abbeyroad_knapp.pack(pady=20)

        notw_knapp = tk.Radiobutton(fönster, text="News of the World", value="News of the World", variable=var_val)
        notw_knapp.pack(pady=20)

        nevermind_knapp = tk.Radiobutton(fönster, text="Nevermind", value="Nevermind", variable=var_val)
        nevermind_knapp.pack(pady=20)

        knapp = tk.Button(fönster, text="Klicka här för att ange svar", command=lambda: val_metod(var_val))
        knapp.pack(pady=20)

        fönster.mainloop()

def film_metod():
    while True:
        huvudram.pack_forget()

        val_ram = tk.Frame(fönster)
        val_ram.pack()

        var_val = tk.StringVar(val_ram)

        etikett = tk.Label(val_ram, text="Välj en film")
        etikett.pack(pady=20)

        jurassicpark_knapp = tk.Radiobutton(val_ram, text="Jurassic Park", value="Jurassic Park", variable=var_val)
        jurassicpark_knapp.pack(pady=20)

        titanic_knapp = tk.Radiobutton(val_ram, text="Titanic", value="Titanic", variable=var_val)
        titanic_knapp.pack(pady=20)

        pulpfiction_knapp = tk.Radiobutton(val_ram, text="Pulp Fiction", value="Pulp Fiction", variable=var_val)
        pulpfiction_knapp.pack(pady=20)

        knapp = tk.Button(val_ram, text="Klicka här för att ange svar", command=lambda: val_metod(var_val))
        knapp.pack(pady=20)

        fönster.mainloop()

def bok_metod():
    while True:
        huvudram.pack_forget()

        val_ram = tk.Frame(fönster)
        val_ram.pack()

        var_val = tk.StringVar(val_ram)

        etikett = tk.Label(val_ram, text="Välj en bok")
        etikett.pack(pady=20)

        evoh_knapp = tk.Radiobutton(val_ram, text="En världsomsegling under havet", value="En världsomsegling under havet", variable=var_val)
        evoh_knapp.pack(pady=20)

        davincikoden_knapp = tk.Radiobutton(val_ram, text="Da Vinci-koden", value="Da Vinci-koden", variable=var_val)
        davincikoden_knapp.pack(pady=20)

        rodarummet_knapp = tk.Radiobutton(val_ram, text="Röda Rummet", value="Röda Rummet", variable=var_val)
        rodarummet_knapp.pack(pady=20)

        knapp = tk.Button(val_ram, text="Klicka här för att ange svar", command=lambda: val_metod(var_val))
        knapp.pack(pady=20)

        fönster.mainloop()

def metod():
    while True:
        var_get = var.get()
        if var_get == "Musik":
            musik_metod()
        elif var_get == "Film":
            film_metod()
        elif var_get == "Bok":
            bok_metod()
        else:
            print("Fel")

huvudram = tk.Frame(fönster)
huvudram.pack()

var = tk.StringVar()

etikett = tk.Label(huvudram, text="Välj ett alternativ")
etikett.pack(pady=20)

musik_knapp = tk.Radiobutton(huvudram, text="Musik", value="Musik", variable=var)
musik_knapp.pack(pady=20)

film_knapp = tk.Radiobutton(huvudram, text="Film", value="Film", variable=var)
film_knapp.pack(pady=20)

bok_knapp = tk.Radiobutton(huvudram, text="Bok", value="Bok", variable=var)
bok_knapp.pack(pady=20)

knapp = tk.Button(huvudram, text="Klicka här för att ange svar", command=metod)
knapp.pack(pady=20)

fönster.mainloop()








