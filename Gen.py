import numpy
import random

def prob(num, arr):
    sum = 0
    for x in arr:
        sum = sum + x
    return (num / sum)

def conv_int(bin_arr, arr):
    str1 = ""
    for i in range(4):
        str1 = ""
        for ele in bin_arr[i]:  
            str1 += ele
        arr[i] = int(str1, 2)
    return arr

#El vel se debe enviar, será la vel de los 4 enemigos
vel = [35, 86, 42, 74]
aux = [0, 0, 0, 0]

bin_num1 = f'{0:08b}'
bin_vel = [bin_num1, bin_num1, bin_num1, bin_num1]

for i in range(4):
    bin_vel[i] = f'{vel[i]:08b}'

print("Original:")
print(bin_vel, vel)

#Escoge según su probabilidad para el cruce

for i in range(4):
    aux[i] = vel[numpy.random.choice(numpy.arange(0, 4), p = [prob(vel[0], vel), prob(vel[1], vel), prob(vel[2], vel), prob(vel[3], vel)])]

for i in range(4):
    vel[i] = aux[i]
    bin_vel[i] = f'{aux[i]:08b}'

print("Seleccionado por probabilidad:")
print(bin_vel, vel)

#Definir puntos de cruce
p1 = random.randrange(8)
p2 = random.randrange(8) 

aux[0] = bin_vel[0][0:p1] + bin_vel[1][p1:]
aux[1] = bin_vel[1][0:p1] + bin_vel[0][p1:]
aux[2] = bin_vel[2][0:p2] + bin_vel[3][p2:]
aux[3] = bin_vel[3][0:p2] + bin_vel[2][p2:]

bin_vel = aux
vel = conv_int(bin_vel, vel)

print("Cruce:")
print(bin_vel, vel)

#Mutación
for i in range(4):
    rand = random.randrange(9)
    if rand != 8:
        # El < 4 para que no cree números muy grandes
        if rand > 4:
            if bin_vel[i][rand] == '0':
                aux[i]= bin_vel[i][:rand] +'1'+ bin_vel[i][rand+1:]
            else:  aux[i] = bin_vel[i][:rand] +'0'+ bin_vel[i][rand+1:]

bin_vel = aux
vel = conv_int(bin_vel, vel)
print("Mutación:")
print(aux, vel)
