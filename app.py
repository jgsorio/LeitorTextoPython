import os

import gtts
from playsound import playsound


def open_file_and_play():
    file = open('texto.txt', 'r')
    for linha in file:
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save('frase.mp3')
        playsound('frase.mp3')


texto = input("Digite o que voce quer que o Python fale: ")
if texto:
    file = open('texto.txt', 'w+')
    file.write(texto)
    file.close()
    open_file_and_play()
else:
    print("Voce precisa digitar algo")
    os.remove('texto.txt')
