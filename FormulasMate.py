####################Menu####################################################
print("Bienvenido dime que formula deseas hacer:")

a=["Suma[S]", "Resta[R]", "Multiplicacion[M]", "Division[D]", "Otros[O]"]

print(" ")##########> Lo ocupo para estetica

for lista in range (len(a)):##>Determino un rango
    print(a[lista])
for elemento in a:
    print(elemento)
    
print(" ")##########> Lo ocupo para estetica 

x=str(input("Selecciona la formula:"))######>pongo "str" porque estoy pidiendo un valor no numerico
##############################Suma##########################################

if x=="S":
    print ("Seccion suma")
    def suma(a,b):
        suma=a+b
        print(suma)
            
    def main():
        a=int(input("Selecciona un primer numero:"))
        b=int(input("Selecciona un segundo numero:"))
        suma(a,b)
    main()
#############################Suma#####################################################
if x=="R":
    print ("Seccion resta")
    def resta(a,b):
        resta=a-b
        print(resta)
            
    def main():
        a=int(input("Selecciona un primer numero:"))
        b=int(input("Selecciona un segundo numero:"))
        resta(a,b)
    main()
###############################Resta##############################################
if x=="M":
    print ("Seccion Multiplicación")
    def multiplicacion(a,b):
      b9  multiplicacion=a*b
        print(multiplicacion)
            
    def main():
        a=int(input("Selecciona un primer numero:"))
        b=int(input("Selecciona un segundo numero:"))
        multiplicacion(a,b)
    main()
##################################Multiplicacion################################
if x=="D":
    print ("Seccion Division")
    
    a=["Decimal[D]", "Entera[E]", "Residuo[R]"]

    for lista in range (len(a)):
        print(a[lista])
        
        
    x=str(input("Deseas hacer una division:"))
    
    if x=="D":
        def Decimal(a,b):
            decimal=a/b
            print(decimal)
                 
        def main():
            a=float(input("Selecciona un primer numero:"))#############>ocupe el float para decimales
            b=float(input("Selecciona un segundo numero:"))
            decimal(a,b)
        main()
    if x=="E":
        def Entera(a,b):
            entera=a//b
            print(entera)
                 
        def main():
            a=float(input("Selecciona un primer numero:"))#############>ocupe el float para decimales
            b=float(input("Selecciona un segundo numero:"))
            Entera(a,b)
        main()
    if x=="R":
        def Residuo(a,b):
            residuo=a%b
            print(residuo)
                 
        def main():
            a=float(input("Selecciona un primer numero:"))#############>ocupe el float para decimales
            b=float(input("Selecciona un segundo numero:"))
            Residuo(a,b)
        main()
###############Division###############################################################

if x=="O":
    
    a=["Area[A]","Perimetro[P]","Contador[C]","Serie[S]"]
    
    for lista in range (len(a)):##>Determino un rango
        print(a[lista])
        
    x=str(input("Selecciona la formula:"))
#############################Menu "Otros"##############################################
    if x=="A":
        a=["Triangulo[A]","Cuadrado[C]", "Rectangulo[R]"]
            
        for lista in range (len(a)):##>Determino un rango
            print(a[lista])
        
        x=str(input("Selecciona la formula:"))
        if x=="A":
            def triangulo(a,b):
                Area=(a*b)/2
                print(Area)
                 
            def main():
                a=float(input("Selecciona tu base:"))#############>ocupe el float para decimales
                b=float(input("Selecciona tu altura:"))
                
                triangulo(a,b)
                
            main()
            
        if x=="C":
            def Cuadrado(a,b):
                area=a*b
                print(area)
            def main():
                a=float(input("Selecciona tu base:"))#############>ocupe el float para decimales
                b=float(input("Selecciona tu altura:"))
                Cuadrado(a,b)
            main()
            
        if x=="R":
            def Rectangulo(a,b):
                area=a*b
                print(area)
            def main():
                a=float(input("Selecciona tu base:"))#############>ocupe el float para decimales
                b=float(input("Selecciona tu altura:"))
                Rectangulo(a,b)
###############################Area##################################################################################################################
    if x=="P":
        a=["Triangulo[T]","Cuadrado[C]", "Rectangulo[R]" ]
            
        for lista in range (len(a)):##>Determino un rango
            print(a[lista])
        
        x=str(input("Selecciona la formula:"))
        if x=="T":
            def Triangulo(a):
                area=a*3
                print(area)
            def main():
                a=int(input("Selecciona tu base:"))
                Triangulo(a)
            main()
        if x=="C":
            def Cuadrado(a):
                area=a*4
                print(area)
            def main():
                a=int(input("Selecciona tu base:"))
                Cuadrado(a)
            main()
        if x=="R":
            def Rectangulo(a,b):
                area=a*2+b*2
                print(area)
            def main():
                a=int(input("Selecciona tu lado 1:"))
                b=int(input("Selecciona tu lado 2:"))
                Rectangulo(a)
            main()
            
    if x=="C":
        def contador(a,b):
            numero=a
            while a<b+1:
                print(a)
                a+=1
                
                
        def main():
            a=int(input("Selecciona tu numero minimo:"))
            b=int(input("Selecciona tu numero maximo:"))
            contador(a,b)
        main()
    if x=="S":
        def series(x,y,z):
            for serie in range(x,y+1,z):
                print(serie)
                
        def main():
            x=int(input("Selecciona tu numero minimo:"))
            y=int(input("Selecciona tu numero maximo:"))
            z=int(input("Selecciona el orden de la sucesion:"))
            series(x,y,z)
        main()
#################################Series#############################################
                
