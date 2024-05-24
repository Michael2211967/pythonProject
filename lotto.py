#! /usr/bin/python3

import random as rnd
import sys
import os
import funktionen
import datum

class Lotto:
        __menutext = """
*************************
***  Lotto-Generator  ***
*************************

* Zahlen (A)uslesen
* Zahlen (E)rstellen
* (V)erzeichnis wechseln
* (B)eenden
        """
        
        def __init__(self, filename):
                self.path = filename
                if sys.platform == "win32":
                        self.user = os.environ['USERNAME']
                else:
                        self.user = os.environ['USER']

        def lotto_read(self):
                funktionen.clear()
                try:         
                        file = open(self.path, "r")
                        lotto = file.read()
                        file.close()
                        print(f"\n{self.path}:")
                        print(lotto)
                except:
                        print(f"\nDatei {self.path} ist nicht im aktuellen Verzeichnis!")
                menu = input("Zum Beenden Return drücken:")

        def lotto_create(self):
                funktionen.clear()
                zeilen = int(input("Wieviele Zeilen sind erwünscht? "))
                lotto=[]
                lotto.extend(range(1,50))
                date = funktionen.date()
                time_now = funktionen.time_now()
                file = open(self.path, 'w')
                file.write(date + '  ' + time_now)
                print(date + "  " + time_now, end = ' ')
                for i in range(zeilen):
                    ergebnis = rnd.sample(lotto, 6)
                    ergebnis.sort()
                    file.write("\n{:2d}. ".format(i+1))
                    print("\n{:2d}.".format(i+1), end=" ")
                    for j in ergebnis:
                        print("{:2d}".format(j), end=" ")
                        file.write("{:2d} ".format(j))
                file.write("\n")
                print("\n")
                menu = input("Zum Beenden Return drücken:")

        def changedir(self):
                funktionen.clear()
                files = os.listdir()
                files.sort()
                path = ""
                for entry in files:
                        path += "{entry:<30}{bytes:>10} Byte\n".format(
                                entry=entry,
                                bytes=os.path.getsize(entry))
                print(path)
                newPath = input("Bitte Arbeitsverzeichnis eingeben: ")
                try:
                        os.chdir(newPath)
                except:
                        print("Verzeichnis '{}' ist nicht vorhanden!".format(newPath))
                menu = input("Zum Beenden Return drücken:")

        def run(self):
                choice = "-"
                while choice not in "Bb":
                        funktionen.clear()
                        self.date = datum.datetime()
                        print("{} {}".format(self.date[0], self.user))
                        print("\naktuelles Verzeichnis: ", os.getcwd())
                        print(self.__menutext)
                        choice = input("Ihre Wahl: ")
                        if choice in "Aa": self.lotto_read()
                        elif choice in "Ee": self.lotto_create()
                        elif choice in "Vv": self.changedir()
                print("Danke für die Benutzung des Lotto-Generators!")
                menu = input("Zum Beenden Return drücken")
                

try:
        file = sys.argv[1]
        path = file.split("/")
        
        if path[-1] != "lotto.txt":
                try:
                        os.chdir(file)
                        file = "lotto.txt"
                except:
                        print("Verzeichnis '{}' ist nicht vorhanden!".format(file))
                        file = "lotto.txt"
except:
        file = "lotto.txt"
   
l = Lotto(file)
menue = Lotto(l)

Lotto.run(l)


