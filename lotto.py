import time
import random as rnd
import os

class Lotto:
        __menutext = """
        ***********************
        *** Lotto-Generator ***
        ***********************

        * Zahlen (A)uslesen
        * Zahlen (E)rstellen
        * (V)erzeichnis wechseln
        * (B)eenden
        """
        
        def __init__(self, filename):
                self.path = filename


        def lotto_read(self):
                try:         
                        file = open(self.path, "r")
                        lotto = file.read()
                        file.close()
                        print(f"\n{self.path}:")
                        print(lotto)
                except:
                        print(f"\nDatei {self.path} ist nicht im aktuellen Verzeichnis!")
                

        def lotto_create(self):
                zeilen = int(input("Wieviele Zeilen sind erwünscht? "))
                lotto=[]
                lotto.extend(range(1,50))
                lt = time.localtime()
                date = "{:02d}.{:02d}.{:04d} ".format(lt[2], lt[1], lt[0])
                time_now = "{:02d}:{:02d}:{:02d}".format(lt[3], lt[4], lt[5])
                file = open(self.path, 'w')
                file.write(date + time_now)
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

        def changedir(self):
                print("aktuelles Vereichnis: ", os.getcwd())
                files = os.listdir("./")
                for entry in files:
                        print(entry)
                newPath = input("Bitte Arbeitsverzeichnis eingeben: ")
                try:
                        os.chdir(newPath)
                except:
                        print("Verzeichnis ", newPath, " ist nicht vorhanden!")

        def run(self):
                choice = "-"
                while choice not in "Bb":
                        print("\naktuelles Verzeichnis: ", os.getcwd())
                        print(self.__menutext)
                        choice = input("Ihre Wahl: ")
                        if choice in "Aa": self.lotto_read()
                        elif choice in "Ee": self.lotto_create()
                        elif choice in "Vv": self.changedir()
                print("Danke für die Benutzung des Lotto-Generators!")
                
l = Lotto("lotto.txt")
menue = Lotto(l)
Lotto.run(l)


