import random
import tkinter as tk
from tkinter import ttk
import time
import datum

lower_bound = 1
upper_bound = 100
zaehler = 1

def overtaking():
    global lower_bound
    global upper_bound
    lower_bound = int(lower_entry.get())
    upper_bound = int(upper_entry.get())
    new_Round()

def create_secret():
    global secret_Number
    secret_Number = random.randint(lower_bound, upper_bound)
    global Anweisung_1
    lt = time.localtime()
    actual_hour = lt[3]
    actual_min = lt[4]
    Anweisung_1 = "Es wurde um {:02d}:{:02d} eine Zufallszahl zwischen {}  und  {} generiert.".format(actual_hour, actual_min, lower_bound, upper_bound)
    Anweisung3 = "Wähle eine Ganzzahl zwischen {} und {}:".format(lower_bound, upper_bound)
   
def enter_return(event):
    check_Secret()

def check_Secret():
    global zaehler
    guess = int(Guess_entry.get())
    print("Versuch: {:>3d}: {:>4d}".format(zaehler, guess), end=' ')
    
    if guess == secret_Number:
        print(" ist gleich")
        print(" Neue Runde ".center(80, '='))
        antwort = ("Yeahh, das ist korrekt")
        anzahl_value.set("Du hast {} Versuche benötigt, um die korrekte Zahl zu erraten!".format(zaehler))

    elif guess < secret_Number:
       print("ist kleiner")
       zaehler += 1
       antwort = ("Die gesuchte Zahl ist größer als {}!".format(guess))

    else:
       print("ist größer")
       zaehler += 1
       antwort = ("Die gesuchte Zahl ist kleiner als {}".format(guess))
    antwort_value.set(antwort)


def new_Round():
    global zaehler
    zaehler = 1
    anzahl_value.set("")
    create_secret()
    lt = time.localtime()
    actual_hour = lt[3]
    actual_min = lt[4]
    anweisung1_value.set("Es wurde um {:02d}:{:02d} eine Zufallszahl zwischen {}  und  {} generiert.".format(actual_hour, actual_min, lower_bound, upper_bound))
    anweisung2_value.set("Wähle eine Ganzzahl zwischen {} und {}:".format(lower_bound, upper_bound))
    antwort_value.set("")
    guess_value.set("")

root = tk.Tk()
date = datum.datetime()
root.title("{} zum Zahlenratespiel 1".format(date[0]))
root.geometry("500x500")
root.resizable(False, False)
create_secret()

Anweisung2 = "Deine Aufgabe ist es zu erraten, welche Zahl es ist."
Anweisung3 = "Wähle eine Ganzzahl zwischen {} und {}:".format(lower_bound, upper_bound)
guess = None

lower_value = tk.StringVar(value=str(lower_bound))
upper_value = tk.StringVar(value=str(upper_bound))
anweisung1_value = tk.StringVar(value=Anweisung_1)
anweisung2_value = tk.StringVar(value=Anweisung3)
guess_value = tk.StringVar()

lower_label = ttk.Label(root, text="Untergrenze:", font=("Arial", 8))
lower_label.pack(fill="x", padx=5, pady=3)

lower_entry = ttk.Entry(root, textvariable=lower_value, font=("Arial", 12))
lower_entry.pack(fill="x", padx=5, pady=3)

upper_label = ttk.Label(root, text="Obergrenze:", font=("Arial", 8))
upper_label.pack(fill="x", padx=5, pady=3)

upper_entry = ttk.Entry(root, textvariable=upper_value, font=("Arial", 12))
upper_entry.pack(fill="x", padx=5, pady=3)

input_Button = ttk.Button(root, text="neue Grenzen übernehmen", command=overtaking)
input_Button.pack(fill="x", padx=5, pady=3)

Anweisung1_label = ttk.Label(root, textvariable=anweisung1_value, font=("Arial", 10))
Anweisung1_label.pack(fill="x", padx=5, pady=3)

Anweisung2_label = ttk.Label(root, text=Anweisung2, font=("Arial", 10))
Anweisung2_label.pack(fill="x", padx=5, pady=3)

Anweisung3_label = ttk.Label(root, textvariable=anweisung2_value, font=("Arial", 10))
Anweisung3_label.pack(fill="x", padx=5, pady=3)

Guess_entry = ttk.Entry(root, textvariable=guess_value, font=("Arial", 12))
Guess_entry.bind('<Return>', enter_return)
Guess_entry.pack(fill="x", padx=5, pady=3)

guess_Button = ttk.Button(root, text="eingegebene Zahl testen", command=check_Secret)
guess_Button.pack(fill="x", padx=5, pady=3)

antwort_value = tk.StringVar()
antwort_label = ttk.Label(root, textvariable=antwort_value, font=("Arial", 10))
antwort_label.pack(fill="x", padx=5, pady=3)

anzahl_value = tk.StringVar()
anzahl_label = ttk.Label(root, textvariable=anzahl_value, font=("Arial", 10))
anzahl_label.pack(fill="x", padx=5, pady=3)

new_Round_Button = ttk.Button(root, text="Neue Runde", command=new_Round)
new_Round_Button.pack(fill="x", padx=5, pady=5)

quit_Button = ttk.Button(text="Programm beenden", command=root.destroy)
quit_Button.pack(side="bottom", pady=5)

root.mainloop()


