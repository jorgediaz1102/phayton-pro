import random

elementos = input("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") 
long =  int(input("de cuantas letra o numeros para crear tu contraseña"))
contraseña = ""
for i in range(long):
    contraseña += random.choice(elementos)
print(contraseña)
