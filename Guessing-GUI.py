import random
import tkinter as tk
from tkinter import ttk
import time

lower_bound = 1
upper_bound = 100
zaehler = 1

def overtaking():
    global lower_bound
    global upper_bound
    lower_bound = int(lower_entry.get())
    upper_bound = int(upper_entry.get())

def create_secret():
    global secret_Number
    secret_Number = random.randint(lower_bound, upper_bound)
    global Anweisung_1
    lt = time.localtime()
    actual_hour = lt[3]
    actual_min = lt[4]
    Anweisung_1 = "Es wurde um {:02d}:{:02d} eine Zufallszahl zwischen {}  und  {} generiert.".format(actual_hour, actual_min, lower_bound, upper_bound)
    Anweisung3 = "Wähle eine Ganzzahl zwischen {} und {}:".format(lower_bound, upper_bound)
   
    
def check_Secret():
    global zaehler
    guess = int(Guess_entry.get())
    
    if guess == secret_Number:
        antwort = ("Yeahh, das ist korrekt")
        anzahl_value.set("Du hast {} Versuche benötigt, um die korrekte Zahl zu erraten!".format(zaehler))

    elif guess < secret_Number:
       zaehler += 1
       antwort = ("Die gesuchte Zahl ist größer als Deine geratene Zahl!")

    else:
       zaehler += 1
       antwort = ("Die gesuchte Zahl ist kleiner als Deine geratene Zahl!")
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

root = tk.Tk()
root.title("Zahlenratespiel")
root.geometry("800x600")
create_secret()

Anweisung2 = "Deine Aufgabe ist es zu erraten, welche Zahl es ist."
Anweisung3 = "Wähle eine Ganzzahl zwischen {} und {}:".format(lower_bound, upper_bound)
guess = None

lower_value = tk.StringVar(value=str(lower_bound))
upper_value = tk.StringVar(value=str(upper_bound))
anweisung1_value = tk.StringVar(value=Anweisung_1)
anweisung2_value = tk.StringVar(value=Anweisung3)
guess_value = tk.StringVar()

lower_label = ttk.Label(root, text="Untergrenze:", font=("Arial", 15))
lower_label.pack(fill="x")

lower_entry = ttk.Entry(root, textvariable=lower_value, font=("Arial", 15))
lower_entry.pack(fill="x")

upper_label = ttk.Label(root, text="Obergrenze:", font=("Arial", 15))
upper_label.pack(fill="x")

upper_entry = ttk.Entry(root, textvariable=upper_value, font=("Arial", 15))
upper_entry.pack(fill="x")

input_Button = ttk.Button(root, text="neue Grenzen übernehmen", command=overtaking)
input_Button.pack(fill="x")

Anweisung1_label = ttk.Label(root, textvariable=anweisung1_value, font=("Arial", 15))
Anweisung1_label.pack(fill="x")
Anweisung2_label = ttk.Label(root, text=Anweisung2, font=("Arial", 15))
Anweisung2_label.pack(fill="x")

Anweisung3_label = ttk.Label(root, textvariable=anweisung2_value, font=("Arial", 15))
Anweisung3_label.pack(fill="x")

Guess_entry = ttk.Entry(root, textvariable=guess_value, font=("Arial", 15))
Guess_entry.pack(fill="x")

guess_Button = ttk.Button(root, text="eingegebene Zahl testen", command=check_Secret)
guess_Button.pack(fill="x")

antwort_value = tk.StringVar()
antwort_label = ttk.Label(root, textvariable=antwort_value, font=("Arial", 15))
antwort_label.pack(fill="x")

anzahl_value = tk.StringVar()
anzahl_label = ttk.Label(root, textvariable=anzahl_value)
anzahl_label.pack(fill="x")

new_Round_Button = ttk.Button(root, text="Neue Runde", command=new_Round)
new_Round_Button.pack(fill="x")

quit_Button = ttk.Button(text="Programm beenden", command=root.destroy)
quit_Button.pack(side="bottom")

root.mainloop()


