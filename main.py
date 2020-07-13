e=("\033[1;31m"+"PERU"+'\033[0;m')
E=("\033[1;34m"+"AIRLINE"+'\033[0;m')
print(e + E)
print()
print(print("\033[1;37m"+"Bienvenidos a PERU AIRLINE"+'\033[0;m'))
print()
print("\033[1;37m"+"HORARIO DE SALIDA DE VUELOS NACIONALES"+'\033[43;m')
print()

#horarios de salida
CIUDADES = 11 
HORARIOS = 6
ciudades = ["arequipa", "ayacucho" , "cusco", "iquitos", "juliaca" ,"pucalpa","tacna","piura","tumbes","tarapoto", "trujillo"]
horarios =[[10.30, 12.10, 13.40, 14.00, 16.20, 18.00],
           [6.00, 7.25, 8.03, 9.00, 14.27, 16.30],
           [6.50, 8.30, 12.45, 14.19, 17.20, 20.00],
           [6.20, 8.50, 12.00, 15.05, 17.55, 21.01],
           [5.33, 6.40, 8.45, 9.56, 16.23, 19.44],
           [9.21, 12.38, 18.00, 21.22, 22.22, 22.50],
           [7.35, 9.29, 11.06, 11.52, 13.02, 14.30],
           [5.00, 9.59, 16.02, 19.15, 23.30, 23.55],
           [6.30, 8.15, 10.25, 11.00 , 15.20, 19.00],
           [5.20, 8.55, 10.00, 10.45, 15.20, 17.25],
           [5.45, 17.55, 20.20, 23.00, 23.10, 24.00]
          ] 

for i in range (CIUDADES):
  print("%10s" %ciudades[i], end="  ")
  for j in range(HORARIOS):
    print("%12.2f" %(horarios[i][j]), end=" ")
  print()
print()

#asientos de salida
asientos = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#asientos de retorno
asientos2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#costo pasaje: 
def costopasaje(destino): 
    if destino =='arequipa':
      return 80
    if destino=='ayacucho': 
      return 50
    if destino=='cusco':
      return 55
    if destino=='iquitos':
      return 45 
    if destino=='pucalpa':
      return 30
    if destino=='tacna':
      return 34
    if destino=='piura':
      return 32
    if destino=='tumbes':
      return 48
    else:
      return 30

