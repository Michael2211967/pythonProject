import random

lower_bound = int(input("Geben Sie bitte die Untergrenze ein: "))
upper_bound = int(input("Geben Sie bitte die Obergrenze ein: "))
secret_Number = random.randint(lower_bound, upper_bound)

print("Es wurde soeben eine Zufallszahl zwischen " + str(lower_bound) + " und " + str(upper_bound) +" generiert.")
print("Deine Aufgabe ist es zu erraten, welche Zahl es ist.")
print("Viel Erfolg")

guess = None
count = 1
while guess != secret_Number:
    guess = int(input("Wähle eine Ganzzahl zwischen " + str(lower_bound) + " und " + str(upper_bound) + ": "))

    if guess == secret_Number:
        print("Yeahh, das ist korrekt")
    elif guess < secret_Number:
        print("Die gesuchte Zahl ist größer als Deine geratene Zahl!")
        count = count + 1
    else:
        print("Die gesuchte Zahl ist kleiner als Deine geratene Zahl!")
        count = count + 1
print("Du hast " + str(count) + " Versuche benötigt, um die korrekte Zahl zu erraten!")
    



