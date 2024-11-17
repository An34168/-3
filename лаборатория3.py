import tkinter as tk
import random
import string
import pygame  


pygame.mixer.init()


def play_music():
    pygame.mixer.music.load("C:\\Users\\Janeth Yanez\\OneDrive\\Documentos\\TRABAJOS DE DISEÑO 3D\\PROYECTOS DE PYTHON\\laboratorio 3\\musica1.wav")
    pygame.mixer.music.play(-1)  

def stop_music():
    pygame.mixer.music.stop()  
def generate_key():
    key = ""
    for _ in range(4): 
        block = random.choice(string.digits)  
        block += ''.join(random.choices(string.ascii_uppercase, k=3)) 
        block = ''.join(random.sample(block, len(block)))  
        key += block + "-"
    key = key[:-1] 
    key_entry.delete(0, tk.END)  
    key_entry.insert(0, key)  


root = tk.Tk()
root.title("Generador de Claves")


key_entry = tk.Entry(root, width=25, font=("Arial", 16))
key_entry.pack(pady=20)


generate_button = tk.Button(root, text="Generar Clave", command=generate_key)
generate_button.pack()

play_button = tk.Button(root, text="Reproducir Música", command=play_music)
play_button.pack(pady=5)

stop_button = tk.Button(root, text="Detener Música", command=stop_music)
stop_button.pack(pady=5)
root.mainloop()