#comprar pasaje de ida
def ida_y_vuelta(destino):
  fecha1 = input("Ingrese fecha de salida: ")
  print()
  pos = -1
  for i in range(len(ciudades)):
    if ciudades[i] == destino:
      pos=i
      break
  print("Los horarios para",destino, "son:")
    
  print()
  for c in horarios[pos]:
    print(c,"\t", end="")  
  hora = input("Que horario desea: ") 
  print()

  #asiento de ida   
  for l in range(0,4):
    for a in range(0,40):
      asientos[l][a]
  count = 0
  
  while count <= 160:
    f = input("Escoja el número de fila: ") #Escojer una letra A, B, C o D
    def asiento(f): #La función cambia la letra por un número
      if f == 'A':
        return 1
      if f == 'B':
        return 2
      if f == 'C':
        return 3
      else:
        return 4
    k = int(input("Escoja número de asiento del 1-40: "))
    if asientos[asiento(f)-1][k-1] == 0:
      asientos[asiento(f)-1][k-1] = 1
      count = count + 1
      print()
      break
    else:
      print("Asiento reservado, elija otro por favor")

  #regreso
  fecha2 = input("Ingrese fecha de retorno: ")
  hora2 = input("Elija horario de retorno: ")  
  
  #asientos de retorno:
  for l in range(0,4):
    for a in range(0,40):
      asientos2[l][a]
  count = 0
  
  while count <= 160:
    f2 = input("Escoja una fila: ") #Escojer una letra A, B, C o D
    def asiento(f2): #La función cambia la letra por un número
      if f2 == 'A':
        return 1
      if f2 == 'B':
        return 2
      if f2 == 'C':
        return 3
      else:
        return 4
    k2 = int(input("Escoja número de asiento del 1-40: "))
    if asientos2[asiento(f2)-1][k2-1] == 0:
      asientos2[asiento(f2)-1][k2-1] = 1
      count = count + 1
      print()
      print("Reserva éxitosa")
      break
    else:
      print("Asiento reservado, elija otro por favor")
  
  #impresion de datos ingresados hasta el momento 
  print()
  print("Su pasaje para", destino, "es el siguiente")
  print("Su fecha de salida es para el",fecha1)
  print("Lugar de Salida: Lima     ", "Lugar de llegada: ", destino)
  print("Hora de partida: ", hora)
  print("Vuelo N°:1", "Asiento: ", f, k)
  print()
  print("Su pasaje de retorno para Lima es el siguiente")
  print("Su fecha de retorno es para el", fecha2)
  print("Lugar de Salida:", destino, "   Lugar de llegada: Lima")
  print("Hora de retorno: ", hora2)
  print("Vuelo N°: 1", "Asiento: ", f2, k2)

  #datos 
  print()
  nombre = input("Nombres: ")
  apellido = input("Apellidos: ")
  DNI = int(input("Numero de DNI: "))
  print()

  #almacenamiento de pasajes de salida
  almacenamiento = "pasajeros.txt"
  archivo = open(almacenamiento, "w+")
  archivo.write("Salida: Lima   Destino: ")
  archivo.write(destino + "\n")
  archivo.write("Fecha: ")
  archivo.write(fecha1)
  archivo.write("  Hora: ")
  archivo.write(hora + "\n")
  archivo.write("N° Vuelo: 1   Asiento: ")
  archivo.write(f)
  archivo.write(str(k) + "\n")
  archivo.write("Pasaje N°:  1" + "\n")
  archivo.write("Nombres:")
  archivo.write(nombre)
  archivo.write("   Apellidos:")
  archivo.write(apellido + "\n")
  archivo.write("DNI: ")
  archivo.write(str(DNI) + "\n")
  archivo.close()

  #alamcenamiento de pasajes de regreso:
  almacenamiento2 = "pasajeros2.txt"
  archivo = open(almacenamiento2, "w+")
  archivo.write("Salida: ")
  archivo.write(destino)
  archivo.write("   Destino: Lima" + "\n")
  archivo.write("Fecha: ")
  archivo.write(fecha2)
  archivo.write("  Hora: ")
  archivo.write(hora2 + "\n")
  archivo.write("N° Vuelo: 1   Asiento: ")
  archivo.write(f2)
  archivo.write(str(k2) + "\n")
  archivo.write("Pasaje N°:  1" + "\n")
  archivo.write("Nombres:")
  archivo.write(nombre)
  archivo.write("   Apellidos:")
  archivo.write(apellido + "\n")
  archivo.write("DNI: ")
  archivo.write(str(DNI) + "\n")
  archivo.close()  

#Elejir lugar, asiento y horario para viaje de solo ida
def solo_ida(destino):
  fecha1=input("Ingrese la fecha de viaje: ")

  print()
  pos = -1
  for i in range(len(ciudades)):
    if ciudades[i] == destino:
      pos=i
      break
  print("Los horarios para",destino, "son:")
    
  print()
  for c in horarios[pos]:
    print(c,"\t", end="")  
  hora = input("Que horario desea: ") 
  print()

  #Reserva de asientos
  print("Por favor, escoja un asiento")
  
  for l in range(0,4):
    for a in range(0,40):
      asientos[l][a]
  count = 0
  
  while count <= 160:
    f = input("Elija un asiento: ") #Escojer una letra A, B, C o D
    def asiento(f): #La función cambia la letra por un número
      if f == 'A':
        return 1
      if f == 'B':
        return 2
      if f == 'C':
        return 3
      else:
        return 4
    k = int(input("Escoja número de asiento del 1-40: "))
    if asientos[asiento(f)-1][k -1] == 0:
      asientos[asiento(f)-1][k-1] = 1
      count = count + 1
      print()
      print("Reserva éxitosa")
      break
    else:
      print("Asiento reservado, elija otro por favor")

  #impresion de datos ingresados hasta el momento 
  print()
  print()
  print("Su pasaje para", destino, "es el siguiente")
  print("Su fecha de salida es para el",fecha1)
  print("Lugar de Salida: Lima     ", "Lugar de llegada: ", destino)
  print("Hora de partida: ", hora)
  print("Vuelo N°: 1", "Asiento: ", f, k)

  #datos 
  print()
  nombre = input("Nombres: ")
  apellido = input("Apellidos: ")
  DNI = int(input("Numero de DNI: "))

  #almacenamiento de pasajes 
  almacenamiento = "pasajeros.txt"
  archivo = open(almacenamiento, "w+")
  archivo.write("Salida: Lima   Destino: ")
  archivo.write(destino + "\n")
  archivo.write("Fecha: ")
  archivo.write(fecha1)
  archivo.write("  Hora: ")
  archivo.write(hora + "\n")
  archivo.write("N° Vuelo: 1   Asiento: ")
  archivo.write(f)
  archivo.write(str(k) + "\n")
  archivo.write("Pasaje N°:  1" + "\n")
  archivo.write("Nombres:")
  archivo.write(nombre)
  archivo.write("   Apellidos:")
  archivo.write(apellido + "\n")
  archivo.write("DNI: ")
  archivo.write(str(DNI) + "\n")
  archivo.close()

