from pygame import mixer
import os
from time import sleep

pasta = "musicas"
arquivos = os.listdir(pasta)
i = -1
funcao = ""
tocando = True

print(arquivos)
mixer.init()

def proxima(atual):
    print(len(arquivos))
    if(len(arquivos) - 1 == atual):
        prox = 0
    else:
        prox = atual + 1   
    return prox

def musicaTocando():
    global tocando
    sleep(1)
    tocando = False

#mixer.music.queue(pasta + "/" + arquivos[i+1])

while(True):
    i = proxima(i)
    mixer.music.load(pasta + "/" + arquivos[i])
    mixer.music.play()
    print("Está tocando: " + arquivos[i])
    while(tocando):
        funcao = input("Tste: ")  
        if(funcao == "play"):
            mixer.music.unpause()
        elif(funcao == "pause"):
            mixer.music.pause()
        elif(funcao == "proxima"):
            break
