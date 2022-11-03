import os
import random
import time

start_time = time.time()

global hits
hits = 0

os.system('clear')
name = input("¿Cual es tu nombre?: ")
name = name.strip().capitalize()

def game_mode():
       
    os.system("clear")

    t = 0
    m = ""

    select_line = random.choice(data)
    select_line_list = [letter for letter in select_line]
    ocult_line = ["_"] * len(select_line_list)
    ocult_line_index = {}

    for a, letter in enumerate(select_line):
        if not ocult_line_index.get(letter): 
            ocult_line_index[letter] = []
        ocult_line_index[letter].append(a)

    if via == "1" or via == "palabra":
        for i in select_line:
            t += 0.75
            tries = int(t)

    elif via == "2" or via == "frase":
        for i in select_line:
            t += 0.20
            tries = int(t)

    space = " "

    if space in ocult_line_index:
        for idx in ocult_line_index[space]:
            ocult_line[idx] = space

    coma = ","

    if coma in ocult_line_index:
        for idx in ocult_line_index[coma]:
            ocult_line[idx] = coma

    while True:

        os.system("clear")
        print(f"Buena suerte, {name}.")
        print(m)
        print(f"¡Adivina la {modus}!")
        print(f"Tienes {tries} intentos")
        m = ""

        for under in ocult_line:    
            print(under + " ", end=" ")
        print("")

        letter = input("\n" "Ingresa una letra: ").strip().upper()

        if letter == select_line:
            os.system("clear")
            print(f"""¡Muy bien {name}!, la {modus} correcta era: 

{select_line.capitalize()}""")
            win()     
            break  

        elif "_" not in ocult_line:
            os.system("clear")
            print(f"""¡Felicidades! {name}, la {modus} era: 

{select_line.capitalize()}""")
            win()
            break

        if "_" not in ocult_line:
            tries = tries - 1
                  
        if letter in select_line_list:
            for idx in ocult_line_index[letter]:
                ocult_line[idx] = letter

        elif letter not in select_line_list:
            tries = tries - 1

            if not letter.isalpha():    
                m = "No deberías intentar con numeros \n"

        if tries == 0:
            os.system("clear")
            print(f"{name} ¡Perdiste!, la palabra correcta era {select_line.capitalize()}" )
            reload()
            break

def credits():

    os.system("clear")
    end = """
Hangman Game
Autor: David Cordellat
Made in Venezuela
20/10/2022"""
    print(f"Gracias por jugar, {name}")
    end_time = time.time() - start_time

    if end_time < 60:
        print(f"Jugaste un total de {round(float(end_time), 2)} segundos")

    if end_time >= 60:
        end_time /= 60
        print(f"Jugaste un total de {round(float(end_time), 2)} minutos")

    if hits == 0:
        print("Y no tuviste aciertos")
        
    else:
        print(f"Y tuviste un total de {str(hits)} aciertos")

    print(end)

def run():

    os.system("clear")

    global via
    global data
    global modus

    via = input("""
¿Que quieres adivinar?

1.- Palabra
2.- Frase
R: """).strip().lower()

    if via == "1" or via == "palabra":
        data = word(filepath="./data.txt")
        modus = "palabra"
    
    elif via == "2" or via == "frase":
        data = phrases(filepath="./frases.txt")
        modus = "frase"

    game_mode()

def win():
    global hits
    hits = hits + 1
    reload()

def reload():

    reload = input("""
¿Quieres volver a jugar?

1.- Si
2.- No
R: """).strip().lower()

    if reload == "1" or reload == "si":
        run()

    elif reload == "2" or reload == "no":
        credits()

def word(filepath="./data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
        return(words)
    
def phrases(filepath="./frases.txt"):
    phrases = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            phrases.append(line.strip().upper())
        return(phrases)
              
if __name__ == '__main__':
   run()