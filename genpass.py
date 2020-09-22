#Generador de contraseñas aleatorio de 16 caracteres
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]*,/_-"
all = lower + numbers + symbols
length = 16
password = "".join(random.sample(all,length,))
print(password)

