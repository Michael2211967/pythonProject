import random
import tkinter as tk
from tkinter import ttk
import time
import datum


class guessing:
    # Variable werden bereitgestellt:
    def __init__(self):
        self.lower_bound = 1
        self.upper_bound = 100
        self.count = 1
        self.root = tk.Tk()
        self.date = datum.datetime()
        self.root.title("{} zum Zahlenratespiel 3".format(self.date[0]))
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.secret_number, self.instruction1 = self.create_secret()
        self.instruction2 = "Deine Aufgabe ist es zu erraten, welche Zahl es ist."
        self.instruction3 = "Wähle eine Ganzzahl zwischen {} und {}:".format(self.lower_bound, self.upper_bound)
        self.guess = None

        self.lower_value = tk.StringVar(value=str(self.lower_bound))
        self.upper_value = tk.StringVar(value=str(self.upper_bound))
        self.instruction1_value = tk.StringVar(value=self.instruction1)
        self.instruction2_value = tk.StringVar(value=self.instruction3)
        self.guess_value = tk.StringVar()

        self.limit_frame = tk.Frame(self.root, height="12", relief="ridge")
        self.entry_frame = ttk.Frame(self.limit_frame,)
        self.lower_frame = ttk.Frame(self.entry_frame, width=250)
        self.lower_label = ttk.Label(self.lower_frame, text="Untergrenze:", font=("Arial", 8))
        self.lower_label.pack(fill="x", padx=5, pady=3)

        self.lower_entry = ttk.Entry(self.lower_frame, textvariable=self.lower_value, font=("Arial", 12))
        self.lower_entry.pack(fill="x", padx=5, pady=3)
        self.lower_frame.pack(side="left")

        self.upper_frame = ttk.Frame(self.entry_frame, width=250)
        self.upper_label = ttk.Label(self.upper_frame, text="Obergrenze:", font=("Arial", 8))
        self.upper_label.pack(fill="x", padx=5, pady=3)

        self.upper_entry = ttk.Entry(self.upper_frame, textvariable=self.upper_value, font=("Arial", 12))
        self.upper_entry.pack(fill="x", padx=5, pady=3)
        self.upper_frame.pack(side="right")
        self.entry_frame.pack(fill="x", padx=5, pady=3)

        self.input_Button = ttk.Button(self.limit_frame, text="neue Grenzen übernehmen", width="350", command=self.overtaking)
        self.input_Button.pack(side="bottom", padx=5, pady=3)
        self.limit_frame.pack(fill="x", padx=5, pady=3)

        self.description_frame = ttk.Frame(self.root, relief="ridge")
        self.instruction1_label = ttk.Label(self.description_frame, textvariable=self.instruction1_value, font=("Arial", 10))
        self.instruction1_label.pack(fill="x", padx=5, pady=3)

        self.instruction2_label = ttk.Label(self.description_frame, text=self.instruction2, font=("Arial", 10))
        self.instruction2_label.pack(fill="x", padx=5, pady=3)
        self.description_frame.pack(fill="x", padx=5, pady=3)

        self.guess_frame = ttk.Frame(self.root, relief="ridge")
        self.guess_entry_frame = ttk.Frame(self.guess_frame)
        self.instruction3_label = ttk.Label(self.guess_entry_frame, textvariable=self.instruction2_value, font=("Arial", 10))
        self.instruction3_label.pack(side="left", padx=5, pady=3)

        self.Guess_entry = ttk.Entry(self.guess_entry_frame, textvariable=self.guess_value, font=("Arial", 12))
        self.Guess_entry.pack(side="right", padx=5, pady=3)
        self.guess_entry_frame.pack(fill="x", padx=5, pady=3)

        self.guess_Button = ttk.Button(self.guess_frame, text="eingegebene Zahl testen", command=self.check_Secret)
        self.guess_Button.pack(side="bottom", fill="x", padx=5, pady=3)
        self.guess_frame.pack(fill="x", padx=5, pady=3)

        self.answer_frame = ttk.Frame(self.root, relief="ridge")
        self.answer_value = tk.StringVar()
        self.answer_label = ttk.Label(self.answer_frame, textvariable=self.answer_value, font=("Arial", 10))
        self.answer_label.pack(fill="x", padx=5, pady=3)

        self.count_value = tk.StringVar()
        self.count_label = ttk.Label(self.answer_frame, textvariable=self.count_value, font=("Arial", 10))
        self.count_label.pack(fill="x", padx=5, pady=3)
        self.answer_frame.pack(fill="x", padx=5, pady=3)

        self.new_Round_Button = ttk.Button(self.root, text="Neue Runde", command=self.new_Round)
        self.new_Round_Button.pack(fill="x", padx=5, pady=5)

        self.quit_Button = ttk.Button(text="Programm beenden", command=self.root.destroy)
        self.quit_Button.pack(side="bottom", pady=5)

        self.root.mainloop()

    # eingegebene Grenzwerte werden übernommen und Spiel neugestartet
    def overtaking(self):
        self.lower_bound = int(self.lower_entry.get())
        self.upper_bound = int(self.upper_entry.get())
        self.new_Round()

    # geheime Zahl wird erzeugt
    def create_secret(self):
        secret_number = random.randint(self.lower_bound, self.upper_bound)
        lt = time.localtime()
        actual_hour = lt[3]
        actual_min = lt[4]
        instruction1 = "Es wurde um {:02d}:{:02d} eine Zufallszahl zwischen {}  und  {} generiert.".format(actual_hour, actual_min, self.lower_bound, self.upper_bound)
        self.instruction3 = "Wähle eine Ganzzahl zwischen {} und {}:".format(self.lower_bound, self.upper_bound)
        return(secret_number, instruction1)
    
    # geheime Zahl wird mit eingegebener Zahl verglichen
    def check_Secret(self):
        guess = int(self.Guess_entry.get())
        print("Versuch {:>3d}:".format(self.count), end=' ')

        if guess == self.secret_number:
            print(self.secret_number)
            print(" Neue Runde ".center(80, '='))
            answer = ("Yeahh, das ist korrekt")
            self.count_value.set("Du hast {} Versuche benötigt, um die korrekte Zahl zu erraten!".format(self.count))

        elif guess < self.secret_number:
            print("Die gesuchte Zahl ist größer als {}!".format(guess))
            self.count += 1
            answer = ("Die gesuchte Zahl ist größer als {}!".format(guess))

        else:
            print("Die gesuchte Zahl ist kleiner als {}".format(guess))
            self.count += 1
            answer = ("Die gesuchte Zahl ist kleiner als {}".format(guess))
        self.answer_value.set(answer)
        
    # Variablen werden zurückgesetzt
    def new_Round(self):
        self.count = 1
        self.count_value.set("")
        self.secret_number, self.instruction1 = self.create_secret()
        self.instruction1_value.set(self.instruction1)
        self.instruction2_value.set("Wähle eine Ganzzahl zwischen {} und {}:".format(self.lower_bound, self.upper_bound))
        self.answer_value.set("")
        self.guess_value.set("")
        return


g = guessing()