#escoger un destino
while True:
    destino = input("Escoja el lugar de destino: ")
    if destino in ciudades:
      print("Su lugar de destino es",destino)
      break
    else: 
      print("Esta ciudad no se encuentra disponible")

#elegir opción 
print('Selecciona una opción: ')
print('1.- Comprar pasaje de ida y vuelta')
print('2.- Comprar pasaje de solo ida')

def opciones(opc):
  if opc == 1:
   return ida_y_vuelta(destino)
  else:
    return solo_ida(destino)
opc =int(input("Ingrese una opción: "))
print(opciones(opc))

#Ingrsar correo
correo = input("Correo: ")
print()

#Si viaja otra persona
n = 1
while True:
  l=input("¿viaja con otra persona?: ")
  if l == 'si':
     n = n + 1
     nombre2 = input("Nombres: ")
     apellido2 = input("Apellidos: ")
     DNI2 = int(input("Numero de DNI: "))
     correo2=input("Ingrese su correo electronico: ")

     inputFile = open("pasajeros.txt", "a")
     inputFile.write("Pasaje N°: ")
     inputFile.write(str(n) + "\n")
     inputFile.write("Nombres:")
     inputFile.write(nombre2)
     inputFile.write("   Apellidos:")
     inputFile.write(apellido2 + "\n")
     inputFile.write("DNI: ")
     inputFile.write(str(DNI2) + "\n")
     inputFile.close()
  else:
    break 
print("El total de boletos reservados es de:", n)
print()

#confirmar la compra y hacer la compra
k=input("¿Quiere proseguir con la compra?: ")
if k == "si":
  if n > 1:
    if opc == 2:
      total =  costopasaje(destino)*n
      print("El costo a pagar por persona es $", costopasaje(destino))
      print("El total a pagar es $", total)
    else:
      total = costopasaje(destino)*2*n
      print("El costo a pagar por persona es $", costopasaje(destino)*2)
      print("El total a pagar es $", total)
  else:
   if opc == 2:
     total =costopasaje(destino)
     print("El total a pagar es $", costopasaje(destino))
   else:
     total =costopasaje(destino)*2
     print("El total a pagar es $", costopasaje(destino)* 2)
  print("\033[1;32m"+"Reserva realizada"+'\033[0;m')
else:
  print("\033[1;31m"+"Reserva cancelada"+'\033[0;m')

#realizar el pago
print()
H=input("¿Qusiera realizar el pago? ")
if H=='si':
  print("Usted ha pagado $",total)
  print()
  print("\033[1;32m"+"Compra realizada y enviada a su correo electrónico"+'\033[0;m')
  print("\033[1;32m"+"Por favor, presentarse en el aereopuerto 2 horas antes de su hora de salida"+'\033[0;m')

  #gmail
  import smtplib
  mensaje = 'Su compra ha sido realizada exitosamente '

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login('peruairline@gmail.com', 'grupoicc')
  server.sendmail('peruairline@gmail.com',correo, mensaje)
  server.quit()
else:
  print("\033[1;34m"+"Su compra ha sido cancelada"+'\033[0;m')  
