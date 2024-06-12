import os

dir = input("Escolha o Brenatório: ")

for file in os.listdir(dir):
    if file == "img.png":
        os.rename(dir + file, dir + "breno.png")

""" print("oi", "tchau") """