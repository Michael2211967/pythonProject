import random
import tkinter as tk
from tkinter import ttk
import time
import datum
lower_bound = 1
upper_bound = 100
count = 1

def overtaking():
    global lower_bound
    global upper_bound
    lower_bound = int(lower_entry.get())
    upper_bound = int(upper_entry.get())
    new_Round()

def create_secret():
    secret_number = random.randint(lower_bound, upper_bound)
    lt = time.localtime()
    actual_hour = lt[3]
    actual_min = lt[4]
    instruction1 = "Es wurde um {:02d}:{:02d} eine Zufallszahl zwischen {}  und  {} generiert.".format(actual_hour, actual_min, lower_bound, upper_bound)
    instruction3 = "Wähle eine Ganzzahl zwischen {} und {}:".format(lower_bound, upper_bound)
    return(secret_number, instruction1)
   
    
def check_Secret():
    global count
    guess = int(Guess_entry.get())
    print("Versuch {:>3d}:".format(count), end=' ')
    
    if guess == secret_number:
        print(secret_number)
        print(" Neue Runde ".center(80, '='))
        answer = ("Yeahh, das ist korrekt")
        count_value.set("Du hast {} Versuche benötigt, um die korrekte Zahl zu erraten!".format(count))

    elif guess < secret_number:
       print("Die gesuchte Zahl ist größer als {}!".format(guess))
       count += 1
       answer = ("Die gesuchte Zahl ist größer als {}!".format(guess))

    else:
       print("Die gesuchte Zahl ist kleiner als {}".format(guess))
       count += 1
       answer = ("Die gesuchte Zahl ist kleiner als {}".format(guess))
    answer_value.set(answer)


def new_Round():
    global count
    count = 1
    count_value.set("")
    global secret_number
    secret_number, instruction1 = create_secret()
    instruction1_value.set(instruction1)
    instruction2_value.set("Wähle eine Ganzzahl zwischen {} und {}:".format(lower_bound, upper_bound))
    answer_value.set("")
    guess_value.set("")
    return

root = tk.Tk()
date = datum.datetime()
root.title("{} zum Zahlenratespiel 2".format(date[0]))
root.geometry("500x500")
root.resizable(False, False)
secret_number, instruction1 = create_secret()

instruction2 = "Deine Aufgabe ist es zu erraten, welche Zahl es ist."
instruction3 = "Wähle eine Ganzzahl zwischen {} und {}:".format(lower_bound, upper_bound)
guess = None

lower_value = tk.StringVar(value=str(lower_bound))
upper_value = tk.StringVar(value=str(upper_bound))
instruction1_value = tk.StringVar(value=instruction1)
instruction2_value = tk.StringVar(value=instruction3)
guess_value = tk.StringVar()

limit_frame = ttk.Frame(root, height="12", relief="ridge")
entry_frame = ttk.Frame(limit_frame)
lower_frame = ttk.Frame(entry_frame, width=250)
lower_label = ttk.Label(lower_frame, text="Untergrenze:", font=("Arial", 8))
lower_label.pack(fill="x", padx=5, pady=3)

lower_entry = ttk.Entry(lower_frame, textvariable=lower_value, font=("Arial", 12))
lower_entry.pack(fill="x", padx=5, pady=3)
lower_frame.pack(side="left")

upper_frame = ttk.Frame(entry_frame, width=250)
upper_label = ttk.Label(upper_frame, text="Obergrenze:", font=("Arial", 8))
upper_label.pack(fill="x", padx=5, pady=3)

upper_entry = ttk.Entry(upper_frame, textvariable=upper_value, font=("Arial", 12))
upper_entry.pack(fill="x", padx=5, pady=3)
upper_frame.pack(side="right")
entry_frame.pack(fill="x", padx=5, pady=3)

input_Button = ttk.Button(limit_frame, text="neue Grenzen übernehmen", width="350", command=overtaking)
input_Button.pack(side="bottom", padx=5, pady=3)
limit_frame.pack(fill="x", padx=5, pady=3)

description_frame = ttk.Frame(root, relief="ridge")
instruction1_label = ttk.Label(description_frame, textvariable=instruction1_value, font=("Arial", 10))
instruction1_label.pack(fill="x", padx=5, pady=3)

instruction2_label = ttk.Label(description_frame, text=instruction2, font=("Arial", 10))
instruction2_label.pack(fill="x", padx=5, pady=3)
description_frame.pack(fill="x", padx=5, pady=3)

guess_frame = ttk.Frame(root, relief="ridge")
guess_entry_frame = ttk.Frame(guess_frame)
instruction3_label = ttk.Label(guess_entry_frame, textvariable=instruction2_value, font=("Arial", 10))
instruction3_label.pack(side="left", padx=5, pady=3)

Guess_entry = ttk.Entry(guess_entry_frame, textvariable=guess_value, font=("Arial", 12))
Guess_entry.pack(side="right", padx=5, pady=3)
guess_entry_frame.pack(fill="x", padx=5, pady=3)

guess_Button = ttk.Button(guess_frame, text="eingegebene Zahl testen", command=check_Secret)
guess_Button.pack(side="bottom", fill="x", padx=5, pady=3)
guess_frame.pack(fill="x", padx=5, pady=3)

answer_frame = ttk.Frame(root, relief="ridge")
answer_value = tk.StringVar()
answer_label = ttk.Label(answer_frame, textvariable=answer_value, font=("Arial", 10))
answer_label.pack(fill="x", padx=5, pady=3)

count_value = tk.StringVar()
count_label = ttk.Label(answer_frame, textvariable=count_value, font=("Arial", 10))
count_label.pack(fill="x", padx=5, pady=3)
answer_frame.pack(fill="x", padx=5, pady=3)

new_Round_Button = ttk.Button(root, text="Neue Runde", command=new_Round)
new_Round_Button.pack(fill="x", padx=5, pady=5)

quit_Button = ttk.Button(text="Programm beenden", command=root.destroy)
quit_Button.pack(side="bottom", pady=5)

root.mainloop()


