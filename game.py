#============Importaciones=======================
import time
import sys
#============Colores=======================
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    AZULC = '\033[90m' #AZUL FONDO
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    
#============Inicio del juego=======================
titulo=("Hola bienvenido a La leyenda del angel caído")
print(bcolors.AZULC+titulo+bcolors.RESET)

print(" ") #Sirve para dar espacios en blanco 
print(" ")
#=========Lobby=================================
a = "MENU"
print(a.center(20)) #sirve para poner el texto en el lugar que necesites
print(" ")
time.sleep(5)
print(bcolors.OK+"Selecciona [si] o [no]"+bcolors.RESET)
time.sleep(1)
star=str(input("Quieres iniciar si o no: "))


#=======================Juego acabadof1===========================================
if star=="no":
    print(" ")
    print("Ten lindo día")
    sys.exit()
#=======================Edad=======================================================
ed=int(input("Introduce tu edad"))

if ed<18:
    print("Eres un crio")
else:
    print("Eres un machito")
    
if ed<18:
    a=("me gusta tienes")
    b=("es de alguien muy pequeño")
    print(a,ed,b)
    
if ed>18:
    a=("me gusta tienes")
    b=("es de alguien muy mayor")
    print(a,ed,b)

#============Primera parte===========================
if star=="si":
    print(" ")
    print("Esta historia empieza como otras...")


if star=="si":
    print(" ")
    print(bcolors.OK+"Selecciona [si] o [no]"+bcolors.RESET)
p1=str(input("Eres bueno si o no?"))
    
if p1=="si" or p1!="no":
    print(" ")
    print("Entonces por que")
    
elif p1=="no":
    print(" ")
    print("Estas mal de la cabeza")

#==================Segunda parte=====================
if p1=="si" or p1=="no":  
    print(" ")
    print(bcolors.OK+"Selecciona [tu] o [yo]"+bcolors.RESET)
p2=str(input("Quien te hizo tanto daño:"))

    
if p2=="tu":
    print(" ")
    print("Es mi culpa")
    
elif p2=="yo":
    print(" ")
    print("Es tu culpa")
#============Tercera parte=====================


#==============Cuarta parte========================
    
    
#comandos guardados
def papa():
    ed=int(input("Introduce tu edad"))
    pp=int(input("Introduce la edad de tu papá"))
    resta = pp - ed
    print("tu papa tiene",resta)

papa()
