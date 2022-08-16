#============Importaciones=======================
import time
#============Colores=======================
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    AZULC = '\033[90m'
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    
#============Inicio del juego=======================
print(bcolors.AZULC+"Hola bienvenido a La leyenda del angel caído"+bcolors.RESET)
print("Cargando...1%")
time.sleep(2)
print("Cargando...15%")
time.sleep(2)
print("Cargando...20%")
time.sleep(2)
print("Cargando...40%")
time.sleep(2)
print("Cargando...50%")
time.sleep(2)
print("Cargando...78%")
time.sleep(2)
print("Cargando...90%")
time.sleep(2)
print("Cargando...100%")
time.sleep(2)
print(" ")
print(" ")
    #=========Lobby=================================
a = "MENU"
print(a.center(20))
print(" ")
time.sleep(5)
print(bcolors.OK+"Selecciona [si] o [no]"+bcolors.RESET)
time.sleep(1)
star=str(input("Quieres iniciar si o no:"))

if star=="si":
    print(" ")
    print("Esta historia empieza como otras...")
else:
    print(" ")
    print("Ten lindo día")
#============Primera parte===========================
if star=="si":
    print(" ")
    print(bcolors.OK+"Selecciona [si] o [no]"+bcolors.RESET)
    p1=str(input("Eres bueno si o no?"))
    
if p1=="si":
    print(" ")
    print("Entonces por que")
else:
    print(" ")
    print("Estas mal de la cabeza")
#==================Segunda parte=====================
if p1=="si":
    print(" ")
    print(bcolors.OK+"Selecciona [tu] o [yo]"+bcolors.RESET)
    p2=str(input("Quien te hizo tanto daño:"))
    
if p2=="tu":
    print(" ")
    print("Es mi culpa")
    
elif p2=="yo":
    print(" ")
    print("Es tu culpa")