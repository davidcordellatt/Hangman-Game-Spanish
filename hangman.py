import os
import random

name = input("¿Cual es tu nombre?: ")



creditos = """
El Ahorcado - Autor: David Cordellat - Made in Venezuela 
"""
def random_word(filepath="./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
        return(words)
           
def select_word():
    data = random_word(filepath="./archivos/data.txt")
    select_word = random.choice(data)
    select_word_list = [letter for letter in select_word]
    ocult_word = ["_"] * len(select_word_list)
    ocult_word_index = {}
    for a, letter in enumerate(select_word):
        if not ocult_word_index.get(letter): 
            ocult_word_index[letter] = []
        ocult_word_index[letter].append(a)
    
    while True:
            
            print("Buena suerte, " + name)
            print("¡Adivina la palabra!")
            for under in ocult_word:
                print(under + " ", end=" ")
            print("")

            letter = input("Ingresa una letra: ").strip().upper()
            assert letter.isalpha(), "Solo puedes ingresar letras"

            if letter in select_word_list:
                for idx in ocult_word_index[letter]:
                    ocult_word[idx] = letter

            if "_" not in ocult_word:
                
                print("¡Felicidades! " + name + " La palabra era", select_word)
                print(creditos)
                break

select_word()

if __name__ == '__main__':
   random_word()